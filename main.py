#external libs
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QListWidgetItem
from bradocs4py.chaveacessonfe import ValidadorChaveAcessoNFe  

#native libs
import sqlite3
import re
from datetime import date, datetime
import dateutil.relativedelta

#internal modules
from initdb import init_db, limpa_notas_db
import constant
from nota import Nota
from messages import Messages

#ui - internal modules
import ui_list
import ui_cnpj_dialog

def busca_chaves_banco():
 conn = sqlite3.connect('notas.db')
 query = "select * from notas"
 conn.row_factory = sqlite3.Row
 cur = conn.cursor()
 cur.execute(query)
 rows = cur.fetchall()
 conn.close()
 return rows

def busca_cnpj_banco():
 conn = sqlite3.connect('notas.db')
 query = "select * from cnpj"
 conn.row_factory = sqlite3.Row
 cur = conn.cursor()
 cur.execute(query)
 rows = cur.fetchall()
 conn.close()
 return rows 


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

 


def cria_tabela_notas():
    ui.tableWidget.setColumnCount(12)
    ui.tableWidget.setRowCount(1)
 
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
    dialog.lista_empresas.setItem(0, 0, QTableWidgetItem("new") )
    dialog.lista_empresas.setItem(0, 1, QTableWidgetItem("") )
    dialog.lista_empresas.setItem(0, 2, QTableWidgetItem(new_nota.cnpj) )    
    dialog.lista_empresas.setItem(0, 3, QTableWidgetItem(new_nota.uf) )
    dialog.lista_empresas.setItem(0, 4, QTableWidgetItem(new_nota.modelo) )
    dialog.lista_empresas.setItem(0, 5, QTableWidgetItem(new_nota.serie) )
    lista_cnpj.append(new_nota.cnpj)

def adiciona_chave_na_lista(new_nota, expirada):

    ui.tableWidget.insertRow(0)
    ui.tableWidget.setItem(0, 0, QTableWidgetItem("new") )
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
    if (len(get_chave()) == constant.NUM_CHAVE):
        if (constant.VALIDA_CHAVE_PELO_DIGITO):
          return valida_chave_pelo_digito(chave)   
        else: 
          return True
    else:
        return False    


def get_chave():
    return ui.txtChave.toPlainText()

def salva_chave_banco(new_nota):
    conn = sqlite3.connect('notas.db')
    cursor = conn.cursor()
    cursor.execute(constant.QUERY_SAVE,  
                    (new_nota.chave, 
                     new_nota.cnpj, 
                     new_nota.data, 
                     new_nota.uf, 
                     new_nota.numero, 
                     new_nota.codigo, 
                     new_nota.modelo, 
                     new_nota.serie, 
                     new_nota.tipo_emissao, 
                     constant.DEFAULT_STATUS, 
                     m.aguardando_postagem) )
    conn.commit()
    conn.close()

def salva_cnpj_banco(new_nota):
    conn = sqlite3.connect('notas.db')
    cursor = conn.cursor()
    cursor.execute(constant.QUERY_SAVE_CNPJ,  
                    (
                     new_nota.cnpj, 
                     new_nota.uf, 
                     new_nota.modelo, 
                     new_nota.serie) )
    conn.commit()
    conn.close()


def mostra_mensagem(text):
    ui.lbl_message.setText(text)
def limpa_mensagem():
    ui.lbl_message.setText("")

def atualiza_contagem_digitos(text):
    ui.lblDigitos.setText("{num_digitos} dígitos".format(num_digitos=len(text)))

def on_limpa_banco_clickado():
    limpa_notas_db()
    lista_notas.clear()
    carrega_lista_chaves(None)

def chave_ja_existe(chave):
 return chave in lista_notas

def cnpj_ja_existe(cnpj):
 return cnpj in lista_cnpj

from calendar import monthrange
from datetime import date, datetime, timedelta

