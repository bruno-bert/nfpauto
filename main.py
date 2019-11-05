#external libs
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QTableWidgetItem, QListWidgetItem
from bradocs4py.chaveacessonfe import ValidadorChaveAcessoNFe  
from bradocs4py.cnpj import  ValidadorCnpj 


#native libs
import sqlite3
import re
from datetime import date, datetime, timedelta
from calendar import monthrange
import dateutil.relativedelta
import os.path



#internal modules
from db.initdb import init_db
import constant
from nota import Nota
from messages import Messages
from login import Login
from posting import Posting
from database import *
from auth import Auth 

#ui - internal modules
import ui_list
import ui_cnpj_dialog
import ui_cnpj_padrao_dialog

from api import ApiPortal, ApiResult

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



def carrega_lista_chaves(rows):

    ui.tableWidget.setRowCount(0) 

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
            lista_notas.append(row['chave'])

    header = ui.tableWidget.horizontalHeader()       
    header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
    header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
    header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents) 
    header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents) 
    header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents) 
    header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents) 
    header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents) 
    header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents) 
    header.setSectionResizeMode(8, QtWidgets.QHeaderView.ResizeToContents) 
    header.setSectionResizeMode(9, QtWidgets.QHeaderView.ResizeToContents) 
    header.setSectionResizeMode(10, QtWidgets.QHeaderView.ResizeToContents) 
    header.setSectionResizeMode(11, QtWidgets.QHeaderView.ResizeToContents) 
        


def cria_tabela_notas():
    ui.tableWidget.setColumnCount(12)
    ui.tableWidget.setRowCount(1)
    ui.tableWidget.hideColumn(0) #esconde coluna de id
    ui.tableWidget.hideColumn(10) #esconde coluna de tipo_emissao

    
    ui.tableWidget.setHorizontalHeaderLabels(
                                      ['ID', 'Chave', 
                                       'CNPJ', 
                                       'Data', 'Status', 
                                       'UF', 'Numero', 
                                       'Codigo', 'Modelo', 
                                       'Serie', 'Tipo Emissao', 'Mensagem'])                                       

def cria_tabela_empresas():
    dialog.lista_empresas.setColumnCount(6)
    dialog.lista_empresas.setRowCount(1)
 
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

def adiciona_chave_na_lista(new_nota, expirada):

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

    lista_notas.append(new_nota.chave)

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
def limpa_mensagem():
    ui.lbl_message.setText("")
    ui.lbl_message.hide()

def atualiza_contagem_digitos(text):
    ui.lblDigitos.setText("{num_digitos} dígitos".format(num_digitos=len(text)))

def on_limpa_banco_clickado():
    limpa_notas_db()
    lista_notas.clear()
    rows = busca_chaves_banco()
    carrega_lista_chaves(rows)

    
def chave_ja_existe(chave):
 return chave in lista_notas

def cnpj_ja_existe(cnpj):
 return cnpj in lista_cnpj

def on_importar_arquivo():
  import importa  
  importador = importa.ImportaArquivo()
  result = importa.ImportResult()
  path = ui.txt_arquivo.toPlainText()

  if (not os.path.isdir(path) ) :
    result = importador.importar_arquivo(path)
  else: 
    result = importador.importar_dir_xml(path)
     
  if (result.success): 
    
    for index, data in enumerate(result.data):

      if valida_chave(data):
          sequencia_adiciona_nota(data)         
      else:
          print("Linha {linha} - Chave {chave} inválida".format(linha=index, chave=data))

  else:
    mostra_mensagem(result.err)
   

