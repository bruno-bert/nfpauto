class Auth:
   __instance = None
   @staticmethod 
   def getInstance():
      """ Static access method. """
      if Auth.__instance == None:
         Auth()
      return Auth.__instance

      
   def __init__(self):
      """ Virtually private constructor. """
      if Auth.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Auth.__instance = self

      self.token = None 
     