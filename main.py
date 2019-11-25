
#external libs - PyQt5 - UI Libs
from PyQt5.QtCore import Qt, QSize, pyqtSignal
from PyQt5.QtGui import QIntValidator, QColor, QPixmap, QIcon, QCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog, QHeaderView, QTableWidget, QTableWidgetItem, QListWidgetItem, QPlainTextEdit

#other external libs
from bradocs4py.chaveacessonfe import ValidadorChaveAcessoNFe  
from bradocs4py.cnpj import  ValidadorCnpj 
from bradocs4py.cpf import  ValidadorCpf 
from playsound import playsound


from update_checker import Update_Handler
import app_version
import dbutil
import feature_flags
from task_video import TaskVideo


#native libs
import sqlite3
import re
from datetime import date, datetime, timedelta
from calendar import monthrange
import dateutil.relativedelta
import os.path
import subprocess
from sys import argv, exit


#internal modules
import constant
from nota import Nota
from messages import Messages
from login import Login
from database import *
from auth import Auth 
from util import Util, VideoStatus

#ui - internal modules
import ui_list
import ui_cnpj_dialog
import ui_cnpj_padrao_dialog
import ui_stats

from api import ApiPortal, ApiResult

from page_posting import *



def combo_status_changed(index):
   status = int(ui.combo_status.currentText().split(' - ')[0])
   if (status == 0):
    rows = busca_chaves_banco() 
   else: 
    rows = busca_chaves_por_status(status)
   carrega_lista_chaves(rows)

def carrega_lista_status(rows):
   ui.combo_status.clear()
   ui.combo_status.addItem('0 - Todas as Notas')
   for row_data in rows:
     row = dict(row_data)
     ui.combo_status.addItem(str(row['codigo']) + ' - ' + row['descricao'])
   ui.combo_status.setCurrentIndex(1)
   ui.combo_status.currentIndexChanged.connect(combo_status_changed)
   


def carrega_lista_empresas(rows):

 dialog.lista_empresas.setRowCount(0) 
 
 if (rows):
    for row_num, row_data in enumerate(rows):
        row = dict(row_data)
        dialog.lista_empresas.insertRow(row_num)
        dialog.lista_empresas.setItem(row_num, 0, QTableWidgetItem(str(row['id']))) 
        dialog.lista_empresas.setItem(row_num, 1, QTableWidgetItem(row['empresa']))
        dialog.lista_empresas.setItem(row_num, 2, QTableWidgetItem(row['cnpj']))
        dialog.lista_empresas.setItem(row_num, 3, QTableWidgetItem(row['uf']))
        dialog.lista_empresas.setItem(row_num, 4, QTableWidgetItem(row['modelo']))
        dialog.lista_empresas.setItem(row_num, 5, QTableWidgetItem(row['serie']))  
        lista_cnpj.append(row['cnpj'])
    dialog.lista_empresas.setFocus()
    dialog.lista_empresas.selectRow(0)

    header = dialog.lista_empresas.horizontalHeader()       
    header.setSectionResizeMode(0, QHeaderView.Stretch)
    header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
    header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
    header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
    header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
    header.setSectionResizeMode(5, QHeaderView.ResizeToContents)
   


def resizeColumns(table, cols):
   header = table.horizontalHeader()       
   header.setSectionResizeMode(0, QHeaderView.Stretch)
   current_col = 1
   while (current_col < cols-1):
    header.setSectionResizeMode(current_col, QHeaderView.ResizeToContents)
    current_col+=1

def carrega_lista_chaves(rows):

    ui.tableWidget.setRowCount(0)
    lista_chaves.clear()
    atualiza_titulo_total()
    

    if (rows):
        for row_num, row_data in enumerate(rows):
            row = dict(row_data)
            ui.tableWidget.insertRow(row_num)
            ui.tableWidget.setItem(row_num, 0, QTableWidgetItem(str(row['id']))) 
            ui.tableWidget.setItem(row_num, 1, QTableWidgetItem(row['chave']))
            ui.tableWidget.setItem(row_num, 2, QTableWidgetItem(row['cnpj']))
            ui.tableWidget.setItem(row_num, 3, QTableWidgetItem(row['data']))
            ui.tableWidget.setItem(row_num, 4, QTableWidgetItem(row['status']))
            ui.tableWidget.setItem(row_num, 5, QTableWidgetItem(row['uf']))
            ui.tableWidget.setItem(row_num, 6, QTableWidgetItem(row['numero']))
            ui.tableWidget.setItem(row_num, 7, QTableWidgetItem(row['codigo']))
            ui.tableWidget.setItem(row_num, 8, QTableWidgetItem(row['modelo']))
            ui.tableWidget.setItem(row_num, 9, QTableWidgetItem(row['serie']))
            ui.tableWidget.setItem(row_num, 10, QTableWidgetItem(row['tipo_emissao']))
            ui.tableWidget.setItem(row_num, 11, QTableWidgetItem(row['message']))

           
            datetime_object = datetime.strptime(row['datahora'], '%Y-%m-%d %H:%M:%S')
            ui.tableWidget.setItem(row_num, 12, QTableWidgetItem(datetime_object.strftime('%d-%m-%Y %H:%M:%S')))
            
            if (row['datapostagem']):
              datetime_object = datetime.strptime(row['datapostagem'], '%Y-%m-%d %H:%M:%S')
              ui.tableWidget.setItem(row_num, 13, QTableWidgetItem(datetime_object.strftime('%d-%m-%Y %H:%M:%S')))

        
            lista_chaves.append(row['chave'])

    resizeColumns(ui.tableWidget, ui.tableWidget.columnCount())
        

