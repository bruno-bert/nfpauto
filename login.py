from PyQt5 import QtWidgets, QtCore
import ui_login
import messages
from database import busca_cnpj_padrao_valor

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
 
 def executa_login_servidor(self, usuario, senha, cnpj):
     return False 

 def limpa_info_login(self):
     self.dialog_login.lbl_message_login.setText("")
     self.dialog_login.txt_usuario.clear() 
     self.dialog_login.txt_password.clear() 

 def executa_login(self):
     usuario = self.dialog_login.txt_usuario.text() 
     senha = self.dialog_login.txt_password.text() 
     cnpj = busca_cnpj_padrao_valor()
     login_success = self.executa_login_servidor(usuario, senha, cnpj)

     if (login_success): 
      self.dialog_login.lbl_message_login.setText(self.messages.good_login)
      #self.DialogLogin.accept()
     else:
      self.dialog_login.lbl_message_login.setText(self.messages.bad_login)
      #self.DialogLogin.reject()
