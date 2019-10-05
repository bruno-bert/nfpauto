import messages
import constant
import os.path

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
   #todo - definir automaticamente
  return constant.IMPORTA_PADRAO

 def importar_arquivo(self, file):
   tipo = self.seleciona_tipo_importacao(file)
   result = ImportResult()

   if (tipo == "TEXT_PADRAO"): #txt sem header
    result =  self.importa_arquivo_texto(file)
   elif (tipo == "TEXT_MULT_COL"):
    result =  self.importa_arquivo_texto(file)
   elif (tipo == "TEXT_MULT_COL_HEADER"):
    result =  self.importa_arquivo_texto(file)
   elif (tipo == "CSV"):    
    result =  self.importa_arquivo_texto(file)
   elif (tipo == "CSV_HEADER"):  
    result =  self.importa_arquivo_texto(file)
   elif (tipo == "EXCEL"):
    result =  self.importa_arquivo_texto(file)
   elif (tipo == "EXCEL_HEADER"):
    result = self.importa_arquivo_texto(file)

   return result
    
 def importa_arquivo_texto(self, file):  
     
     result = ImportResult()
     list_result = []

     if (os.path.exists(file)):

        try:
         f = open(file, 'r')
         with f:
          
          data = f.readline().rstrip()            
         
          while data:
           list_result.append(data) 
           data = f.readline().rstrip()  
         
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
           

     