def on_buscar_arquivo():
 
  try:
    if (not ui.check_dir.isChecked()):
      filename = QtWidgets.QFileDialog.getOpenFileName(ui.centralwidget, constant.TITULO_DIALOG_ARQUIVO, None, "Text files (*.txt);;Csv files (*.csv);;Excel files (*.xlsx)")  
      if filename: 
        ui.txt_arquivo.setPlainText(filename[0])  
    else: 
      filename = str(QtWidgets.QFileDialog.getExistingDirectory(ui.centralwidget, constant.TITULO_DIALOG_ARQUIVO))
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
  
  if (valida_filtros_busca_nota()) :

    result = service.busca_notas(token, cnpj, estab, limit )

    if (result.success):
      if (not result.data):
        mostra_mensagem(m.nenhuma_nota) 
      else:
          for index, item in enumerate(result.data):
            if (item['status']=="1"):
              if valida_chave(item['chave']):
                sequencia_adiciona_nota(item['chave'])         
              else:
                print("Item {item} - Chave {chave} inválida".format(item=index+1, chave=item['chave']))
            
    else:
      mostra_mensagem(result.err) 


def atualiza_botao_login():
  ui.btn_login.setText("Usuário Logado: " + Auth.getInstance().user)

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

 
def sequencia_adiciona_nota(chave):
  if (not chave_ja_existe(chave)):

    nota_separada = separa_campos_pela_chave(chave)     
    nota_expirou = verifica_data_expirada(nota_separada.data)

    if (not valida_uf(nota_separada.uf)):    
       mostra_mensagem(m.uf_invalida) 
    else:
      if ( (not nota_expirou) | (constant.SALVA_NOTA_EXPIRADA) ):   
        salva_chave_banco(nota_separada, nota_expirou)
        adiciona_chave_na_lista(nota_separada, nota_expirou)
        limpa_mensagem()

        #salva cnpj na base   
        if (constant.SALVA_CNPJ):
            if (not cnpj_ja_existe(nota_separada.cnpj)):
                salva_cnpj_banco(nota_separada)            
                lista_cnpj.append(nota_separada.cnpj)

      else:
        mostra_mensagem(m.data_expirada)      

  else:
   mostra_mensagem(m.chave_existe)
   print("Chave {} já existe".format(chave))     

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
         sequencia_adiciona_nota(text)
         limpa_campo_chave() 
       else:
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
         sequencia_adiciona_nota(text)
         limpa_campo_chave() 
       else:
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
    ui.tab_opcao.setCurrentIndex (1)
    ui.txtChave_3.setFocus()
    Dialog.show()
    ui.txtChave_2.setPlainText(constant.EMPTY_STR)
    ui.txtChave_3.setPlainText(constant.EMPTY_STR)
    mostra_data_nota()
    rows = busca_cnpj_banco()
    carrega_lista_empresas(rows)

def modo_leitor():
    ui.tab_opcao.setCurrentIndex (0)
    ui.txtChave.setFocus()

def modoarquivo():
    ui.tab_opcao.setCurrentIndex (2)
    ui.btn_arquivo.setFocus()

def modoportal():
    ui.tab_opcao.setCurrentIndex (3)
    ui.btn_portal.setFocus()
    ui.txt_num_notas.text = str(constant.DEFAULT_NUMERO_NOTAS)

def mostra_dialogCnpj():

   #aplica tema no dialog de cnpj padrão
   sshFile = constant.STYLES_FILE
   with open(sshFile,"r") as fh:
     Dialog_Cnpj.setStyleSheet(fh.read())   

   Dialog_Cnpj.show()
   row = busca_cnpj_padrao()
   row = dict(row)
   
   dialog_cnpj_padrao.txt_cnpj_padrao.setFocus()
   dialog_cnpj_padrao.txt_cnpj_padrao.setPlainText(row['cnpj'])
   dialog_cnpj_padrao.txt_descricao_entidade.setPlainText(row['descricao'])
   dialog_cnpj_padrao.txt_palavras_chave.setPlainText(row['palavras'])

def valida_cnpj(cnpj):
    return ValidadorCnpj.validar(cnpj)

