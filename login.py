from PyQt5 import QtWidgets, QtCore
import ui_login
import messages
from database import busca_cnpj_padrao_valor
from auth import Auth
from api import ApiPortal, LoginResult

class Login:
 def __init__(self):
     
     self.dialog_login = ui_login.Ui_Dialog()
     
     self.DialogLogin = QtWidgets.QDialog()
     self.dialog_login = ui_login.Ui_Dialog()
     self.dialog_login.setupUi(self.DialogLogin)
     self.DialogLogin.setModal(True)

     self.dialog_login.btn_login.clicked.connect(self.executa_login)
     self.dialog_login.btn_cancel.clicked.connect(self.DialogLogin.reject)

     self.limpa_info_login()

     self.messages = messages.Messages()

 def mostra_login(self):   
      self.DialogLogin.show()
 

     
 def limpa_info_login(self):
     self.dialog_login.lbl_message_login.setText("")
     self.dialog_login.txt_usuario.clear() 
     self.dialog_login.txt_password.clear() 

 def executa_login(self):
     usuario = self.dialog_login.txt_usuario.text() 
     senha = self.dialog_login.txt_password.text() 
     #cnpj = busca_cnpj_padrao_valor()

     service = ApiPortal()
     result = LoginResult()
     result = service.login(usuario, senha)
     
     if (result.success): 
      Auth.getInstance().token = result.token
      self.DialogLogin.accept()  
     else:  
      if (result.err):
        self.dialog_login.lbl_message_login.setText(self.messages.bad_login + " - " + result.err )
      else:
        self.dialog_login.lbl_message_login.setText(self.messages.bad_login)   

     