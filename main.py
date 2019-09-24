from PyQt5 import QtWidgets
import ui_list
import sys



def createTable(ui):
    ui.tableWidget.setColumnCount(5); 
  
def InitWindow():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ui_list.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    createTable(ui)    
    sys.exit(app.exec_())    
    

if __name__ == "__main__":    
    InitWindow()
    
    
   
 