def confirma_cnpj_padrao():
   cnpj = dialog_cnpj_padrao.txt_cnpj_padrao.toPlainText()  
   descricao = dialog_cnpj_padrao.txt_descricao_entidade.toPlainText()  
   palavras = dialog_cnpj_padrao.txt_palavras_chave.toPlainText() 
         
   if (valida_cnpj(cnpj)):
     salva_cnpj_padrao_banco(cnpj, descricao, palavras)  
     #atualiza botão na tela principal
     #ui.btn_cnpj.setText(cnpj )
     Dialog_Cnpj.accept()
   else:  
     dialog_cnpj_padrao.lbl_message_cnpj_padrao.setText(m.cnpj_invalido)
     print(m.cnpj_invalido)


def txt_cnpj_padrao_keyPressEvent(e):
     if (e.key() == QtCore.Qt.Key_Escape ):
         Dialog_Cnpj.reject()
     else:    
       if (e.key() == QtCore.Qt.Key_Return or  e.key() == QtCore.Qt.Key_Enter ): 
         confirma_cnpj_padrao()
       else: 
         return QtWidgets.QPlainTextEdit.keyPressEvent(dialog_cnpj_padrao.txt_cnpj_padrao, e)     


def txtChave_3_keyPressEvent(e):
     if (e.key() == QtCore.Qt.Key_Escape ):
       limpa_campo_chave()
   
     if (e.key() == QtCore.Qt.Key_A ):
       modo_leitor()
       return 

     if (e.key() == QtCore.Qt.Key_B ):
       modo_digitacao()   
       return

     if (e.key() == QtCore.Qt.Key_C ):
       modoarquivo()   
       return 

     if (e.key() == QtCore.Qt.Key_D ):
       modoportal()   
       return 

     if (e.key() == QtCore.Qt.Key_E ):
       mostra_dialogCnpj()
       return      
     
     if (e.key() == QtCore.Qt.Key_L ):
      on_abre_login()
      return  

     if (e.key() == QtCore.Qt.Key_P ):
      on_abre_postar()
      return 

     if (e.key() == QtCore.Qt.Key_Return or  e.key() == QtCore.Qt.Key_Enter ):
       text = get_chave_parcial()
       chave_ok = valida_chave(text)    

       if (chave_ok): 
          sequencia_adiciona_nota(text) 
       else:
          mostra_mensagem(m.chave_invalida)
          if (constant.LIMPA_CAMPO_QUANDO_INVALIDA):
            limpa_campo_chave()
     else: 
       return QtWidgets.QPlainTextEdit.keyPressEvent(ui.txtChave_3, e)     

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
     if (e.key() == QtCore.Qt.Key_Space ):
        toggle_mes()
        mostra_data_nota()

     if (e.key() == QtCore.Qt.Key_Escape ):
       Dialog.reject()
     else:   
       if (e.key() == QtCore.Qt.Key_Return or  e.key() == QtCore.Qt.Key_Enter ):
            if dialog.lista_empresas.selectionModel().hasSelection():
             row = dialog.lista_empresas.currentRow()
             atualiza_campo_parcial_nota(row)
             Dialog.accept()
       else: 
         return QtWidgets.QTableWidget.keyPressEvent(dialog.lista_empresas, e)

def on_abre_postar():
 servico_posting = Posting() 
 servico_posting.mostra_posting()
 #if (servico_posting.mostra_posting()):
 #  print('Form de postagem fechado')
 #else:
 #  print('Form de postagem fechado')  

def txtChave_keyPressEvent(e):
   if (e.key() == QtCore.Qt.Key_Escape ):
       limpa_campo_chave()

   if (e.key() == QtCore.Qt.Key_A ):
       modo_leitor()
       return 

   if (e.key() == QtCore.Qt.Key_B ):
       modo_digitacao()   
       return   

   if (e.key() == QtCore.Qt.Key_C ):
       modoarquivo()   
       return 

   if (e.key() == QtCore.Qt.Key_D ):
       modoportal()   
       return      
       
   if (e.key() == QtCore.Qt.Key_E ):
       mostra_dialogCnpj()
       return      

   if (e.key() == QtCore.Qt.Key_L ):
      on_abre_login()
      return   

   
   if (e.key() == QtCore.Qt.Key_P ):
      on_abre_postar()
      return   

   if (e.key() == QtCore.Qt.Key_Return or  e.key() == QtCore.Qt.Key_Enter ):
       text = get_chave()
       chave_ok = valida_chave(text)    

       if (chave_ok): 
          sequencia_adiciona_nota(text) 
       else:
          mostra_mensagem(m.chave_invalida)
          if (constant.LIMPA_CAMPO_QUANDO_INVALIDA):
            limpa_campo_chave()

   else: 
       return QtWidgets.QPlainTextEdit.keyPressEvent(ui.txtChave, e)


