import nfp_messages
import nfp_settings
from selenium import webdriver

class NotaPaulista_Posting:
 def __init__(self):
     self.messages = nfp_messages.Messages()

 def start(self):
   self.open_browser()

 def open_browser(self):
   driver = webdriver.Chrome('chromedriver.exe')
   self.log('abrindo site')
   driver.get(nfp_settings.URL_PORTAL)
   self.log('aguardando ação no site - fazer login')

 def log(self, message):
   print(message)  


if __name__ == "__main__":
  service = NotaPaulista_Posting()
  service.start()