def carrega_lista_chaves_total(rows):

    if (rows):
        for row_num, row_data in enumerate(rows):
            row = dict(row_data)
            lista_chaves.append(row['chave'])



def cria_tabela_notas():
    ui.tableWidget.setColumnCount(14)
    ui.tableWidget.setRowCount(1)
    ui.tableWidget.hideColumn(0) #esconde coluna de id
    ui.tableWidget.hideColumn(10) #esconde coluna de tipo_emissao

    
    ui.tableWidget.setHorizontalHeaderLabels(
                                      ['ID', 'Chave', 
                                       'CNPJ', 
                                       'Data', 'Status', 
                                       'UF', 'Numero', 
                                       'Codigo', 'Modelo', 
                                       'Serie', 'Tipo Emissao', 'Mensagem','Data Inclusão','Data Postagem'])                                       

def cria_tabela_empresas():
    dialog.lista_empresas.setColumnCount(6)
    dialog.lista_empresas.setRowCount(1)
    dialog.lista_empresas.hideColumn(0)
    dialog.lista_empresas.setHorizontalHeaderLabels(
                                      ['ID', 
                                       'Empresa', 
                                       'CNPJ',
                                       'UF', 'Modelo', 
                                       'Serie'])

    


def limpa_campo_chave():
    ui.txtChave.setPlainText(constant.EMPTY_STR)  
    ui.txtChave_2.setPlainText(constant.EMPTY_STR)   
    ui.txtChave_3.setPlainText(constant.EMPTY_STR)   

def separa_campos_pela_chave(chave):
    new_nota = Nota()
    new_nota.chave = chave

    try:
      new_nota.uf = chave[0:2]
      new_nota.data = chave[2:6]
      new_nota.cnpj = chave[6:20]
      new_nota.modelo = chave[20:22]
      new_nota.serie = chave[22:25]
      new_nota.numero = chave[25:34]
      new_nota.tipo_emissao = chave[34:35]
      new_nota.codigo = chave[35:43]
      new_nota.digito = chave[43:44]
    except:
      print(m.erro_separacao)
  
    return new_nota


def adiciona_empresas_na_lista(new_nota):

    dialog.lista_empresas.insertRow(0)
    dialog.lista_empresas.setItem(0, 0, QTableWidgetItem("") )
    dialog.lista_empresas.setItem(0, 1, QTableWidgetItem("") )
    dialog.lista_empresas.setItem(0, 2, QTableWidgetItem(new_nota.cnpj) )    
    dialog.lista_empresas.setItem(0, 3, QTableWidgetItem(new_nota.uf) )
    dialog.lista_empresas.setItem(0, 4, QTableWidgetItem(new_nota.modelo) )
    dialog.lista_empresas.setItem(0, 5, QTableWidgetItem(new_nota.serie) )
    lista_cnpj.append(new_nota.cnpj)

def setColortoRow(table, rowIndex, color):
    for j in range(ui.tableWidget.columnCount() -1):
        ui.tableWidget.item(rowIndex, j).setBackground(color)

def adiciona_chave_na_lista(new_nota, expirada):
    
    white = QColor(255,255,255)
    highlighted = QColor(192,247,224)

    ui.tableWidget.insertRow(0)
    ui.tableWidget.setItem(0, 0, QTableWidgetItem("") )
    ui.tableWidget.setItem(0, 1, QTableWidgetItem(new_nota.chave) )
    ui.tableWidget.setItem(0, 2, QTableWidgetItem(new_nota.cnpj) )
    ui.tableWidget.setItem(0, 3, QTableWidgetItem(new_nota.data) )
    ui.tableWidget.setItem(0, 4, QTableWidgetItem(str(constant.DEFAULT_STATUS)) )
    ui.tableWidget.setItem(0, 5, QTableWidgetItem(new_nota.uf) )
    ui.tableWidget.setItem(0, 6, QTableWidgetItem(new_nota.numero) )
    ui.tableWidget.setItem(0, 7, QTableWidgetItem(new_nota.codigo) )
    ui.tableWidget.setItem(0, 8, QTableWidgetItem(new_nota.modelo) )
    ui.tableWidget.setItem(0, 9, QTableWidgetItem(new_nota.serie) )
    ui.tableWidget.setItem(0, 10, QTableWidgetItem(new_nota.tipo_emissao) )
    ui.tableWidget.setItem(0, 11, QTableWidgetItem(m.aguardando_postagem if not expirada else m.data_expirada_doacao ) )
    ui.tableWidget.setItem(0, 12, QTableWidgetItem(datetime.now().strftime('%d-%m-%Y %H:%M:%S')))

   
    setColortoRow(ui.tableWidget,0,highlighted)

    if( ui.tableWidget.rowCount() > 1):
      setColortoRow(ui.tableWidget,1,white)
    


    lista_chaves.append(new_nota.chave)

def valida_chave_pelo_digito(chave):
  has_chars = re.search('[a-zA-Z]', chave)
  if (has_chars):
    return False
  else:     
    return ValidadorChaveAcessoNFe.validar(chave)          


def valida_chave(chave):
    if (len(chave) == constant.NUM_CHAVE):
        if (constant.VALIDA_CHAVE_PELO_DIGITO):
          return valida_chave_pelo_digito(chave)   
        else: 
          return True
    else:
        return False    


def get_chave():
    return ui.txtChave.toPlainText()

