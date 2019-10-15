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

class NotaPaulista_Posting:
 def __init__(self):
     self.messages = nfp_messages.Messages()

 def is_dinamic(self, attr):
    index = str(attr).find("{")
    return (index != -1) 

 def get_text_to_type(self, attribute, values):
    if self.is_dinamic(attribute):
     return values[attribute]

 def get_element_from_other_step(self, steps, step_id):
    step = Step()
    step = next((x for x in steps if x.step_id == step_id), None)
    return step.resulted_element

 def get_chaves(self):
    return ['11111','22222','33333']
 
 def get_cnpj(self):
    return '01.146.603/0001-69'
 
 def must_skip(self, step_id,  skip, steps_to_skip ):
   if (skip): 
      return True
   else:
      if (not steps_to_skip) or (steps_to_skip == 'none'):
         return True
      else:
        steps_to_check = str(steps_to_skip).split('|')
        for step_to_check in steps_to_check:
          if (step_to_check == step_id):
             return True

      return False       


 def start(self):
   driver = self.open_browser()
   lista_steps = self.get_steps()
   values = None
   chaves = self.get_chaves()
   cnpj = self.get_cnpj()

   #filtra lista retirando os steps de checagem de sessao 
   lista_steps_sem_timeout = list(filter(lambda x: x.is_check_session_timeout == '0', lista_steps)) 

   #busca as steps de checagem de timeout e inclui em lista separada
   lista_steps_timeout = list(filter(lambda x: x.is_check_session_timeout == '1', lista_steps))  

   #orderna lista pelo sort_number
   lista_steps_sem_timeout.sort(key=lambda x: x.sort_number)
   lista_steps_timeout.sort(key=lambda x: x.sort_number)

   #pega primeira step 
   index = 0
   step = Step()      
   step = lista_steps_sem_timeout[index]
   step_id = step.step_id
   chegou_fim = False
   
   for chave in chaves:
    
    values = { chave: chave, cnpj: cnpj}

    while (not chegou_fim):
      
      #pega step pelo step id
      step = next((x for x in lista_steps_sem_timeout if x.step_id == step_id), None)

      try:
         
        if (not self.must_skip(step.step_id, step.skip, steps_to_skip)):

         #message before
         self.log(step.log_message_before)

         #find
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
          
         #salva elemento resultante
         step.resulted_element = element
         
         #action
         if (step.action == "click"):
            element.click()  

         elif (step.action == "type"):
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(self.get_text_to_type(step.text_to_type, values)) 

         elif (step.action == "show"):   

            if (step.error_message_finder == "1"):
             step.resulted_error_message = element.text
             step.success = False

            if (step.success_message_finder == "1"):
             step.resulted_success_message = element.text
             step.success = True
             
            
            self.log('step {} - resultado: {}'.format(step.step_id, element.text))
            
         #elif (step.action == "find"):            
         #message after
         self.log(step.log_message_after)

        else:
         #skipped step
         self.log('pulou step {} '.format(step.step_id))   
        
        success = True

      except ValueError as err:
         self.log('step {} - erro: {}'.format(step.step_id, err))
         success = False
      finally:
         self.log('step {} concluída'.format(step.step_id))

         if ((step.on_success_goto != 0) & success):
          step_id = step.on_success_goto 
          steps_to_skip = step.steps_to_skip_on_next_run   
         elif ((step.on_error_goto != 0) & (not success) ):
          step_id = step.on_error_goto  
          steps_to_skip = step.steps_to_skip_on_next_run   
         else:
          index = lista_steps_sem_timeout.index(step)
          index += 1   
          step_id = lista_steps_sem_timeout[index]
          steps_to_skip = step.steps_to_skip_on_next_run     

         chegou_fim = step.is_end_step

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
   

   try:
     chrome_options =  Options()
     chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
     driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
     found = True
   except:
     found = False 

   if (not found):  
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