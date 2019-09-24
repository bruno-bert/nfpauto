from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import ui_list
import sys



def createTable(self):
    self.tableWidget.setColumnCount(6); 
    self.tableWidget.setRowCount(2); 
 
    self.tableWidget.setItem(0, 0, QTableWidgetItem("ID"))
    self.tableWidget.setItem(0, 1, QTableWidgetItem("Chave de Acesso"))
    self.tableWidget.setItem(0, 2, QTableWidgetItem("CNPJ"))
    self.tableWidget.setItem(0, 3, QTableWidgetItem("Valor Total"))
    self.tableWidget.setItem(0, 4, QTableWidgetItem("Data de Emissão"))
    self.tableWidget.setItem(0, 5, QTableWidgetItem("Status"))
 
    self.tableWidget.setItem(1, 0, QTableWidgetItem("1"))
    self.tableWidget.setItem(1, 1, QTableWidgetItem("2222 3333 4444 5555 6666 7777 8888 9999 0000"))
    self.tableWidget.setItem(1, 2, QTableWidgetItem(""))
    self.tableWidget.setItem(1, 3, QTableWidgetItem(""))
    self.tableWidget.setItem(1, 4, QTableWidgetItem(""))
    self.tableWidget.setItem(1, 5, QTableWidgetItem("Pendente"))
    
   
def InitWindow():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ui_list.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    createTable(ui)    
    sys.exit(app.exec_())    
    

if __name__ == "__main__":    
    InitWindow()
    
    
   
 