def get_chave_parcial():
    return ui.txtChave_2.toPlainText() + ui.txtChave_3.toPlainText()


def valida_uf(uf):
   result = False
   for row_data in lista_ufs:
      row = dict(row_data)
      if (row['codigo'] == uf): 
        result = True
   return result 

def mostra_mensagem(text):
    ui.lbl_message.setText(text)
    ui.lbl_message.show()
    limpa_mensagem_sucesso()
def limpa_mensagem():
    ui.lbl_message.setText("")
    ui.lbl_message.hide()

def mostra_mensagem_sucesso(text):
    limpa_mensagem()
    ui.lbl_info.setText(text)
    ui.lbl_info.show()
    
def limpa_mensagem_sucesso():
    ui.lbl_info.setText("")
    ui.lbl_info.hide()

def atualiza_contagem_digitos(text):
    ui.lblDigitos.setText("{num_digitos} dígitos".format(num_digitos=len(text)))

def on_limpa_banco_clickado():
    limpa_notas_db()
    lista_chaves.clear()
    combo_status_changed(1)
    
    
def chave_ja_existe(chave):
 return chave in lista_chaves

def cnpj_ja_existe(cnpj):
 return cnpj in lista_cnpj

def on_importar_arquivo():
  import importa  
  importador = importa.ImportaArquivo()
  result = importa.ImportResult()
  path = ui.txt_arquivo.toPlainText()
  
  if (len(path)==0):
    mostra_mensagem(messages.Messages().arquivo_diretorio_nao_informado)
    return

  if (not os.path.exists(path)) :
    mostra_mensagem(messages.Messages().arquivo_diretorio_nao_existe)
    return

  if (not os.path.isdir(path) ) :
    result = importador.importar_arquivo(path)
    origem = constant.ORIGEM_NOTA_IMPORTA
  else: 
    result = importador.importar_dir_xml(path)
    origem = constant.ORIGEM_NOTA_XML
     
  if (result.success): 
    
    for index, data in enumerate(result.data):

      if valida_chave(data):
          sequencia_adiciona_nota(data, origem)         
      else:
          print("Linha {linha} - Chave {chave} inválida".format(linha=index, chave=data))

    mostra_mensagem_sucesso(messages.Messages().importacao_sucesso)  
  else:
    mostra_mensagem(result.err)
   

def on_buscar_arquivo():
 
  try:
    if (not ui.check_dir.isChecked()):
      filename = QFileDialog.getOpenFileName(ui.centralwidget, constant.TITULO_DIALOG_ARQUIVO, None, "Text files (*.txt);;Csv files (*.csv);;Excel files (*.xlsx)")  
      if filename: 
        ui.txt_arquivo.setPlainText(filename[0])  
    else: 
      filename = str(QFileDialog.getExistingDirectory(ui.centralwidget, constant.TITULO_DIALOG_ARQUIVO))
      if filename: 
        ui.txt_arquivo.setPlainText(filename)  
      
      
  except ValueError as strerror:
      print(strerror)
   
def valida_filtros_busca_nota():
  
  estab = ui.txt_cnpj_estab.text()
  if ( (len(estab)>0) & (not valida_cnpj(estab))):
    mostra_mensagem(m.cnpj_estabelecimento_invalido)
    return False
  
  limit = int(ui.txt_num_notas.text())
  if (limit <constant.MIN_NOTAS | limit > constant.MAX_NOTAS):  
    mostra_mensagem(m.numero_notas_fora_range)
    return False

  return True  

def buscar_portal(): 
  import json
  token = Auth.getInstance().token
  cnpj = busca_cnpj_padrao_valor()
  estab = ui.txt_cnpj_estab.text()
  limit = int(ui.txt_num_notas.text())

  service = ApiPortal()
  result = ApiResult()
  
  cnpj = Util.remove_special_chars(cnpj)

  if (valida_filtros_busca_nota()) :

    result = service.busca_notas(token, cnpj, estab, limit )

    if (result.success):
      if (not result.data):
        mostra_mensagem(m.nenhuma_nota) 
      else:
          for index, item in enumerate(result.data):
            if (item['status']=="1"):
              if valida_chave(item['chave']):
                sequencia_adiciona_nota(item['chave'], constant.ORIGEM_NOTA_PORTAL)         
              else:
                print("Item {item} - Chave {chave} inválida".format(item=index+1, chave=item['chave']))
            
    else:
      mostra_mensagem(result.err) 


def atualiza_botao_login():
  ui.btn_login.setText(Auth.getInstance().user)

def on_baixar_portal():
  rows = busca_cnpj_padrao()
  if (not rows):
     mostra_dialogCnpj()
  else:
    token = Auth.getInstance().token
    if (not token):
      if (servico_login.mostra_login()):
        atualiza_botao_login()
        buscar_portal()  
    else: 
      buscar_portal()
       
def monthdelta(d1, d2):
    delta = 0
    while True:
        mdays = monthrange(d1.year, d1.month)[1]
        d1 += timedelta(days=mdays)
        if d1 <= d2:
            delta += 1
        else:
            break
    return delta



