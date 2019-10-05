import messages
import constant
import os.path
from database import busca_config_arquivo, busca_config_arquivo_padrao

class ImportResult:
    def __init__(self):
       self.data = None
       self.err = None
       self.success = False
       self.status = 0


class ImportaArquivo:
 def __init__(self):
     
     self.messages = messages.Messages()

 def seleciona_tipo_importacao(self, file):
  result = busca_config_arquivo_padrao()
  return result['id_text']
  #return constant.IMPORTA_PADRAO

 def importar_arquivo(self, file):
   tipo = self.seleciona_tipo_importacao(file)
   config = busca_config_arquivo(tipo)
   config = dict(config)
   result = ImportResult()
   if (config['tipo'] == "txt"):
    result =  self.importa_arquivo_texto(file, config)
   elif (config['tipo'] == "csv"):
    result =  self.importa_arquivo_csv(file, config)
   elif (config['tipo'] == "excel"):
    result =  self.importa_arquivo_excel(file, config)
   
   return result

 def importa_arquivo_csv(self, file, config):  
   result = ImportResult()
   list_result = [] 
   result.data = list_result
   result.status = 0
   result.err =  None
   result.success = True  
   return result

 def importa_arquivo_excel(self, file, config):  
   result = ImportResult()
   list_result = [] 
   result.data = list_result
   result.status = 0
   result.err =  None
   result.success = True  
   return result

 def extract_value(self, data, config): 
   sep = str(data).split(config['delimitador'])
   if (sep):
     try:
       return sep[int(config['coluna'])] 
     except:
       return constant.EMPTY_STR
   else:
     return constant.EMPTY_STR

 def importa_arquivo_texto(self, file, config):  
     
     result = ImportResult()
     list_result = []

     if (os.path.exists(file)):

        try:
         f = open(file, 'r')

         with f:
          
          lines = f.readlines()
         
          for data in lines:
           data = self.extract_value(data, config)
           if (data):
             list_result.append(data.rstrip()) 
             
         
         #adiciona resultados no retorno
         result.data = list_result
         result.status = 0
         result.err =  None
         result.success = True 
         
         #fecha arquivo 
         f.close()

         return result

        except ValueError as strerr:
           result.data = None
           result.status = 0
           result.err =  strerr
           result.success = False
           return result
        finally:
         try:
           f.close()     
         except ValueError as strerr1:
           result.data = None
           result.status = 0
           result.err =  strerr1
           result.success = False
           return result
           

     