def on_abre_login():
  if (servico_login.mostra_login()):
    atualiza_botao_login()

def applyStyles():
   #TODO - pegar style de uma classe singleton, carregada uma unica vez"styles/main.css"
  sshFile = constant.STYLES_FILE
  with open(sshFile,"r") as fh:
    MainWindow.setStyleSheet(fh.read())      

if __name__ == "__main__":
        import sys    
    
        app = QtWidgets.QApplication(sys.argv)
        
      
        MainWindow = QtWidgets.QMainWindow()
        ui = ui_list.Ui_MainWindow()
        ui.setupUi(MainWindow)

        applyStyles()

        MainWindow.show()

        MainWindow.setWindowState(QtCore.Qt.WindowMaximized)


        ui.txtChave.setFocus()

        Dialog = QtWidgets.QDialog()
        dialog = ui_cnpj_dialog.Ui_Dialog()
        dialog.setupUi(Dialog)
        Dialog.setModal(True)
        
        Dialog_Cnpj = QtWidgets.QDialog()
        dialog_cnpj_padrao = ui_cnpj_padrao_dialog.Ui_Dialog()
        dialog_cnpj_padrao.setupUi(Dialog_Cnpj)
        Dialog_Cnpj.setModal(True)
        
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
        
        ui.lbl_message.hide()
        #ui.btn_limpa_banco.hide()
        
           
        dialog_cnpj_padrao.txt_cnpj_padrao.textChanged.connect(on_cnpj_padrao_alterado )
        dialog_cnpj_padrao.txt_cnpj_padrao.keyPressEvent = txt_cnpj_padrao_keyPressEvent
        
        ui.btn_cnpj.clicked.connect(mostra_dialogCnpj)
        cnpj = busca_cnpj_padrao_valor()
        #ui.btn_cnpj.setText(cnpj)

        dialog_cnpj_padrao.btn_ok.clicked.connect(confirma_cnpj_padrao)
        dialog_cnpj_padrao.btn_cancel.clicked.connect(Dialog_Cnpj.reject)
        
        ui.txt_num_notas.setValidator(QtGui.QIntValidator(constant.MIN_NOTAS , constant.MAX_NOTAS) )
        ui.txt_num_notas.setText(str(constant.DEFAULT_NUMERO_NOTAS))
        
        ui.txt_cnpj_estab.setText(constant.EMPTY_STR)
        
        

        ui.btn_postar.clicked.connect(on_abre_postar)    
        
        m = Messages()

        lista_notas = []
        lista_cnpj = []
        
        mes_tipo = 1 #mes atual
        mes_sel = define_mes_padrao()
        mes_sel_int = define_mes_padrao_int()
        
      

        if constant.INICIA_DB_INICIO:
            init_db()

        #cria lista (notas e empresas)
        cria_tabela_notas()  
        cria_tabela_empresas()      
      
        dialog.lista_empresas.keyPressEvent = lista_empresas_keyPressEvent

        #carrega lista de notas do banco
        rows = busca_chaves_por_status(constant.DEFAULT_STATUS_CODIGO)
        carrega_lista_chaves(rows)
        
        #lista ufs
        lista_ufs = busca_uf_banco()

        #lista status
        rows = busca_status_banco()
        carrega_lista_status(rows)

        #carrega cnpjs na memoria
        rows = busca_cnpj_banco()
        carrega_lista_empresas(rows)
        

        modo_leitor()

        

        sys.exit(app.exec_())

        
    

    
   
 