
from PyQt5.QtGui import QColor,QBrush, QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtWidgets import QWidget, QDialog, QHeaderView, QTableWidgetItem, QListWidgetItem, QMessageBox
from PyQt5.QtCore import  pyqtSignal, QSize, Qt as QtCoreQt, QObject
from PyQt5.Qt import Qt

import messages
import constant
from database import busca_chaves_banco
from seleniumdb.observer import Subscriber
from database import  busca_script_padrao, busca_chaves_por_status, atualiza_status_nota, atualiza_status_message_nota, busca_cnpj_padrao_valor
from task import Task, Log
from datetime import datetime

#variaveis globais 
dialog_postar = None
notas = None
logs = None
cnpj_entidade = None
modo_atual = None


def seleciona_modo_atual():
  global modo_atual
  return modo_atual

#signal
def show_log( log):
  adiciona_log_lista(log.message, log.manual_action)

#signal 
def save_result( result): 
  atualiza_status_nota_processada(result)
  
#signal
def init_value( value):
  destaca_chave_sendo_processada(value)  

def setColortoRow( table, rowIndex, color):
  for j in range(table.columnCount()):
      table.item(rowIndex, j).setBackground(color)

def destaca_chave_sendo_processada( value):
  global dialog_postar
  items = dialog_postar.lista_notas.findItems(value, QtCoreQt.MatchExactly)
  if ( len(items) > 0 ):
    for item in items:
      try:
        index = dialog_postar.lista_notas.indexFromItem(item).row()
        highlighted = QColor(192,247,224)
        setColortoRow(dialog_postar.lista_notas,index,highlighted)
      
      except Exception as err:
        print(err) 

  
  
  
def define_status( result):

  if (result.success):
    status = 2
  else:
    status = 3

  return status   


def atualiza_lista( value):
  global dialog_postar
  items = dialog_postar.lista_notas.findItems(value, QtCoreQt.MatchExactly)
  if ( len(items) > 0 ):
    for item in items:
      index = dialog_postar.lista_notas.indexFromItem(item).row()
      dialog_postar.lista_notas.removeRow(index)

def atualiza_lista_tela_principal( value):
  global dialog_postar

  #atualiza tela principal apenas se esta estiver com selecao de filtro igual a "pendentes" 
  if (dialog_postar.combo_status.currentIndex() == 1):
    items = dialog_postar.tableWidget.findItems(value, QtCoreQt.MatchExactly)
    if ( len(items) > 0 ):
      for item in items:
        index = dialog_postar.tableWidget.indexFromItem(item).row()
        dialog_postar.tableWidget.removeRow(index)

def atualiza_status_nota_processada( result):
    global cnpj_entidade
    #atualiza status da nota no banco
    status = define_status(result)
    
    adiciona_log_lista("Chave {} - Atualizando status na base de dados".format(result.value), 0)
    atualiza_status_message_nota(result.value, status, result.message, cnpj_entidade)
    
    #atualiza lista no ui
    atualiza_lista(result.value)
    atualiza_lista_tela_principal(result.value)
  


def mostra_posting(ui):
  global dialog_postar, logs, cnpj_entidade
   
   #se for a primeira vez que está abrindo a tela de postagens, inicia tela
   # inicia log, inicia em modo_parado
  if (not dialog_postar):

    dialog_postar = ui
    logs = QStandardItemModel()
    dialog_postar.list_log.setModel(logs)
    modo_parado()

    #inicializa a tabela de notas disponiveis
    cria_tabela_notas()
    
    #busca entidade
    cnpj_entidade = busca_cnpj_padrao_valor()

  #apenas as pendentes de postagem
  notas = busca_chaves_por_status(1, 'ASC') 
  carrega_lista_chaves(notas)

def limpar_log():
  global logs
  logs.clear()

def format_log( message):
  dt = datetime.now()
  timestamp = '{:%d/%m/%Y %H:%M:%S}'.format(dt)
  return '{} - {}'.format(timestamp, message)

def applyStylesToElement(component, cssFile):
  with open(cssFile,"r") as fh:
    component.setStyleSheet(fh.read())   

def adiciona_log_lista( message, manual_action):
  global logs, dialog_postar

  if (message):
    message = format_log(message)
    item = QStandardItem(message)
    

    if (manual_action == 1):
      brush = QBrush ()
      brush.setColor(QColor(255,0,0))
      item.setForeground(brush)
      applyStylesToElement(dialog_postar.toolBox, constant.STYLES_FILE_TAB_ALERT)
      dialog_postar.toolBox.setItemText(dialog_postar.toolBox.indexOf(dialog_postar.page_2), "      Postagem de Notas ( " + str(message).split(" - ")[1] + " )")
      
    else:
      dialog_postar.toolBox.setItemText(dialog_postar.toolBox.indexOf(dialog_postar.page_2), "      Postagem de Notas ( Em Andamento )")
      applyStylesToElement(dialog_postar.toolBox, constant.STYLES_FILE_TAB_PROGRESS)   
       
    logs.insertRow(0, item) 
  
  
def carrega_lista_chaves(notas):
  global dialog_postar
  dialog_postar.lista_notas.setRowCount(0) 

  if (notas):
    for row_num, row_data in enumerate(notas):
        row = dict(row_data)
        dialog_postar.lista_notas.insertRow(row_num)
        dialog_postar.lista_notas.setItem(row_num, 0, QTableWidgetItem(str(row['id']))) 
        dialog_postar.lista_notas.setItem(row_num, 1, QTableWidgetItem(row['chave']))
        dialog_postar.lista_notas.setItem(row_num, 2, QTableWidgetItem(row['status']))
        dialog_postar.lista_notas.setItem(row_num, 3, QTableWidgetItem(row['message']))

def cria_tabela_notas():
  global dialog_postar
  dialog_postar.lista_notas.setColumnCount(4)
  dialog_postar.lista_notas.setRowCount(1)
  dialog_postar.lista_notas.setHorizontalHeaderLabels(
                                    ['ID', 'Chave', 
                                      'Status', 
                                    'Mensagem'])
  
  dialog_postar.lista_notas.hideColumn(0)

  header = dialog_postar.lista_notas.horizontalHeader()       
  header.setSectionResizeMode(0, QHeaderView.Stretch)
  header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
  header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
  header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
  



def modo_postagem():
  global modo_atual, dialog_postar
  dialog_postar.btn_iniciar_postagem.setText("               Parar Postagem")
  icon = QIcon("assets/icons/stop.png")
  dialog_postar.btn_iniciar_postagem.setIcon(icon)
  dialog_postar.btn_iniciar_postagem.setIconSize(QSize(32,32))
  modo_atual = 'postando'
  dialog_postar.toolBox.setItemText(dialog_postar.toolBox.indexOf(dialog_postar.page_2), "      Postagem de Notas ( Em Andamento )")
  applyStylesToElement(dialog_postar.toolBox, constant.STYLES_FILE_TAB_PROGRESS)   
  

def modo_parado():
  global modo_atual, dialog_postar
  dialog_postar.btn_iniciar_postagem.setText("               Iniciar Postagem")
  icon = QIcon("assets/icons/play1.png")
  dialog_postar.btn_iniciar_postagem.setIcon(icon)
  dialog_postar.btn_iniciar_postagem.setIconSize(QSize(32,32))
  modo_atual = 'parado'  
  dialog_postar.toolBox.setItemText(dialog_postar.toolBox.indexOf(dialog_postar.page_2), "      Postagem de Notas ( Parado )")
  applyStylesToElement(dialog_postar.toolBox, constant.STYLES_FILE_TAB_STOPPED)   


        
