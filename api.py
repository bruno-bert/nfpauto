import requests
import settings
import json
import constant
import messages

class ApiResult:
    def __init__(self):
       self.data = None
       self.err = None
       self.success = False
       self.status = 0

class ApiPortal:
    def __init__(self):
       self.url = settings.API_URL
       self.url_login =  self.url + settings.API_ROUTE_LOGIN
       self.url_register =  self.url + settings.API_ROUTE_REGISTER
       self.url_notas =  self.url + settings.API_ROUTE_NOTAS
       self.m = messages.Messages()  
      

    def login(self, usuario, senha):

       authObj = { "email": usuario, "password": senha  }       
       result = ApiResult() 

       try:
         request = requests.post(self.url_login, json=authObj)
         if (request.ok):
            data = request.json()
            result.data = data['accessToken']  
            result.err = None
            result.success = True
            result.status = request.status_code
            return result
         else:
            result.err = request.text
            result.success = False
            result.data = None  
            result.status = request.status_code
            return result    
       except requests.RequestException as e:
         
         if ((repr(e).find('MaxRetryError')) != -1):
           result.err =  self.m.portal_indisponivel
         else:    
           result.err = repr(e)

         result.success = False
         result.data = None       
         result.status = 500  
         return result

    def register(self):
       pass 
    
    def monta_url(self, url_basic, cnpj, estab, limit):
      url = url_basic
      hasParam = False

      if (cnpj):
         url = url +  ( ("&" + settings.API_ROUTE_FILTER_CNPJ.format(cnpj=cnpj)) if hasParam else ("?" + settings.API_ROUTE_FILTER_CNPJ.format(cnpj=cnpj)) )
         hasParam = True

      if (estab):
         url = url +  ( ("&" + settings.API_ROUTE_FILTER_ESTAB.format(estab=estab)) if hasParam else ("?" + settings.API_ROUTE_FILTER_ESTAB.format(estab=estab)) )
         hasParam = True

      if (limit):
         url = url +  ( ("&" + settings.API_ROUTE_FILTER_LIMIT.format(limit=limit)) if hasParam else ("?" + settings.API_ROUTE_FILTER_LIMIT.format(limit=limit) ))
         hasParam = True   

      return url 

    def valida_parametros_busca_notas(self, cnpj, estab, limit):
       if (limit >=constant.MIN_NOTAS & limit < constant.MAX_NOTAS):
          return True
       else:
          return False    

    def busca_notas(self, token, cnpj,  estab, limit):
       result = ApiResult() 

       if (not self.valida_parametros_busca_notas(cnpj, estab, limit)):
         result.err = self.m.invalid_param
         result.success = False
         result.data = None  
         return result    

       url = self.monta_url(self.url_notas, cnpj, estab, limit)

       try:
         request = requests.get(url, headers={'Authorization': 'Bearer ' + token})
         if (request.ok):
            result.data = request.json()
            result.err = None
            result.success = True
            result.status = request.status_code
            return result
         else:
            result.err = request.text
            result.success = False
            result.data = None  
            result.status = request.status_code
            return result    
       except requests.RequestException as e:
         if ((repr(e).find('MaxRetryError')) != -1):
           result.err =  self.m.portal_indisponivel
         else:    
           result.err = repr(e)

         result.success = False
         result.data = None       
         result.status = 500  
         return result