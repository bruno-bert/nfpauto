from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QListWidgetItem
import ui_dialog_postar
import messages
import constant
from database import busca_chaves_banco

class Posting:
 def __init__(self):
     
     self.dialog_postar = ui_dialog_postar.Ui_Dialog()     
     self.DialogPostar = QtWidgets.QDialog()
     self.dialog_postar.setupUi(self.DialogPostar)
     self.DialogPostar.setModal(True)

     self.dialog_postar.btn_iniciar_postagem.clicked.connect(self.inicia_postagem)
     self.dialog_postar.btn_fechar.clicked.connect(self.DialogPostar.reject)

     self.messages = messages.Messages()

 def carrega_lista_chaves(self, rows):

  self.dialog_postar.lista_notas.setRowCount(0) 

  if (rows):
    for row_num, row_data in enumerate(rows):
        row = dict(row_data)
        self.dialog_postar.lista_notas.insertRow(row_num)
        self.dialog_postar.lista_notas.setItem(row_num, 0, QTableWidgetItem(str(row['id']))) 
        self.dialog_postar.lista_notas.setItem(row_num, 1, QTableWidgetItem(row['chave']))
        self.dialog_postar.lista_notas.setItem(row_num, 2, QTableWidgetItem(row['status']))
        self.dialog_postar.lista_notas.setItem(row_num, 3, QTableWidgetItem(row['message']))

 def cria_tabela_notas(self):
    self.dialog_postar.lista_notas.setColumnCount(4)
    self.dialog_postar.lista_notas.setRowCount(1)
    self.dialog_postar.lista_notas.setHorizontalHeaderLabels(
                                      ['ID', 'Chave', 
                                       'Status', 
                                      'Mensagem'])       
 def mostra_posting(self):   
     
     self.cria_tabela_notas()
     rows = busca_chaves_banco()
     self.carrega_lista_chaves(rows)
     
     if  (self.DialogPostar.exec_()):
        return True
     else:
        return False 

     
 def inicia_postagem(self):
   print('nao implementado') 