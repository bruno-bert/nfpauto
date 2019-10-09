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

        #element.send_keys(Keys.BACKSPACE)
        #element.send_keys('3211-1111-1111-1111-1111-1111-1111-1113-3333-3333-3333')
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
   try:
      self.log('procurando elemento mensagem popup')
      element_popup = WebDriverWait(driver, 5 ).until(EC.presence_of_element_located( (By.XPATH, "//div[@aria-labelledby='ui-dialog-title-divPerguntaMaster']")) )
      self.log('achou element janela popup')
      self.log('procurando elemento mensagem popup botao click sim')
      element = element_popup.find_element_by_xpath(".//span[contains(text(), 'Sim')]")
      self.log('achou elemento mensagem popup botao click sim')
      element.click()
      self.log('clicou elemento mensagem popup botao click sim')
   except ValueError as strerr:
      self.log(strerr) 
   finally:
      self.log('step 4 concluida!!')   
   


 def log(self, message):
   print(message) 



if __name__ == "__main__":
  service = NotaPaulista_Posting()
  service.start()