def verifica_data_expirada(data): 
 today = date.today() 
 #print("today =", today) 
 data_hoje = today.strftime("%d/%m/%Y")
 #print("data_hoje =", data_hoje)

 sub_ano = str(today.year)[0:2]
 #print("sub_ano = {}".format(sub_ano))

 ano = data[0:2]
 mes = data[2:4]
 dia = 1
 #print("ano = {}".format(sub_ano + ano))
 #print("mes = {}".format(mes))
 data_nota = date(year = int(sub_ano + ano), month = int(mes), day = dia)
 data_nota = data_nota.strftime("%d/%m/%Y")
 #print("data_nota = {}".format(data_nota))
 delta = monthdelta(datetime.strptime(data_nota,"%d/%m/%Y"), datetime.strptime(data_hoje,"%d/%m/%Y"))
 #print("Delta is {}".format(delta))
 
 if (delta <= 1):
    if (delta == 0):
        return False
    else:
        #delta = 1
        if (today.day<=constant.DIA_EXPIRA):
            return False
        else:
            return True          
 else:
    return True   

def atualiza_titulo_total():
  ui.lbTitulo.setText(m.titulo_lista_principal.format(ui.tableWidget.rowCount()))

def sequencia_adiciona_nota(chave, origem):
  if (not chave_ja_existe(chave)):

    nota_separada = separa_campos_pela_chave(chave)     
    nota_expirou = verifica_data_expirada(nota_separada.data)
  
    if (not valida_uf(nota_separada.uf)):    
       mostra_mensagem(m.uf_invalida)       
       emitir_som_erro(origem) 
    else:
      if ( (not nota_expirou) | (constant.SALVA_NOTA_EXPIRADA) ):   
        salva_chave_banco(nota_separada, nota_expirou, origem)
        adiciona_chave_na_lista(nota_separada, nota_expirou)
        mostra_mensagem_sucesso(messages.Messages().gravada_sucesso.format(chave))
        atualiza_titulo_total()
        

        #salva cnpj na base   
        if (constant.SALVA_CNPJ):
            if (not cnpj_ja_existe(nota_separada.cnpj)):
                salva_cnpj_banco(nota_separada)            
                lista_cnpj.append(nota_separada.cnpj)

      else:
        mostra_mensagem(m.data_expirada)      
        emitir_som_erro(origem)
  else:

   #se for captura por vídeo, não mostra que chave já existe, 
   # pois o video le varias vezes
   # caso contrário a mensagem sempre aparecerá que a chave já existe
   if (origem != 6):
     mostra_mensagem(m.chave_existe)
     emitir_som_erro(origem)
   
def on_cnpj_padrao_alterado():
    print('cnpj padrao alterado')
    text = dialog_cnpj_padrao.txt_cnpj_padrao.toPlainText()
    print(text)

def on_campo_chave_alterado():
    text = get_chave()
    atualiza_contagem_digitos(text)

    if (len(text) > constant.NUM_CHAVE  ):
       ui.txtChave.setPlainText(text[0:constant.NUM_CHAVE])

    if (len(text) == constant.NUM_CHAVE ):
       chave_ok = valida_chave(get_chave())    
       if (chave_ok): 
         sequencia_adiciona_nota(text, constant.ORIGEM_NOTA_MANUAL)
         limpa_campo_chave() 
       else:
         emitir_som_erro(constant.ORIGEM_NOTA_MANUAL)
         mostra_mensagem(m.chave_invalida)
         if (constant.LIMPA_CAMPO_QUANDO_INVALIDA):
           limpa_campo_chave() 

def on_campo_chave_alterado_2():
    text = get_chave_parcial()
    
    if (len(text) > constant.NUM_CHAVE  ):
       atual = ui.txtChave_3.toPlainText()
       ui.txtChave_3.setPlainText(text[0:len(atual)-1])

    if (len(text) == constant.NUM_CHAVE ):
       chave_ok = valida_chave(text)    
       if (chave_ok): 
         sequencia_adiciona_nota(text, constant.ORIGEM_NOTA_DIGITAR)
         limpa_campo_chave() 
       else:
         emitir_som_erro(constant.ORIGEM_NOTA_DIGITAR)
         mostra_mensagem(m.chave_invalida)
         if (constant.LIMPA_CAMPO_QUANDO_INVALIDA):
           limpa_campo_chave() 

        
def define_mes_padrao_int():
    mes_atual = date.today().month
    return mes_atual - 1

def define_mes_padrao():
    return date.today().strftime("%y%m")

def define_mes_anterior_int():
    d2 = date.today() - dateutil.relativedelta.relativedelta(months=1)
    #print("d2={}".format(d2))
    return d2.month - 1

def define_mes_anterior():
    d2 =  date.today() - dateutil.relativedelta.relativedelta(months=1)
    return datetime.strftime(d2, "%y%m")


def modo_digitacao():
    ui.tab_opcao.setCurrentIndex (2)
   

def modo_leitor():
    ui.tab_opcao.setCurrentIndex (1)
    ui.txtChave.setFocus()

def modo_video():
    ui.tab_opcao.setCurrentIndex (0)
    
def modoarquivo():
    ui.tab_opcao.setCurrentIndex (3)
    ui.btn_arquivo.setFocus()

def modoportal():
    ui.tab_opcao.setCurrentIndex (4)
    ui.btn_portal.setFocus()
    ui.txt_num_notas.text = str(constant.DEFAULT_NUMERO_NOTAS)

def limpa_stats():
  dialog_stats.lbl_hoje.setText("0")
  dialog_stats.lbl_pendentes.setText("0")
  dialog_stats.lbl_postadas.setText("0")
  dialog_stats.lbl_erro.setText("0")

