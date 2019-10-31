from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QTableWidgetItem, QListWidgetItem
import ui_dialog_postar
import messages
import constant
from database import busca_chaves_banco
from service_posting import NFPPosting
from seleniumdb.observer import Subscriber
from database import  busca_script_padrao


class Posting(Subscriber):

#listener
 def show_log(self, message):
   self.adiciona_log_lista(message)

 #listener 
 def save_result(self, result):
   self.atualiza_status_nota(result)

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
 
 def atualiza_status_nota(self, result):
   print('atualizando status da nota')


 
 
 def inicia_postagem(self):
      
      script_id = self.get_script_id() 
      chaves = self.seleciona_chaves()
      cnpj = self.seleciona_cnpj()
      
      descricao_entidade = self.seleciona_descricao_entidade()
      
      service = NFPPosting(script_id, cnpj, descricao_entidade, chaves)
      service.register(self)
      
      service.iniciar_postagem()

 def get_script_id(self):      
      result = busca_script_padrao()
      return int(result['script_id'])

 def seleciona_chaves(self):
   chaveIndex = 1
   return [elt[chaveIndex] for elt in self.rows]
        

 def seleciona_cnpj(self):
   return '01.146.603/0001-69'

 def seleciona_descricao_entidade(self):
   return "GACC GRUPO DE ASSISTENCIA A CRIANCA COM CANCER"     

   