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

 def get_text_to_type(self, item, values):
    return "11111"

 def get_element_from_other_step(self, steps, step_id):
    step = Step()
    step = next((x for x in steps if x.step_id == step_id), None)
    return step.resulted_element

 def start(self):
   driver = None #self.open_browser()
   lista_steps = self.get_steps()
   index = 0
   values = None


   #filtra lista retirando os steps de checagem de sessao 
   lista_steps_sem_timeout = list(filter(lambda x: x.is_check_session_timeout == '0', lista_steps)) 

   #busca as steps de checagem de timeout e inclui em lista separada
   lista_steps_timeout = list(filter(lambda x: x.is_check_session_timeout == '1', lista_steps))  

   #orderna lista pelo sort_number
   lista_steps_sem_timeout.sort(key=lambda x: x.sort_number)
   lista_steps_timeout.sort(key=lambda x: x.sort_number)
    
   
   
   while (index <= lista_steps.count - 1):
      step = Step()      
      step = lista_steps_sem_timeout[index]
    
      try:
         
        if (not step.skip):

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
         
         #action
         if (step.action == "click"):
            element.click()  

         elif (step.action == "type"):
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(self.get_text_to_type(step.text_to_type, values)) 

         #elif (step.action == "find"):            
         #elif (step.action == "show"):    
         
         #message after
         self.log(step.log_message_after)

        else:
         #skipped step
         self.log(print('pulou step {} '.format(step.step_id)))   

      except ValueError as err:
         self.log(print('step {} - erro: {}'.format(step.step_id, err)))  
      finally:
         self.log(print('step {} concluída'.format(step.step_id)))  
         index += 1  
        

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

  
   
   
     
      

   
      #step 4 
   STEP4 = False
   if (STEP4):    
    try:
        self.log('procurando elemento mensagem popup')
        element_popup = WebDriverWait(driver, 5 ).until(EC.presence_of_element_located( (By.XPATH, "//div[@aria-labelledby='ui-dialog-title-divPerguntaMaster']")) )
        self.log('achou element janela popup')
        self.log('procurando elemento mensagem popup botao click sim')
        if (element_popup):
         element = element_popup.find_element_by_xpath(".//span[contains(text(), 'Sim')]")
         self.log('achou elemento mensagem popup botao click sim')
         if (element):
          element.click()
        self.log('clicou elemento mensagem popup botao click sim')
    except ValueError as strerr:
        self.log(strerr) 
    finally:
        self.log('step 4 concluida!!')   


      #step 5 
   try:
      self.log('procurando elemento chave de acesso')
      div_dados = WebDriverWait(driver, 3 ).until(EC.presence_of_element_located( (By.ID, "divDados")) )
      div_dados_com_chave = div_dados.find_element_by_id("divDocComChave")
      #div_dados_sem_chave = div_dados.find_element_by_id("divDocSemChave") 

      input_chave = div_dados_com_chave.find_element_by_xpath("//span[contains(text(), 'Chave-de-acesso')]/following-sibling::input")

      self.log('achou element chave de acesso')
      self.log('preenchendo element com chave de acesso')
      input_chave.send_keys(Keys.BACKSPACE)
      input_chave.send_keys('3211-1111-1111-1111-1111-1111-1111-1113-3333-3333-3333')
      self.log('chave de acesso preenchida') 
   except ValueError as strerr:
      self.log(strerr) 
   finally:
      self.log('step 5 concluida!!')    

   
   #step 6 
   try:
      input_cnpj = WebDriverWait(driver, 1 ).until(EC.presence_of_element_located( (By.NAME, "ctl00$ConteudoPagina$entiFilantropica$txtCNPJEntidade")) )
      input_cnpj.send_keys(Keys.BACKSPACE)
      input_cnpj.send_keys('01.146.603/0001-69')       
   except ValueError as strerr:
      self.log(strerr) 
   finally:
      self.log('step 6 concluida!!')    

      
    #step 7 
   try:
      btn_buscar = WebDriverWait(driver, 1 ).until(EC.presence_of_element_located( (By.NAME, "ctl00$ConteudoPagina$entiFilantropica$btnBuscar")) )
      btn_buscar.click()
   except ValueError as strerr:
      self.log(strerr) 
   finally:
      self.log('step 7 concluida!!')    


    #step 8 
   try:
      input_selecao_entidade = WebDriverWait(driver, 10 ).until(EC.presence_of_element_located( (By.NAME, "ctl00$ConteudoPagina$entiFilantropica$gdvConsultaEntidades$ctl02$rdbSelecao")) )
      input_selecao_entidade.click()
   except ValueError as strerr:
      self.log(strerr) 
   finally:
      self.log('step 8 concluida!!')    


    
     #step 9 
   try:
      btn_salvar = WebDriverWait(driver, 1 ).until(EC.presence_of_element_located( (By.NAME, "ctl00$ConteudoPagina$btnSalvarNota")) )
      btn_salvar.click()
   except ValueError as strerr:
      self.log(strerr) 
   finally:
      self.log('step 9 concluida!!')   

    
     #step 10
     # se deu erro - vai mostrar tela de erro 
   STEP10 = True
   tela_erro_encontrada = False
   if (STEP10):    
    try:
        element_erro = WebDriverWait(driver, 5 ).until(EC.presence_of_element_located( (By.XPATH, "//div[@aria-labelledby='ui-dialog-title-divErroMaster']")) )
        tela_erro_encontrada = True
        erro_mensagem = element_erro.find_element_by_id("lblErroMaster")
        self.log(erro_mensagem.text) 
        btn_Ok = element_erro.find_element_by_xpath(".//span[contains(text(), 'Ok')]")
        btn_Ok.click()
            
    except ValueError as strerr:
        self.log(strerr) 
        tela_erro_encontrada = False
    finally:
        self.log('step 10 concluida!!')     

    
     #step 11
     # se não deu erro - vai mostrar tela de sucesso 
    if (not tela_erro_encontrada):
      try:
        element_success = WebDriverWait(driver, 5 ).until(EC.presence_of_element_located( (By.XPATH, "//div[@aria-labelledby='ui-dialog-title-divPerguntaMaster']")) )
        tela_success_encontrada = True
        success_mensagem = element_success.find_element_by_id("lblPerguntaMaster")
        self.log(success_mensagem.text) 
        btn_Nao = element_success.find_element_by_xpath(".//span[contains(text(), 'Não')]")
        btn_Nao.click()
            
      except ValueError as strerr:
        self.log(strerr) 
        tela_success_encontrada = False
      finally:
        self.log('step 11 concluida!!')     
     

     #mensagemBemVindo

 def log(self, message):
   print(message) 



if __name__ == "__main__":
  service = NotaPaulista_Posting()
  service.start()