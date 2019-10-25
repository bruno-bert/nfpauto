import nfp_messages
import nfp_settings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import *
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import os
import subprocess
import webbrowser
import time
from database import busca_steps
from script import Script, Step
from cycle_result import CycleResult
import re

class NotaPaulista_Posting:
 def __init__(self):
     self.messages = nfp_messages.Messages()

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

 def find_element(self, driver, step, lista_steps):

    if (step.must_wait_element == "1"):
      if (step.find_method == "name"):  
        element = WebDriverWait(driver, step.timeout_to_element ).until(EC.presence_of_element_located( (By.NAME, step.expression)) )
      elif (step.find_method == "id"):
        element = WebDriverWait(driver, step.timeout_to_element ).until(EC.presence_of_element_located( (By.ID, step.expression)) )  
      elif (step.find_method == "xpath"):
        element = WebDriverWait(driver, step.timeout_to_element ).until(EC.presence_of_element_located( (By.XPATH, step.expression)) )  
      elif (step.find_method == "class_name"):
        element = WebDriverWait(driver, step.timeout_to_element ).until(EC.presence_of_element_located( (By.CLASS_NAME, step.expression)) )  
      elif (step.find_method == "css_selector"):
        element = WebDriverWait(driver, step.timeout_to_element ).until(EC.presence_of_element_located( (By.CSS_SELECTOR, step.expression)) )  
      elif (step.find_method == "link_text"):              
        element = WebDriverWait(driver, step.timeout_to_element ).until(EC.presence_of_element_located( (By.LINK_TEXT, step.expression)) )  
      elif (step.find_method == "tag_name"):      
        element = WebDriverWait(driver, step.timeout_to_element ).until(EC.presence_of_element_located( (By.TAG_NAME, step.expression)) )  
      elif (step.find_method == "partial_link_text"):      
        element = WebDriverWait(driver, step.timeout_to_element ).until(EC.presence_of_element_located( (By.PARTIAL_LINK_TEXT, step.expression)) )   
    else:

      if (step.base_element != 'other_step'):
          base_element = driver
      else:
          base_element = self.get_element_from_other_step(lista_steps, step.element_from_step)

      if (step.find_method == "name"):  
        element = base_element.find_element_by_name(step.expression)
      elif (step.find_method == "id"):
        element = base_element.find_element_by_id(step.expression)
      elif (step.find_method == "xpath"):
        element = base_element.find_element_by_xpath(step.expression)
      elif (step.find_method == "class_name"):
        element = base_element.find_element_by_class_name(step.expression)
      elif (step.find_method == "css_selector"):
        element = base_element.find_element_by_css_selector(step.expression)
      elif (step.find_method == "link_text"):              
        element = base_element.find_element_by_link_text(step.expression)
      elif (step.find_method == "tag_name"):      
        element = base_element.find_element_by_tag_name(step.expression)
      elif (step.find_method == "partial_link_text"):      
        element = base_element.find_element_by_partial_link_text(step.expression)

    return element
                  
 def start(self):
   driver = self.open_browser()
   lista_steps = self.get_steps()
   values = None
   chaves = self.get_chaves()
   cnpj = self.get_cnpj()
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
   
   for chave in chaves:
      
      chegou_fim = False
      values = { "chave": chave, "cnpj": cnpj}

      while (not chegou_fim):
      
         #pega step pelo step id
         step = next((x for x in lista_steps if x.step_id == step_id), None)
         

         try:
            
            if (not self.must_skip(step, steps_to_skip)):

               #message before
               self.log(step.log_message_before)

               
               if (step.wait_manual_action == "0"):
                #find element
                element = self.find_element(driver, step, lista_steps)
               else:

                #para esperar por ação manual, 
                #faz loop até quando determinado elemento for encontrado na tela
                #quando não for mais encontrado, significa que houve uma ação manual na tela
                while (True):
                  #show waiting message
                  self.log(step.manual_action_message)
                  element = self.find_element(driver, step, lista_steps)
                  time.sleep(5)

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

                  self.log('step {} - resultado: {}'.format(step.id_tela, message))  
                  
               #elif (step.action == "find"):
                           
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
               self.log('pulou step {} '.format(step.id_tela))   
            
            success = True

         except Exception as err:
            if (step.show_error_log == "1"):
              self.log('step {} - erro: {}'.format(step.id_tela, err))
            success = False
         finally:
            self.log('step {} concluída'.format(step.id_tela))

            chegou_fim = (step.is_end_step == '1' )
           
            #se foi bem sucedido e tem um step seguinte identificado
            if ((step.on_success_goto != 0) & success):
                step_id = step.on_success_goto 
                steps_to_skip = step.steps_to_skip_on_next_run             
            elif ((step.on_error_goto != 0) & (not success) ):
                #se deu erro e tem um step seguinte identificado
                step_id = step.on_error_goto  
                steps_to_skip = step.steps_to_skip_on_next_run
            else:
                #se nao tem um step seguinte identificado e foi bem sucedido, segue pro proximo step da lista  
                if (success):  
                   index = lista_steps.index(step)
                   index += 1   
                   step_id = lista_steps[index].step_id

                   #limpa steps_to_skip  apenas se for igual a 'none'
                   if (not steps_to_skip) :
                     steps_to_skip = step.steps_to_skip_on_next_run
                   else:  
                     if ( step.steps_to_skip_on_next_run == 'none' ):
                       steps_to_skip = step.steps_to_skip_on_next_run

            if (step.wait_next > 0):
              self.log('Esperando {} segundos para execução do próximo passo'.format(str(step.wait_next)))
              time.sleep(step.wait_next)           

   self.log('Resultado Final')                
   for res in list_result:
      self.log(res.value + ' - ' + str(res.success))
      self.log('Mensagem: ' + res.message)
      


 def get_steps(self):
   script_id = self.get_script_id()
   steps = busca_steps(script_id)
   lista_steps = [] 
   
   for data in steps:
      step = dict(data)
      model = self.row_to_model(step)
      lista_steps.append(model)

   return lista_steps     

 def get_script_id(self):
    return 1 
 
 def row_to_model(self, row):
    model = Step()
    for col_name in row:
       model.__setattr__(col_name, row[col_name])
             
    return model

 def open_browser(self):
   
   args = ' --remote-debugging-port=9222 --user-data-dir=C:\\selenium\\AutomationProfile'
   CHROME = os.path.join('C:\\', 'Program Files (x86)', 'Google', 'Chrome', 'Application', 'chrome.exe')
   os.system('taskkill /im chrome.exe')
   os.system('start CHROME "' + nfp_settings.URL_PORTAL +  '"' + args)
   cont = 0
   self.log('delay para abertura do site')
   time.sleep(5)
   found = False
   
   while (not found):
    self.log('buscando site aberto - tentativa ' + str(cont))
    
    try:
     chrome_options =  Options()
     chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
     driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
     found = True
    except:
     found = False 
    
    cont+=1

   return driver 


 def log(self, message):
   print(message) 



if __name__ == "__main__":
  service = NotaPaulista_Posting()
  service.start()