def mostra_dialogStats():
   
   try:

    #aplica tema no dialog de cnpj padrão
    sshFile = constant.STYLES_FILE
    with open(sshFile,"r") as fh:
      Dialog_Cnpj.setStyleSheet(fh.read()) 

    rows = busca_chaves_stats_hoje() 
    soma = 0
    limpa_stats()

    if (rows):
      for row_data in rows:
          row = dict(row_data)
          soma+= int(row['contador']) 
          
          if(str(row['status']) == '1') :
            dialog_stats.lbl_pendentes.setText(str(row['contador']))
            
          if(str(row['status']) == '2') :
            dialog_stats.lbl_postadas.setText(str(row['contador']))

          if(str(row['status']) == '3') :
            dialog_stats.lbl_erro.setText(str(row['contador']))

    dialog_stats.lbl_hoje.setText(str(soma))   

    if  (Dialog_Stats.exec_()):
     return True
    else:
     return False      

   except Exception as err:
     limpa_stats()
     print(repr(err))  


def mostra_dialogCnpj():

   #aplica tema no dialog de cnpj padrão
   sshFile = constant.STYLES_FILE
   with open(sshFile,"r") as fh:
     Dialog_Cnpj.setStyleSheet(fh.read())   
   
   dialog_cnpj_padrao.lbl_message_cnpj_padrao.setText("")
   
   row = busca_cnpj_padrao()

   if (row):
     row = dict(row)
     dialog_cnpj_padrao.txt_cnpj_padrao.setFocus()
     dialog_cnpj_padrao.txt_cnpj_padrao.setPlainText(row['cnpj'])
     dialog_cnpj_padrao.txt_descricao_entidade.setPlainText(row['descricao'])
     dialog_cnpj_padrao.txt_palavras_chave.setPlainText(row['palavras']) 
   else:
     dialog_cnpj_padrao.txt_cnpj_padrao.setFocus()
     dialog_cnpj_padrao.txt_cnpj_padrao.setPlainText("")
     dialog_cnpj_padrao.txt_descricao_entidade.setPlainText("")
     dialog_cnpj_padrao.txt_palavras_chave.setPlainText("") 

   if  (Dialog_Cnpj.exec_()):
     return True
   else:
     return False  

def valida_cpf(cpf):
    return ValidadorCpf.validar(cpf)

def valida_cnpj(cnpj):
    return ValidadorCnpj.validar(cnpj)

def confirma_cnpj_padrao():
   cnpj = dialog_cnpj_padrao.txt_cnpj_padrao.toPlainText()  
   descricao = dialog_cnpj_padrao.txt_descricao_entidade.toPlainText()  
   palavras = dialog_cnpj_padrao.txt_palavras_chave.toPlainText()  

   if (len(cnpj)==0):
     dialog_cnpj_padrao.lbl_message_cnpj_padrao.setText(m.cnpj_invalido)
     return

   if (len(descricao)==0):
     dialog_cnpj_padrao.lbl_message_cnpj_padrao.setText(m.descricao_requerida)
     return

   if (valida_cnpj(cnpj)):
     salva_cnpj_padrao_banco(cnpj, descricao, palavras)  
    #atualiza botão na tela principal
     applyStylesToElement(ui.btn_cnpj, constant.STYLES_FILE_BUTTONS)
     #ui.btn_cnpj.setText("     " + cnpj )
     Dialog_Cnpj.accept()
   else:  
     dialog_cnpj_padrao.lbl_message_cnpj_padrao.setText(m.cnpj_invalido)
     
   
   


def txt_cnpj_padrao_keyPressEvent(e):
     if (e.key() == Qt.Key_Escape ):
         Dialog_Cnpj.reject()
     else:    
       if (e.key() == Qt.Key_Return or  e.key() == Qt.Key_Enter ): 
         confirma_cnpj_padrao()
       else: 
         return QPlainTextEdit.keyPressEvent(dialog_cnpj_padrao.txt_cnpj_padrao, e)     

def emitir_som_erro(origem):
  if (constant.EMITIR_SOM_ERRO):
   if (origem == constant.ORIGEM_NOTA_MANUAL or origem == constant.ORIGEM_NOTA_DIGITAR): 
      playsound(constant.SOM_ERRO_FILE)

def txtChave_3_keyPressEvent(e):
     if (e.key() == Qt.Key_Escape ):
       limpa_campo_chave()
   
     if (e.key() == Qt.Key_A ):
       modo_leitor()
       return 

     if (e.key() == Qt.Key_V ):
       modo_video()
       return 

     if (e.key() == Qt.Key_B ):
       modo_digitacao()   
       return

     if (e.key() == Qt.Key_C ):
       modoarquivo()   
       return 

     if (e.key() == Qt.Key_D ):
       modoportal()   
       return 

     if (e.key() == Qt.Key_E ):
       mostra_dialogCnpj()
       return      
     
     if (e.key() == Qt.Key_L ):
      on_abre_login()
      return  

     if (e.key() == Qt.Key_P ):
      on_abre_postar()
      return 

     if (e.key() == Qt.Key_Return or  e.key() == Qt.Key_Enter ):
       text = get_chave_parcial()
       chave_ok = valida_chave(text)    

       if (chave_ok): 
          sequencia_adiciona_nota(text, constant.ORIGEM_NOTA_DIGITAR) 
       else:
          emitir_som_erro(constant.ORIGEM_NOTA_DIGITAR)
          mostra_mensagem(m.chave_invalida)
          if (constant.LIMPA_CAMPO_QUANDO_INVALIDA):
            limpa_campo_chave()
     else: 
       return QPlainTextEdit.keyPressEvent(ui.txtChave_3, e)     

def mostra_data_nota():  
   global mes_sel_int       
   ano = mes_sel[0:2]
   print(constant.MESES[mes_sel_int])
   try:
      mes_view = constant.MESES[mes_sel_int] + " de " + ano
      dialog.lbl_mes.setText( mes_view)    
   except ValueError as strerror:
      print(strerror)
   
 
