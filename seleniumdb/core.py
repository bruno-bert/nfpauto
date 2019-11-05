import os
import subprocess
import webbrowser
import time
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import *
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


import win32gui
import win32con

from seleniumdb import constant
from seleniumdb.steps_from_database import busca_steps, busca_script, busca_start_config
from seleniumdb.models import Script, Step, Start_Config
from seleniumdb.cycle_result import CycleResult
from seleniumdb.observer import Publisher

class SeleniumDB(Publisher):
 
 
 def log(self, message):
    raise Exception('log must be implemented by super class')
 def get_id(self, values):
    raise Exception('get_id must be implemented by super class')
 def get_id_to_show(self, values):
    raise Exception('get_id_to_show must be implemented by super class') 
 def on_save_result(self, cycle_result):
    raise Exception('on_save_result must be implemented by super class')

 

 def clear_results(self):
   self.list_result = []

 def __init__(self, script_id):    

     super().__init__()
      
     self.driver = None
     self.list_result = []
     self.script_id = script_id
     self.flag_cancelar = 0

     self.start_config = self.get_start_config(self.script_id)
     self.script_config = self.get_script_config(self.script_id)
     self.lista_steps = self.get_steps()

     
     if (len(self.lista_steps) == 0):
       self.log('Steps not found on script {}'.format(str(self.script_id)))
       return
     
     #orderna lista pelo sort_number
     self.lista_steps.sort(key=lambda x: x.sort_number)


 def is_dinamic(self, attr):
    index = str(attr).find("{")
    return (index != -1) 

 
 def detect_chrome_window(self, start_config): 
   hwnd = win32gui.FindWindow(start_config.chrome_class_name, start_config.browser_title )
   if (hwnd != 0):
     return True
   else:
     return False  


 
 def get_expression(self, value, values):
    if self.is_dinamic(value):
      attribute = value[value.find("{")+1:value.find("}")]
      attrib_value = values[attribute]
      value = str(value).replace(attribute, '')
      return str(value).format(attrib_value)
    else: 
      return value

 def get_text_to_type(self, value, values):
    if self.is_dinamic(value):
      attribute = re.sub(r'[^\w]', '', value) 
      return values[attribute]
    else: 
      return value

 def get_element_from_other_step(self, steps, step_id):
    step = Step()
    step = next((x for x in steps if x.step_id == step_id), None)
    return step.resulted_element

 
 def must_skip(self, step, steps_to_skip ):
   if (step.skip == "1"): 
      return True   
   else:
      if (not steps_to_skip) or (steps_to_skip == 'none'):        
        return False
      else:
        steps_to_check = str(steps_to_skip).split('|')
        for step_to_check in steps_to_check:
          if (step_to_check == str(step.step_id)):
             return True

      return False       

 def find_element(self, driver, step, lista_steps, values_on_expression):
    
    expression = self.get_expression(step.expression, values_on_expression)
    
    if (step.must_wait_element == "1"):
      if (step.find_method == "name"):  
        element = WebDriverWait(driver, step.timeout_to_element ).until(EC.presence_of_element_located( (By.NAME, expression)) )
      elif (step.find_method == "id"):
        element = WebDriverWait(driver, step.timeout_to_element ).until(EC.presence_of_element_located( (By.ID, expression)) )  
      elif (step.find_method == "xpath"):
        element = WebDriverWait(driver, step.timeout_to_element ).until(EC.presence_of_element_located( (By.XPATH, expression)) )  
      elif (step.find_method == "class_name"):
        element = WebDriverWait(driver, step.timeout_to_element ).until(EC.presence_of_element_located( (By.CLASS_NAME, expression)) )  
      elif (step.find_method == "css_selector"):
        element = WebDriverWait(driver, step.timeout_to_element ).until(EC.presence_of_element_located( (By.CSS_SELECTOR, expression)) )  
      elif (step.find_method == "link_text"):              
        element = WebDriverWait(driver, step.timeout_to_element ).until(EC.presence_of_element_located( (By.LINK_TEXT, expression)) )  
      elif (step.find_method == "tag_name"):      
        element = WebDriverWait(driver, step.timeout_to_element ).until(EC.presence_of_element_located( (By.TAG_NAME, expression)) )  
      elif (step.find_method == "partial_link_text"):      
        element = WebDriverWait(driver, step.timeout_to_element ).until(EC.presence_of_element_located( (By.PARTIAL_LINK_TEXT, expression)) )   
    else:

      if (step.base_element != 'other_step'):
          base_element = driver
      else:
          base_element = self.get_element_from_other_step(lista_steps, step.element_from_step)

      if (step.find_method == "name"):  
        element = base_element.find_element_by_name(expression)
      elif (step.find_method == "id"):
        element = base_element.find_element_by_id(expression)
      elif (step.find_method == "xpath"):
        element = base_element.find_element_by_xpath(expression)
      elif (step.find_method == "class_name"):
        element = base_element.find_element_by_class_name(expression)
      elif (step.find_method == "css_selector"):
        element = base_element.find_element_by_css_selector(expression)
      elif (step.find_method == "link_text"):              
        element = base_element.find_element_by_link_text(expression)
      elif (step.find_method == "tag_name"):      
        element = base_element.find_element_by_tag_name(expression)
      elif (step.find_method == "partial_link_text"):      
        element = base_element.find_element_by_partial_link_text(expression)

    return element

 def handle_navigator_open(self):

   start_config = self.start_config

    #se for pra buscar navegador já aberto
   if (start_config.get_opened_browser == "1"):   
    
    #verifica se navegador parece já estar aberto
    browser_seems_to_be_opened = self.detect_chrome_window(start_config)
  
    #se parecer que não está aberto, abre navegador e attach no debugger
    if (not browser_seems_to_be_opened):
      self.open_browser(start_config)
      self.driver = self.attach_to_browser(start_config, False)
    else:
      self.driver = self.attach_to_browser(start_config, True)
    
    if (not  self.driver):
      self.open_browser(start_config)
      self.driver = self.attach_to_browser(start_config, False)

   else:
    #abre novo navegador
    self.open_browser(start_config)
    self.driver = self.attach_to_browser(start_config, False)

   
 def run_steps(self, values, values_on_expression, step_id, steps_to_skip ):
   
     lista_steps = self.lista_steps
     script_config = self.script_config
     start_config = self.start_config      
     
     chegou_fim = False
     
     #se navegador não estiver aberto, abre o mesmo 
     if (not self.driver):
       self.handle_navigator_open()
     
     driver = self.driver

     while (not chegou_fim):

         #print('flag cancelar no while principal do run_steps: ' + str(self.flag_cancelar)    )
         if (self.flag_cancelar == 1) :
            return
      
         #pega step pelo step id
         step = next((x for x in lista_steps if x.step_id == step_id), None)
        

         try:
            
            if (not self.must_skip(step, steps_to_skip)):

               #message before
               self.log(step.log_message_before)

               
               if (step.wait_manual_action == "0"):
                #find element
                element = self.find_element(driver, step, lista_steps, values_on_expression)
               else:

                #para esperar por ação manual, 
                #faz loop até quando determinado elemento for encontrado na tela
                #quando não for mais encontrado, significa que houve uma ação manual na tela
                while (True):
                  
                  #print('flag cancelar no while true do login: ' + str(self.flag_cancelar)) 
                  if (self.flag_cancelar == 1):
                      return

                  #show waiting message
                  self.log(step.manual_action_message)
                  time.sleep(3)
                  element = self.find_element(driver, step, lista_steps, values)
                  

               #salva elemento resultante
               step.resulted_element = element
               
               #action
               if (step.action == "click"):
                  element.click()  

               elif (step.action == "type"):
                  element.clear()
                  element.send_keys(Keys.BACKSPACE)
                  element.send_keys(Keys.BACKSPACE)
                  element.send_keys(Keys.BACKSPACE)
                  element.send_keys(self.get_text_to_type(step.text_to_type, values)) 

               elif (step.action == "show"):   
                  
                  message = str(element.text).partition('\n')[0]

                  if (step.error_message_finder == "1"):
                    step.resulted_error_message = message
                    step.success = False

                  if (step.success_message_finder == "1"):
                    step.resulted_success_message = message
                    step.success = True

                  self.log('Step {} - Result: {}'.format(step.id_tela, message))  
                  
               #message after
               self.log(step.log_message_after)

               #se deve salvar resultado do ciclo, grava o resultado
               save_result = (step.save_result == '1' )
               if (save_result):                 
                  result = CycleResult()  
                  result.value = self.get_id(values)
                  result.value_to_show = self.get_id_to_show(values)
                  result.success = step.success
                  result.message = step.resulted_success_message or step.resulted_error_message
                  self.on_save_result(result)
                  self.list_result.append(result)   

            else:
               #skipped step
               self.log('Step {} Skipped'.format(step.id_tela))   
            
            success = True

         except Exception as err:
            if (step.show_error_log == "1"):
              if (not err.message):                
                self.log('Step {} - Error: {}'.format(step.id_tela,repr(err)))
              else:   
                self.log('Step {} - Error: {}'.format(step.id_tela,err))
            success = False
         finally:
            
            #print('flag cancelar no finally: ' + str(self.flag_cancelar) )
            if (self.flag_cancelar == 1):
              return

            
            self.log('Step {} Completed'.format(step.id_tela))
            
            if (step.minimize_after_step == "1"):
              driver.minimize_window()
              if (script_config.minimize_message):
                self.log(script_config.minimize_message)

            if (step.maximize_after_step == "1"):
              driver.maximize_window()
            

            chegou_fim = (step.is_end_step == '1' )
           
            #se foi bem sucedido e tem um step seguinte identificado
            if ((step.on_success_goto != 0) & success):
              
              if (step.refresh_on_success == "1"):
                self.refresh_browser(driver, start_config)
               
              step_id = step.on_success_goto 
              steps_to_skip = step.steps_to_skip_on_next_run

            elif ((step.on_error_goto != 0) & (not success) ):
              
              if (step.refresh_on_error == "1"):
                self.refresh_browser(driver, start_config)    
                

              #se deu erro e tem um step seguinte identificado
              step_id = step.on_error_goto  
              steps_to_skip = step.steps_to_skip_on_next_run
            else:
                #se nao tem um step seguinte identificado e foi bem sucedido, segue pro proximo step da lista  
                if (success):  
                   index = lista_steps.index(step)
                   index += 1   
                   step_id = lista_steps[index].step_id

                   #limpa steps_to_skip  apenas se for igual a constant.RESET_SKIP_INDICATOR ('none')
                   if (not steps_to_skip) :
                     steps_to_skip = step.steps_to_skip_on_next_run
                   else:  
                     if ( step.steps_to_skip_on_next_run == constant.RESET_SKIP_INDICATOR ):
                       steps_to_skip = step.steps_to_skip_on_next_run

            if (step.wait_next > 0):
              self.log(script_config.wait_message_between_steps.format(str(step.wait_next)))
              time.sleep(step.wait_next)

     return { "step_id": step_id, "steps_to_skip_on_next_run" : steps_to_skip }       


 def get_steps(self):
   steps = busca_steps(self.script_id)
   lista_steps = [] 
   
   for data in steps:
      step = dict(data)
      model = self.row_to_model(Step(), step)
      lista_steps.append(model)

   return lista_steps     

 def get_start_config(self, script_id):   
   start_config = busca_start_config(script_id)
   start_config = dict(start_config)
   start_config = self.row_to_model(Start_Config(), start_config)
   return start_config     

 
 def get_script_config(self, script_id):
   script_config = busca_script(script_id)
   script_config = dict(script_config)
   script_config = self.row_to_model(Script(), script_config)
   return script_config 

 
 def row_to_model(self, model_instance, row):    
    for col_name in row:
       model_instance.__setattr__(col_name, row[col_name])
             
    return model_instance

 def refresh_browser(self, driver, start_config):   
   driver.refresh()
   if ( (start_config.wait_after_refresh) & (start_config.wait_after_refresh > 0)):
    time.sleep(start_config.wait_after_refresh)


 def attach_to_browser(self, start_config, look_for_opened):

  cont = 1
  found = False
  
  while (not found):
    self.log(str(cont) + '...' + start_config.attempt_attach_message)
    
    try:
     chrome_options =  Options()
     chrome_options.add_experimental_option("debuggerAddress", start_config.debugger_host + ':' + start_config.debugger_port)
     driver = webdriver.Chrome(start_config.driver_name, options=chrome_options)
   
     found = True
     
    except Exception as err:
     print(err)
     found = False 
     time.sleep(start_config.delay_between_attempt)

     #se estiver procurando uma janela já aberta, e falhou, não vai ficar tentando
     #vai sair do loop indicar ao caller que não foi possivel encontrar uma janela ativa com o debugger
     if (look_for_opened): 
       return None 
       
    
    cont+=1
    
    
  return driver 
 
 def quit_browser(self):
   self.driver.quit()

 def open_browser(self, start_config):
   #CHROME = start_config.browser_path
   
   if (start_config.close_opened_browser_windows == "1"):
     os.system(start_config.browser_kill_cmd)

   os.system(start_config.browser_start_cmd + ' "' + start_config.initial_url +  '" ' + start_config.browser_args)
 

