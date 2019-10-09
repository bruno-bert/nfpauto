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

class NotaPaulista_Posting:
 def __init__(self):
     self.messages = nfp_messages.Messages()

 def start(self):
   self.open_browser()
  
 
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



   #step 1 
   STEP1 = False

   if (STEP1):
    try:
        print('procurando elemento aviso')
        element = WebDriverWait(driver, 200000000000 ).until(EC.presence_of_element_located( (By.NAME, "ctl00$ConteudoPagina$btnContinuar")) )
        print('achou elemento continuar - clica no botao continuar')
        element.click()  
    finally:
        print('achou!!')  

   #step 2 
   try:
      self.log('procurando elemento menu nivel 1')
      element = WebDriverWait(driver, 5 ).until(EC.presence_of_element_located( (By.XPATH, "//a[contains(text(), 'Entidades')]")) )
      self.log('clicando elemento menu nivel 1')
      element.click()
      self.log('clicou elemento menu nivel 1')
      
      
      self.log('procurando elemento menu nivel 2')
      element = WebDriverWait(driver, 5 ).until(EC.presence_of_element_located( (By.XPATH, "//a[@href='/EntidadesFilantropicas/DoacaoNotasListagem.aspx']")) )
      self.log('clicando elemento menu nivel 2')
      element.click()  
      self.log('clicou elemento menu nivel 2')

      

   except ValueError as strerr:
      self.log(strerr) 
   finally:
      self.log('step 2 concluida!!')   
    

     #step 3 
   try:
      self.log('procurando elemento nova doacao')
      element = WebDriverWait(driver, 5 ).until(EC.presence_of_element_located( (By.ID, "btnNovaDoacao")) )
      self.log('clicando elemento nova doacao')
      element.click()
      self.log('clicou elemento nova doacao')
   except ValueError as strerr:
      self.log(strerr) 
   finally:
      self.log('step 3 concluida!!')   
   
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
        btn_Ok = element_erro.find_element_by_xpath(".//span[contains(text(), 'Ok')]")
        btn_Ok.click()
            
    except ValueError as strerr:
        self.log(strerr) 
        tela_erro_encontrada = False
    finally:
        self.log('step 10 concluida!!')     



 def log(self, message):
   print(message) 



if __name__ == "__main__":
  service = NotaPaulista_Posting()
  service.start()