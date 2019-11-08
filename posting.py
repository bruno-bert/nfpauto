from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QTableWidgetItem, QListWidgetItem
from PyQt5.QtGui import QIcon
import ui_dialog_postar
import messages
import constant
from database import busca_chaves_banco
from seleniumdb.observer import Subscriber
from database import  busca_script_padrao, busca_chaves_por_status, atualiza_status_nota, atualiza_status_message_nota
from task import Task
from datetime import datetime
from PyQt5.QtCore import  pyqtSignal, QSize
from PyQt5.Qt import Qt

class Posting(QtWidgets.QWidget):
 
 sig_cancelar = pyqtSignal(int)
  
 #signal
 def show_log(self, message):
   self.adiciona_log_lista(message)

 #signal 
 def save_result(self, result):   
   self.atualiza_status_nota_processada(result)
   
 #signal
 def init_value(self, value):
   self.destaca_chave_sendo_processada(value)  

 def setColortoRow(self, table, rowIndex, color):
    for j in range(table.columnCount()):
        table.item(rowIndex, j).setBackground(color)

 def destaca_chave_sendo_processada(self, value):

    items = self.dialog_postar.lista_notas.findItems(value, QtCore.Qt.MatchExactly)
    if ( len(items) > 0 ):
      for item in items:
        try:
         index = self.dialog_postar.lista_notas.indexFromItem(item).row()
         highlighted = QtGui.QColor(192,247,224)
         self.setColortoRow(self.dialog_postar.lista_notas,index,highlighted)
       
        except Exception as err:
         print(err) 

   
    
    
 def define_status(self, result):

   if (result.success):
     status = 2
   else:
     status = 3

   return status   
 
 
 def atualiza_lista(self, value):
    items = self.dialog_postar.lista_notas.findItems(value, QtCore.Qt.MatchExactly)
    if ( len(items) > 0 ):
      for item in items:
        #try:
        index = self.dialog_postar.lista_notas.indexFromItem(item).row()
        print('removendo linha {}'.format(str(index)))
        self.dialog_postar.lista_notas.removeRow(index)
        #except Exception as err:
        # print(err) 

 def atualiza_status_nota_processada(self, result):
     
     #atualiza status da nota no banco
     status = self.define_status(result)
     atualiza_status_message_nota(result.value, status, result.message)

     #atualiza lista no ui
     self.atualiza_lista(result.value)
    

 def applyStyles(self):
  sshFile = constant.STYLES_FILE
  #TODO - pegar style de uma classe singleton, carregada uma unica vez
  with open(sshFile,"r") as fh:
       self.DialogPostar.setStyleSheet(fh.read())      

 def __init__(self, parent):

     super().__init__()

     self.rows = None
      
     #self.DialogPostar = QtWidgets.QDialog(parent)
     self.DialogPostar = QtWidgets.QDialog()
     self.dialog_postar = ui_dialog_postar.Ui_Dialog()   
     self.dialog_postar.setupUi(self.DialogPostar)
     self.DialogPostar.setWindowFlags(self.DialogPostar.windowFlags() | Qt.WindowMinimizeButtonHint)
     
     self.applyStyles()
     
     self.dialog_postar.btn_iniciar_postagem.clicked.connect(self.trigger_postagem)
     
     self.dialog_postar.btn_limpar.clicked.connect(self.limpar_log)
     self.dialog_postar.btn_fechar.clicked.connect(self.fechar_dialog)
     
     self.model = QtGui.QStandardItemModel()
     self.dialog_postar.list_log.setModel(self.model)
 
     self.messages = messages.Messages()
     
     self.modo_parado()


 def fechar_dialog(self):
    if (self.modo_atual == 'postando'):
        self.sig_cancelar.emit(1)
        self.modo_parado() 
    self.DialogPostar.reject()
    
 
 def limpar_log(self):
    self.model.clear()
 
 def format_log(self, message):
   dt = datetime.now()
   timestamp = '{:%d/%m/%Y %H:%M:%S}'.format(dt)
   return '{} - {}'.format(timestamp, message)

 def adiciona_log_lista(self, message):
    if (message):
      message = self.format_log(message)
      item = QtGui.QStandardItem(message)
      self.model.insertRow(0, item)
    
   
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
    
    self.dialog_postar.lista_notas.hideColumn(0)

    header = self.dialog_postar.lista_notas.horizontalHeader()       
    header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
    header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
    header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
    header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
    

 def mostra_posting(self):   
     
     self.cria_tabela_notas()

     #apenas as pendentes de postagem
     self.rows = busca_chaves_por_status(1, 'ASC') 

     self.carrega_lista_chaves(self.rows)
     self.DialogPostar.exec_()
  



  


 def modo_postagem(self):
   self.dialog_postar.btn_iniciar_postagem.setText("               Parar Postagem")
   icon = QIcon("assets/icons/stop.png")
   self.dialog_postar.btn_iniciar_postagem.setIcon(icon)
   self.dialog_postar.btn_iniciar_postagem.setIconSize(QSize(64,64))
   self.modo_atual = 'postando'
   

 def modo_parado(self):
   self.dialog_postar.btn_iniciar_postagem.setText("               Iniciar Postagem")
   icon = QIcon("assets/icons/play1.png")
   self.dialog_postar.btn_iniciar_postagem.setIcon(icon)
   self.dialog_postar.btn_iniciar_postagem.setIconSize(QSize(64,64))
   self.modo_atual = 'parado'  

 def trigger_postagem(self):

    if (self.modo_atual == 'parado') :
      self.task_postagem = Task()
     
      try:
       self.sig_cancelar.connect(self.task_postagem.cancel_posting)
       self.sig_cancelar.emit(0)
      except Exception as e:
        print(repr(e)) 
      self.task_postagem.sig_log.connect(self.show_log)
      self.task_postagem.sig_result.connect(self.save_result) 
      self.task_postagem.sig_chave.connect(self.init_value) 
      self.modo_postagem()
      self.task_postagem.start()
    else:
      if (self.modo_atual == 'postando'):
         self.sig_cancelar.emit(1)
         self.modo_parado()
         
