import requests
import settings
import messages
import app_version
import subprocess

class ApiResult:
    def __init__(self):
       self.data = None
       self.err = None
       self.success = False
       self.status = 0
       self.filename = None

class Update_Handler:
 def __init__(self):
      self.url = settings.API_UPDATE
      self.url_version = settings.API_UPDATE + '/' + settings.VERSION_FILE      
      self.m = messages.Messages()  
   

 def verifica_versao_atual(self):
      return app_version.VERSION

 def verifica_versao_nova(self):
      result = ApiResult() 

      try:
         request = requests.get(self.url_version)
         if (request.ok):
            data = request.json()
            result.data = data['version']  
            result.err = None
            result.success = True
            result.status = request.status_code
            return result
         else:
            result.err = repr(request)
            result.success = False
            result.data = None  
            result.status = request.status_code
            return result    
      except requests.RequestException as e:
         
         if ((repr(e).find('MaxRetryError')) != -1):
           result.err =  self.m.repo_update_indisponivel
         else:    
           result.err = repr(e)

         result.success = False
         result.data = None       
         result.status = 500  
         return result
 
 def get_versao_nova(self):
    return self.versao_nova

 def verifica_updates(self):

    result_versao_nova =  self.verifica_versao_nova()
    versao_atual = self.verifica_versao_atual()

    if (result_versao_nova.success):
       versao_nova = result_versao_nova.data 
       self.versao_nova = versao_nova
       if (versao_nova != versao_atual):
         print('A aplicação requer uma atualização. Versão Instalada: {} - Nova Versão: {}'.format(versao_atual, versao_nova))  
         return True
       else:
         print('A aplicação já encontra-se na versão mais atual')  
         return False
    else:
       print('Erro ao verificar novas atualizações: ' + result_versao_nova.err)
       return False     
 


 def download_update(self, version):

      result = ApiResult() 
      url = self.url + '/' + str(version) + '/' + settings.UPDATE_FILE.format(version)
      
      try:
         print('Baixando instalador da versão {}'.format(version))
         request = requests.get(url)
         if (request.ok):
            data = request.content
            result.data = data
            result.err = None
            result.success = True
            result.status = request.status_code
            result.filename = settings.UPDATE_FILE.format(version)
            return result
         else:
            result.err = repr(request)
            result.success = False
            result.data = None  
            result.status = request.status_code
            return result    
      except requests.RequestException as e:
         
         if ((repr(e).find('MaxRetryError')) != -1):
           result.err =  self.m.repo_update_indisponivel
         else:    
           result.err = repr(e)

         result.success = False
         result.data = None       
         result.status = 500  
         return result    
