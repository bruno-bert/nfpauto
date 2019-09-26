from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTableWidgetItem

import constant
import sqlite3

#ui
import ui_list

def carrega_chaves():
 conn = sqlite3.connect('notas.db')
 query = "select * from notas"
 result = conn.execute(query)
 
 ui.tableWidget.setRowCount(0) 
 

 for row_num, row_data in enumerate(result):
     ui.tableWidget.insertRow(row_num)
     for col_num, data in enumerate(row_data):
           ui.tableWidget.setItem(row_num, col_num, QTableWidgetItem(str(data)))

 conn.close()




def cria_tabela():
    ui.tableWidget.setColumnCount(6)
    ui.tableWidget.setRowCount(1)
 
    ui.tableWidget.setItem(0, 0, QTableWidgetItem("ID"))
    ui.tableWidget.setItem(0, 1, QTableWidgetItem("Chave de Acesso"))
    ui.tableWidget.setItem(0, 2, QTableWidgetItem("CNPJ"))
    ui.tableWidget.setItem(0, 3, QTableWidgetItem("Valor Total"))
    ui.tableWidget.setItem(0, 4, QTableWidgetItem("Data de Emissão"))
    ui.tableWidget.setItem(0, 5, QTableWidgetItem("Status"))
    
    carrega_chaves()

def limpa_campo_chave():
    ui.txtChave.setPlainText(constant.EMPTY_STR)   

def adiciona_chave_na_lista(text):
    ui.tableWidget.insertRow(0)
    ui.tableWidget.setItem(0, 1, QTableWidgetItem(text) )
    ui.tableWidget.setItem(0, 5, QTableWidgetItem(constant.DEFAULT_STATUS) )

def valida_chave(chave): 
    if (len(get_chave()) == constant.NUM_CHAVE):
        return True
    else:
        return False    

def get_chave():
    return ui.txtChave.toPlainText()

def on_campo_chave_alterado():
    text = get_chave()
    
    ui.lblDigitos.setText("{n} dígitos".format(n=len(text)))

    if (len(text) >= constant.NUM_CHAVE ):
       salva_chave(text)
       adiciona_chave_na_lista(text)
       limpa_campo_chave()

def salva_chave(chave):
    conn = sqlite3.connect('notas.db')
    cursor = conn.cursor()
    cursor.execute(constant.QUERY_SAVE,  (chave, constant.DEFAULT_STATUS) )
    conn.commit()
    conn.close()

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
    cria_tabela()    
    sys.exit(app.exec_())    
    
    
   
 