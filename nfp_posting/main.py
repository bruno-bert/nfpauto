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

import constant
from database import busca_steps, busca_script, busca_start_config
from script import Script, Step, Start_Config
from cycle_result import CycleResult


class Selenium_Through_DB:
 def __init__(self):
     self.log('Instantiated Selenium_Through_DB Service..')

 def is_dinamic(self, attr):
    index = str(attr).find("{")
    return (index != -1) 

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

 def get_chaves(self):
    return ['11111111111111111111111111111111111111111111',
            '22222222222222222222222222222222222222222222',
            '33333333333333333333333333333333333333333333']
 
 def get_cnpj(self):
    return '01.146.603/0001-69'

 def get_descricao_entidade(self):
    return "GACC GRUPO DE ASSISTENCIA A CRIANCA COM CANCER"   
 
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
    
    expression = self.get_text_to_type(step.expression, values_on_expression)
    
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
                  
 def start(self):
   script_id = self.get_script_id()
   start_config = self.get_start_config(script_id)
   script_config = self.get_script_config(script_id)

   

   lista_steps = self.get_steps()

   if (len(lista_steps) == 0):
     self.log('Steps not found on script {}'.format(str(script_id)))
     return

   #TODO remove specific code from this class through events
   chaves = self.get_chaves()
   cnpj = self.get_cnpj()
   descricao_entidade = self.get_descricao_entidade() 

   list_result = []
  
   #orderna lista pelo sort_number
   lista_steps.sort(key=lambda x: x.sort_number)

   #pega primeira step 
   index = 0
   step = Step()      
   step = lista_steps[index]
   step_id = step.step_id
   chegou_fim = False
   steps_to_skip = None

   self.open_browser(start_config)
   driver = self.attach_to_browser(start_config)
   
   
   values_on_expression = { "descricao_entidade" : descricao_entidade}

   for chave in chaves:
      
      chegou_fim = False
      values = { "chave": chave, "cnpj": cnpj}
      

      while (not chegou_fim):
      
         #pega step pelo step id
         step = next((x for x in lista_steps if x.step_id == step_id), None)
         
         #if (step_id == 20):
         #  print('teste')

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
                  #show waiting message
                  self.log(step.manual_action_message)
                  time.sleep(5)
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
                  result.value = chave
                  result.success = step.success
                  result.message = step.resulted_success_message or step.resulted_error_message
                  list_result.append(result)   

            else:
               #skipped step
               self.log('Step {} Skipped'.format(step.id_tela))   
            
            success = True

         except Exception as err:
            if (step.show_error_log == "1"):
              self.log('Step {} - Error: {}'.format(step.id_tela, err))
            success = False
         finally:
            
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

                
   for res in list_result:
      self.log(res.value + ' - ' + str(res.success) + ' - ' + res.message)
      


 def get_steps(self):
   script_id = self.get_script_id()
   steps = busca_steps(script_id)
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

 def get_script_id(self):
   #TODO script id must come from user interface
   return 2
 
 def row_to_model(self, model_instance, row):    
    for col_name in row:
       model_instance.__setattr__(col_name, row[col_name])
             
    return model_instance

 #def refresh_browser(self, driver, start_config):
 def refresh_browser(self, driver, start_config):
   #driver.get(start_config.initial_url)
   driver.refresh()
   if ( (start_config.wait_after_refresh) & (start_config.wait_after_refresh > 0)):
    time.sleep(start_config.wait_after_refresh)


 def attach_to_browser(self, start_config):

  cont = 1
  found = False

  while (not found):
    self.log(str(cont) + '...' + start_config.attempt_attach_message)
    
    try:
     chrome_options =  Options()
     chrome_options.add_experimental_option("debuggerAddress", start_config.debugger_host + ':' + start_config.debugger_port)
     driver = webdriver.Chrome(start_config.driver_name, options=chrome_options)
     
     found = True
     
    except:
     found = False 
     time.sleep(start_config.delay_between_attempt)
    
    cont+=1
    
    
  return driver 

 def open_browser(self, start_config):
   #CHROME = start_config.browser_path
   os.system(start_config.browser_kill_cmd)
   os.system(start_config.browser_start_cmd + ' "' + start_config.initial_url +  '" ' + start_config.browser_args)
 

 def log(self, message):
   print(message) 

if __name__ == "__main__":
  service = Selenium_Through_DB()
  service.start()