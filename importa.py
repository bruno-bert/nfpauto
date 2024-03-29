import messages
import constant
import os.path
from database import busca_config_arquivo, busca_config_arquivo_padrao
from PyQt5.QtWidgets import QMessageBox
import csv
from xml.dom.minidom import parse

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
 
 def importar_dir_xml(self, path):
   result = ImportResult()
   list_result = [] 
   
   
   files = []
   # r=root, d=directories, f = files
   for r, d, f in os.walk(path):
      for file in f:
          if '.xml' in file:
              files.append(os.path.join(r, file))

   for f in files:
     try:
      doc = parse(f)
      elem = doc.getElementsByTagName("chNFe")
      for e in elem:
         list_result.append(e.childNodes[0].data)
     except:
       continue

   result.data = list_result
   result.status = 0
   result.err =  None
   result.success = True 

   return result

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
   delim = config['delimitador']
   header = config['header']
   coluna = int(config['coluna'])

   with open(file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=delim)
    
    for index, row in enumerate(csv_reader):

        #skip no header - caso arquivo tenha header
        if ( (header == "1") & (index == 0) ):
          continue 
        
        
        try:
          
          if (delim != ','):
            list_result.append(row[0].split(delim)[coluna])         
          else:
            list_result.append(row[coluna])  
        except:
          continue  
    

   result.data = list_result
   result.status = 0
   result.err =  None
   result.success = True  
   return result

 def importa_arquivo_excel(self, file, config):  
   import pandas as pd
   from math import isnan
   result = ImportResult()
   list_result = [] 
   header = None if (config["header"] == "0") else 0

   if (config['sheet_name']):
     data = pd.read_excel(file, sheet_name=config['sheet_name'], header=header)
   else:
     data = pd.read_excel(file, header=header)
     
   if (config['nome_coluna']):

    #df = pd.DataFrame(data, columns=[config['nome_coluna'] ] )
    df = pd.DataFrame(data)
    for index, row in df.iterrows():
     try:
      #value = row.iloc[config["coluna"]]
      value = row[config["nome_coluna"]]
      is_str = isinstance(value, str)
      if (is_str):   
         list_result.append(value)    
     except:
      continue

   else:

    df = pd.DataFrame(data)
    
     #value = df.iloc[:, config.coluna]  
    for index, row in df.iterrows():
      try: 
       value = row.iloc[config["coluna"]]
       is_str = isinstance(value, str)
       if (is_str): 
         list_result.append(value)    
      except:
       continue

    
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

          for index, data in enumerate(lines):
           
            #skip no header - caso arquivo tenha header
            if ( (config['header'] == "1") & (index == 0) ):
             continue 

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
           

     