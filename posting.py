from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QTableWidgetItem, QListWidgetItem
import ui_dialog_postar
import messages
import constant
from database import busca_chaves_banco
from seleniumdb.observer import Subscriber
from database import  busca_script_padrao
from task import Task


class Posting(Subscriber):
 
 
 #signal
 def show_log(self, message):
   self.adiciona_log_lista(message)

 #signal 
 def save_result(self, id_nota):   
   self.atualiza_status_nota_tela(id_nota)

 def atualiza_status_nota_tela(self, id_nota):
     print('atualizando status da nota na tela {}'.format(id_nota))  

 def __init__(self):

     self.rows = None

     self.dialog_postar = ui_dialog_postar.Ui_Dialog()     
     self.DialogPostar = QtWidgets.QDialog()
     self.dialog_postar.setupUi(self.DialogPostar)
     self.DialogPostar.setModal(True)
     
     self.dialog_postar.btn_iniciar_postagem.clicked.connect(self.inicia_postagem)
     
     self.dialog_postar.btn_limpar.clicked.connect(self.limpar_log)
     self.dialog_postar.btn_fechar.clicked.connect(self.DialogPostar.reject)
     
     self.model = QtGui.QStandardItemModel()
     self.dialog_postar.list_log.setModel(self.model)
 
     self.messages = messages.Messages()

 
 def limpar_log(self):
    self.model.clear()

 def adiciona_log_lista(self, message):
    if (message):
      item = QtGui.QStandardItem(message)
      self.model.appendRow(item)
    
   
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
     self.rows = busca_chaves_banco()
     self.carrega_lista_chaves(self.rows)
     
     if  (self.DialogPostar.exec_()):
        return True
     else:
        return False 
 
 def inicia_postagem(self):
      self.task_postagem = Task()
      self.task_postagem.sig_log.connect(self.show_log)
      self.task_postagem.sig_result.connect(self.atualiza_status_nota_tela)
      self.task_postagem.start()


