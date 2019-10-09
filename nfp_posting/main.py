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

   try:
      print('procurando elemento campo chave')
      element = WebDriverWait(driver, 200000000000 ).until(EC.presence_of_element_located( (By.NAME, "ctl00$ConteudoPagina$860b674c8ea846f4a13605d1f836f866")) )
      element.send_keys(Keys.BACKSPACE)
      element.send_keys('3211-1111-1111-1111-1111-1111-1111-1113-3333-3333-3333')
      print('achou elemento continuar')
   finally:
      print('achou!!')  

 def log(self, message):
   print(message) 



if __name__ == "__main__":
  service = NotaPaulista_Posting()
  service.start()