import requests
import settings
import json

class LoginResult:
    def __init__(self):
       self.token = None
       self.err = None
       self.success = False

class ApiPortal:
    def __init__(self):
       self.url = settings.API_URL
       self.url_login =  self.url + settings.API_ROUTE_LOGIN
       self.url_register =  self.url + settings.API_ROUTE_REGISTER
       self.url_notas =  self.url + settings.API_ROUTE_NOTAS

    def login(self, usuario, senha):

       authObj = { "email": usuario, "password": senha  }       
       #info = json.dumps(authObj)
       #print(info)

       result = LoginResult() 

       try:
         request = requests.post(self.url_login, json=authObj)
         if (request.ok):
            data = request.json()
            result.token = data['accessToken']  
            result.err = None
            result.success = True
            return result
         else:
            result.err = request.text
            result.success = False
            result.token = None  
            return result    
       except requests.RequestException as e:
         result.err = e.strerror
         result.success = False
         result.token = None
         return result

    def register(self):
       pass 

    def busca_notas(self, token):
       pass   