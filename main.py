from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTableWidgetItem

import constant
import sqlite3
from nota import Nota
from messages import Messages
 
#ui
import ui_list

def carrega_chaves_banco():
 conn = sqlite3.connect('notas.db')
 query = "select * from notas"
 conn.row_factory = sqlite3.Row
 cur = conn.cursor()
 cur.execute(query)

 rows = cur.fetchall()
 
 ui.tableWidget.setRowCount(0) 

 for row_num, row_data in enumerate(rows):
    row = dict(row_data)
    ui.tableWidget.insertRow(row_num)
    ui.tableWidget.setItem(row_num, 0, QTableWidgetItem(row['id'])) 
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
   
 conn.close()


def cria_tabela():
    ui.tableWidget.setColumnCount(11)
    ui.tableWidget.setRowCount(1)
 
    ui.tableWidget.setHorizontalHeaderLabels(
                                      ['ID', 'Chave', 
                                       'CNPJ', 
                                       'Data', 'Status', 
                                       'UF', 'Numero', 
                                       'Codigo', 'Modelo', 
                                       'Serie', 'Tipo Emissao'])


    carrega_chaves_banco()

def limpa_campo_chave():
    ui.txtChave.setPlainText(constant.EMPTY_STR)   

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
      print("Erro ao tentar separar dados da nota pela chave de acesso")
  
    return new_nota

def adiciona_chave_na_lista(new_nota):

    ui.tableWidget.insertRow(0)
    ui.tableWidget.setItem(0, 1, QTableWidgetItem(new_nota.chave) )
    ui.tableWidget.setItem(0, 2, QTableWidgetItem(new_nota.cnpj) )
    ui.tableWidget.setItem(0, 3, QTableWidgetItem(new_nota.data) )
    ui.tableWidget.setItem(0, 4, QTableWidgetItem(constant.DEFAULT_STATUS) )
    ui.tableWidget.setItem(0, 5, QTableWidgetItem(new_nota.uf) )
    ui.tableWidget.setItem(0, 6, QTableWidgetItem(new_nota.numero) )
    ui.tableWidget.setItem(0, 7, QTableWidgetItem(new_nota.codigo) )
    ui.tableWidget.setItem(0, 8, QTableWidgetItem(new_nota.modelo) )
    ui.tableWidget.setItem(0, 9, QTableWidgetItem(new_nota.serie) )
    ui.tableWidget.setItem(0, 10, QTableWidgetItem(new_nota.tipo_emissao) )

def valida_chave_pelo_digito(chave):
    return True

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
                     constant.DEFAULT_STATUS) )
    conn.commit()
    conn.close()
def mostra_mensagem(text):
    ui.lbl_message.setText(text)

def atualiza_contagem_digitos(text):
    ui.lblDigitos.setText("{num_digitos} dígitos".format(num_digitos=len(text)))

def on_campo_chave_alterado():
    text = get_chave()
    atualiza_contagem_digitos(text)

    if (len(text) >= constant.NUM_CHAVE ):
       chave_ok = valida_chave(get_chave())    
       if (chave_ok): 
         nota_separada = separa_campos_pela_chave(text)     
         salva_chave_banco(nota_separada)
         adiciona_chave_na_lista(nota_separada)
       else:
         mostra_mensagem(m.chave_invalida)
             
       limpa_campo_chave()
        



def keyPressEvent(e):
   if (e.key() == QtCore.Qt.Key_Return or  e.key() == QtCore.Qt.Key_Enter ):
        chave_ok = valida_chave(get_chave())     
        if (chave_ok):
            print('chave ok')
        else:
            print('chave nao ok')
   else: 
       return QtWidgets.QTextEdit.keyPressEvent(ui.txtChave, e)


if __name__ == "__main__":
    import sys    
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ui_list.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    ui.txtChave.setFocus()
    ui.txtChave.textChanged.connect(on_campo_chave_alterado)    
    ui.txtChave.keyPressEvent = keyPressEvent

    m = Messages()

    cria_tabela()    
    sys.exit(app.exec_())    
    
    
   
 