def atualiza_campo_parcial_nota(row):
    
    cnpj = (dialog.lista_empresas.item(row, 2).text())
    uf = (dialog.lista_empresas.item(row, 3).text())
    modelo = (dialog.lista_empresas.item(row, 4).text())
    serie = (dialog.lista_empresas.item(row, 5).text())
    
    mostra_data_nota()   
    data = mes_sel
    
    nota_parcial = uf+data+cnpj+modelo+serie
   
    ui.txtChave_2.setPlainText(nota_parcial[:-1])
    ui.txtChave_3.setPlainText(constant.EMPTY_STR)                 
    ui.txtChave_3.setFocus()

def toggle_mes():
    global mes_tipo
    global mes_sel
    global mes_sel_int

    if (mes_tipo == 1):
        mes_tipo = 2
        mes_sel = define_mes_anterior()
        mes_sel_int = define_mes_anterior_int()
        print(mes_sel_int)
    else:
        mes_tipo = 1
        mes_sel = define_mes_padrao()
        mes_sel_int = define_mes_padrao_int()
        print(mes_sel_int)
    

def lista_empresas_keyPressEvent(e):
     if (e.key() == Qt.Key_Space ):
        toggle_mes()
        mostra_data_nota()

     if (e.key() == Qt.Key_Escape ):
       Dialog.reject()
     else:   
       if (e.key() == Qt.Key_Return or  e.key() == Qt.Key_Enter ):
            if dialog.lista_empresas.selectionModel().hasSelection():
             row = dialog.lista_empresas.currentRow()
             atualiza_campo_parcial_nota(row)
             Dialog.accept()
       else: 
         return QTableWidget.keyPressEvent(dialog.lista_empresas, e)

def page_changed(index):
  if (index == 0):
    atualiza_lista_principal()
  if (index == 1): 
    on_abre_postar()


def trigger_postagem():
  
  if (seleciona_modo_atual() == 'parado') :
    task_postagem = Task(MainWindow)
    
    try:
      ui.sig_cancelar.connect(task_postagem.cancel_posting)
      ui.sig_cancelar.emit(0)
    except Exception as e:
      print(repr(e))

    task_postagem.sig_log.connect(show_log)
    task_postagem.sig_result.connect(save_result) 
    task_postagem.sig_chave.connect(init_value) 
    modo_postagem()
    task_postagem.start()

  else:
    if (seleciona_modo_atual() == 'postando'):
        ui.sig_cancelar.emit(1)
        modo_parado()


def on_abre_postar():
  rowCnpj = busca_cnpj_padrao()
  if (rowCnpj):
     mostra_posting(ui)
  else:
     
     if (mostra_dialogCnpj()):
       mostra_posting(ui)   
     else:
       ui.toolBox.setCurrentIndex(0)
         

  
 
def txtChave_keyPressEvent(e):
   if (e.key() == Qt.Key_Escape ):
       limpa_campo_chave()

   if (e.key() == Qt.Key_A ):
       modo_leitor()
       return 
   
   if (e.key() == Qt.Key_V ):
       modo_video()
       return 

   if (e.key() == Qt.Key_B ):
       modo_digitacao()   
       return   

   if (e.key() == Qt.Key_C ):
       modoarquivo()   
       return 

   if (e.key() == Qt.Key_D ):
       modoportal()   
       return      
       
   if (e.key() == Qt.Key_E ):
       mostra_dialogCnpj()
       return      

   if (e.key() == Qt.Key_L ):
      on_abre_login()
      return   

   
   if (e.key() == Qt.Key_P ):
      on_abre_postar()
      return   

   if (e.key() == Qt.Key_Return or  e.key() == Qt.Key_Enter ):
       text = get_chave()
       chave_ok = valida_chave(text)    

       if (chave_ok): 
          sequencia_adiciona_nota(text, constant.ORIGEM_NOTA_MANUAL) 
       else:
          emitir_som_erro(constant.ORIGEM_NOTA_MANUAL)
          mostra_mensagem(m.chave_invalida)
          if (constant.LIMPA_CAMPO_QUANDO_INVALIDA):
            limpa_campo_chave()

   else: 
       return QPlainTextEdit.keyPressEvent(ui.txtChave, e)


def on_abre_login():
  if (servico_login.mostra_login()):
    atualiza_botao_login()

def applyStyles():
   #TODO - pegar style de uma classe singleton, carregada uma unica vez"styles/main.css"
  sshFile = constant.STYLES_FILE
  with open(sshFile,"r") as fh:
    MainWindow.setStyleSheet(fh.read())      

def applyStylesToElement(component, cssFile):
  with open(cssFile,"r") as fh:
    component.setStyleSheet(fh.read())     

def mostra_tela_estab():
  
  #Dialog.show()

  sshFile = constant.STYLES_FILE
  with open(sshFile,"r") as fh:
    Dialog.setStyleSheet(fh.read()) 

  mostra_data_nota()
  rows = busca_cnpj_banco()
  carrega_lista_empresas(rows)

  if  (Dialog.exec_()):
      if dialog.lista_empresas.selectionModel().hasSelection():
       row = dialog.lista_empresas.currentRow()
       atualiza_campo_parcial_nota(row)
  