DIA_EXPIRA = 20

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
        if (today.day<=DIA_EXPIRA):
            return False
        else:
            return True          
 else:
    return True   

 
def sequencia_adiciona_nota(chave):
  if (not chave_ja_existe(chave)):

    nota_separada = separa_campos_pela_chave(chave)     
    nota_expirou = verifica_data_expirada(nota_separada.data)   

    if ( (not nota_expirou) | (constant.SALVA_NOTA_EXPIRADA) ):   
     salva_chave_banco(nota_separada)
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

def on_campo_chave_alterado():
    text = get_chave()
    atualiza_contagem_digitos(text)

    if (len(text) >= constant.NUM_CHAVE ):
       chave_ok = valida_chave(get_chave())    
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
    return d2.month

def define_mes_anterior():
    print('inicio')
    d2 =  date.today() - dateutil.relativedelta.relativedelta(months=1)
    print('fim')
    return datetime.strftime(d2, "%y%m")


def modo_digitacao():
    ui.tab_opcao.setCurrentIndex (1)
    ui.txtChave_3.setFocus()
    Dialog.show()
    mostra_data_nota()
    rows = busca_cnpj_banco()
    carrega_lista_empresas(rows)

def modo_leitor():
    ui.tab_opcao.setCurrentIndex (0)
    ui.txtChave.setFocus()


def txtChave_3_keyPressEvent(e):
   if (e.key() == QtCore.Qt.Key_Escape ):
       limpa_campo_chave()
   
   if (e.key() == QtCore.Qt.Key_L ):
       modo_leitor()
       return 

   if (e.key() == QtCore.Qt.Key_D ):
       modo_digitacao()   
       return 
   else: 
       return QtWidgets.QPlainTextEdit.keyPressEvent(ui.txtChave_3, e)     

def mostra_data_nota():          
   mes_view = mes_sel #datetime.strftime(mes_sel, constant.MESES[mes_sel_int]  + " de %Y")
   dialog.lbl_mes.setText(mes_view)    
   

def atualiza_campo_parcial_nota(row):
    
    cnpj = (dialog.lista_empresas.item(row, 2).text())
    uf = (dialog.lista_empresas.item(row, 3).text())
    modelo = (dialog.lista_empresas.item(row, 4).text())
    serie = (dialog.lista_empresas.item(row, 5).text())
    
    mostra_data_nota()   
    data = mes_sel
    
    nota_parcial = uf+data+cnpj+modelo+serie
   
    ui.txtChave_2.setPlainText(nota_parcial)
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
    else:
        mes_tipo = 1
        mes_sel = define_mes_padrao()
        mes_sel_int = define_mes_padrao_int()
    
    

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

def txtChave_keyPressEvent(e):
   if (e.key() == QtCore.Qt.Key_Escape ):
       limpa_campo_chave()

   if (e.key() == QtCore.Qt.Key_L ):
       modo_leitor()
       return 

   if (e.key() == QtCore.Qt.Key_D ):
       modo_digitacao()   
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



if __name__ == "__main__":
    import sys    
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ui_list.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.txtChave.setFocus()

    Dialog = QtWidgets.QDialog()
    dialog = ui_cnpj_dialog.Ui_Dialog()
    dialog.setupUi(Dialog)
    Dialog.setModal(True)
    
    

    #connect events
    ui.txtChave.textChanged.connect(on_campo_chave_alterado)    
    ui.txtChave.keyPressEvent = txtChave_keyPressEvent
    ui.txtChave_3.keyPressEvent = txtChave_3_keyPressEvent
    ui.btn_limpa_banco.clicked.connect(on_limpa_banco_clickado)    

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
    rows = busca_chaves_banco()
    carrega_lista_chaves(rows)


     #carrega cnpjs na memoria
    rows = busca_cnpj_banco()
    carrega_lista_empresas(rows)


    sys.exit(app.exec_())    
    
    
   
 