def tab_changed(index):
  if (index == 0):
    ui.btn_video.setFocus()
    
  if (index == 1):
    ui.txtChave.setFocus()
    
  if (index == 2):
    ui.txtChave_3.setFocus()
    ui.txtChave_2.setPlainText(constant.EMPTY_STR)
    ui.txtChave_3.setPlainText(constant.EMPTY_STR)
    mostra_tela_estab()

def fechar_stats():
  Dialog_Stats.accept()

def fechar_dialog_cnpj_padrao():
   row = busca_cnpj_padrao()
   if (not row):
    applyStylesToElement(ui.btn_cnpj, constant.STYLES_FILE_BUTTONS_ALERT)   
   else:
    applyStylesToElement(ui.btn_cnpj, constant.STYLES_FILE_BUTTONS)     
   
   Dialog_Cnpj.reject()

def atualiza_lista_principal():
   rows = busca_chaves_por_status(constant.DEFAULT_STATUS_CODIGO)
   carrega_lista_chaves(rows)
   atualiza_titulo_total()


def chama_rotina_update():

        handler = Update_Handler() 
        #se não tem versão nova, sai da rotina, e segue o programa
        if ( not handler.verifica_updates() ) :       
          return
        else:
            
            #se tem versão nova, faz o download do instalador
            versao_nova = handler.get_versao_nova()
            result = handler.download_update(versao_nova)
              
            if (result.success):

                  #salva arquivo no diretorio de patches
                  directory = 'c://temp/notaamiga-patches'
                  if not os.path.exists(directory):
                    os.makedirs(directory)

                  filename = directory + '//' + result.filename
                  with open(filename, "wb") as file:
                    file.write(result.data)

                  #executa o instalador 
                  print('Iniciando atualizador...')
                  subprocess.Popen([filename], shell=False,
                  stdin=None, stdout=None, stderr=None, close_fds=True)
                  print('Finalizando verificador de atualizações...')

                  #sai do programa principal
                  exit()

            else: 
              print('Erro ao tentar verificar atualizações...' + result.err)    
              
            
           

def aplica_scripts_inicio():
  script_file = './/patches//' + app_version.VERSION + '//script.sql' 
  if ( os.path.exists(script_file) ) :
    qry = open(script_file, 'r').read()
    dbutil.execute_sql(qry)
    os.rename(script_file, str(script_file).replace('.sql','.old' ))



def muda_status_tela(status):
   ui.btn_stat.setEnabled(status)
   ui.btn_postar.setEnabled(status)
   ui.btn_cnpj.setEnabled(status)
   ui.tab_opcao.setEnabled(status)
   ui.combo_status.setEnabled(status)
   ui.tableWidget.setEnabled(status)

def video_read(content):
    chave = str(content).split("|")[0].replace("CFe","")
     
    #verifica se nota tem cpf/cnpj, se tiver, invalida  a nota pois não pode receber creditos
    #essa validacao só é possivel na leitura por vídeo
    try:
      cpf_cnpj = str(content).split("|")[3]
      if (len(cpf_cnpj) > 0):
        if ( (valida_cnpj(cpf_cnpj)) or (valida_cpf(cpf_cnpj))  ):
          mostra_mensagem(m.chave_com_cpf_cnpj)
          return 
    except Exception as err:
      print('ERRO ao tentar validar se existe cpf/cnpj na nota: ' + repr(err)) 
                

    chave_ok = valida_chave(chave)    
    if (chave_ok): 
        sequencia_adiciona_nota(chave, constant.ORIGEM_NOTA_VIDEO)        
    else:
        emitir_som_erro(constant.ORIGEM_NOTA_VIDEO)
        mostra_mensagem(m.chave_invalida)
        

def video_stopped(status):
   global video_status
   ui.btn_video.setText("    Iniciar Captura")
   ui.btn_video.setEnabled(True)
   icon = QIcon("assets/icons/qrcode2.png")
   ui.btn_video.setIcon(icon)
   ui.btn_video.setIconSize(QSize(24,24))
   QApplication.restoreOverrideCursor()
   ui.label_video.setPixmap(QPixmap('assets/video_image.png'))
   video_status = VideoStatus.IDLE

   #retorna outros elementos da tela
   muda_status_tela(True)

def video_started(status):
  global video_status

  if (status == 1):
    status = 0
    video_status = VideoStatus.IN_PROGRESS
    ui.btn_video.setText("    Parar Captura")
    ui.btn_video.setEnabled(True)
    icon = QIcon("assets/icons/stop_small.png")
    ui.btn_video.setIcon(icon)
    ui.btn_video.setIconSize(QSize(24,24))
    QApplication.restoreOverrideCursor()

    #retorna outros elementos da tela
    muda_status_tela(True)
   


   


def setImage(image):
  ui.label_video.setPixmap(QPixmap.fromImage(image))

def on_video():

  global video_status

  if (video_status == VideoStatus.IDLE):
    video_status = VideoStatus.WARMING
    ui.btn_video.setText("    Iniciando captura por vídeo...")
    ui.label_video.setPixmap(QPixmap('assets/video_image_warming.png'))
    ui.btn_video.setEnabled(False)
    icon = QIcon("assets/icons/progress.png")
    ui.btn_video.setIcon(icon)
    ui.btn_video.setIconSize(QSize(24,24))
    QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
    
    #bloqueia outros elementos da tela
    muda_status_tela(False)

    task = TaskVideo(MainWindow)
    task.sig_image.connect(setImage)
    task.sig_start.connect(video_started)
    task.sig_stop.connect(video_stopped)
    task.sig_read.connect(video_read)
    ui.sig_cancelar_video.connect(task.cancel_video)
    task.start()

    

  elif (video_status == VideoStatus.IN_PROGRESS):
    ui.sig_cancelar_video.emit(1)
    
   

 
  
  
if __name__ == "__main__":
        
        m = Messages()

        app = QApplication(argv)
        MainWindow = QMainWindow()
        ui = ui_list.Ui_MainWindow()
        ui.setupUi(MainWindow)

        

        chama_rotina_update()
        aplica_scripts_inicio()

        applyStyles()
        MainWindow.show()

        MainWindow.setWindowState(Qt.WindowMaximized)

        

        ui.txtChave.setFocus()

        Dialog = QDialog()
        dialog = ui_cnpj_dialog.Ui_Dialog()
        dialog.setupUi(Dialog)
        Dialog.setModal(True)
        
        Dialog_Cnpj = QDialog()
        dialog_cnpj_padrao = ui_cnpj_padrao_dialog.Ui_Dialog()
        dialog_cnpj_padrao.setupUi(Dialog_Cnpj)
        Dialog_Cnpj.setModal(True)

        Dialog_Stats = QDialog()
        dialog_stats = ui_stats.Ui_Dialog()
        dialog_stats.setupUi(Dialog_Stats)
        Dialog_Stats.setModal(True)

        
        servico_login = Login()
        ui.btn_login.clicked.connect(on_abre_login)    

        #connect events
        ui.txtChave.textChanged.connect(on_campo_chave_alterado)    
        ui.txtChave_2.textChanged.connect(on_campo_chave_alterado_2)    
        ui.txtChave_3.textChanged.connect(on_campo_chave_alterado_2)   
        
        ui.txtChave.keyPressEvent = txtChave_keyPressEvent
        ui.txtChave_3.keyPressEvent = txtChave_3_keyPressEvent
        ui.btn_limpa_banco.clicked.connect(on_limpa_banco_clickado)    

        ui.btn_arquivo.clicked.connect(on_buscar_arquivo)    
        ui.btn_importar.clicked.connect(on_importar_arquivo)    
        ui.btn_portal.clicked.connect(on_baixar_portal) 

        ui.btn_video.clicked.connect(on_video) 
        
        
        limpa_mensagem()
        limpa_mensagem_sucesso()

        
           
        dialog_cnpj_padrao.txt_cnpj_padrao.textChanged.connect(on_cnpj_padrao_alterado )
        dialog_cnpj_padrao.txt_cnpj_padrao.keyPressEvent = txt_cnpj_padrao_keyPressEvent
        
        ui.btn_cnpj.clicked.connect(mostra_dialogCnpj)
        cnpj = busca_cnpj_padrao_valor()
        
        dialog_cnpj_padrao.btn_ok.clicked.connect(confirma_cnpj_padrao)
        dialog_cnpj_padrao.btn_cancel.clicked.connect(fechar_dialog_cnpj_padrao)

        ui.btn_stat.clicked.connect(mostra_dialogStats)  
        dialog_stats.btn_ok.clicked.connect(fechar_stats)
        
        ui.txt_num_notas.setValidator(QIntValidator(constant.MIN_NOTAS , constant.MAX_NOTAS) )
        ui.txt_num_notas.setText(str(constant.DEFAULT_NUMERO_NOTAS))
        
        ui.txt_cnpj_estab.setText(constant.EMPTY_STR)
        
        ui.tab_opcao.currentChanged.connect(tab_changed)
        ui.btn_estab.clicked.connect(mostra_tela_estab)
        

        ui.btn_postar.hide()
        ui.toolBox.currentChanged.connect(page_changed)

        ui.btn_iniciar_postagem.clicked.connect(trigger_postagem)        
        ui.btn_limpar.clicked.connect(limpar_log)
        ui.btn_fechar.hide()
        
        
        
        lista_chaves = []
        lista_cnpj = []
        
        mes_tipo = 1 #mes atual
        mes_sel = define_mes_padrao()
        mes_sel_int = define_mes_padrao_int()
        
      

        
        #cria lista (notas e empresas)
        cria_tabela_notas()  
        cria_tabela_empresas()      
      
        dialog.lista_empresas.keyPressEvent = lista_empresas_keyPressEvent

        #carrega lista de notas do banco
        atualiza_lista_principal()

        #busca lista total de chaves
        rows_total = busca_chaves_banco() 
        carrega_lista_chaves_total(rows_total)
       
        
        #lista ufs
        lista_ufs = busca_uf_banco()

        #lista status
        rows = busca_status_banco()
        carrega_lista_status(rows)

        #carrega cnpjs na memoria
        rows = busca_cnpj_banco()
        carrega_lista_empresas(rows)


        ui.btn_limpa_banco.hide()
        


        ui.label_video.setPixmap(QPixmap('assets/video_image.png'))
        video_status = VideoStatus.IDLE 
        modo_video()

        if (not feature_flags.PORTAL):
          ui.btn_login.hide()
          ui.tab_opcao.setTabEnabled(4, False)
        


        rowCnpj = busca_cnpj_padrao()
        if (rowCnpj):
           cnpj = dict(rowCnpj)['cnpj']
           #ui.btn_cnpj.setText("     " + cnpj )
           applyStylesToElement(ui.btn_cnpj, constant.STYLES_FILE_BUTTONS)
        else:
           #ui.btn_cnpj.setText(m.cnpj_nao_informado)
           applyStylesToElement(ui.btn_cnpj, constant.STYLES_FILE_BUTTONS_ALERT)
           mostra_dialogCnpj()
            
        exit(app.exec_())

        
    

    
   
 