# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\development\projects\gacc\nfpauto\list.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(775, 571)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbTitulo = QtWidgets.QLabel(self.centralwidget)
        self.lbTitulo.setGeometry(QtCore.QRect(230, 10, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lbTitulo.setFont(font)
        self.lbTitulo.setObjectName("lbTitulo")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 751, 381))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.txtChave = QtWidgets.QTextEdit(self.centralwidget)
        self.txtChave.setGeometry(QtCore.QRect(180, 450, 581, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(14)
        self.txtChave.setFont(font)
        self.txtChave.setTabChangesFocus(False)
        self.txtChave.setObjectName("txtChave")
        self.lblChave = QtWidgets.QLabel(self.centralwidget)
        self.lblChave.setGeometry(QtCore.QRect(10, 450, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lblChave.setFont(font)
        self.lblChave.setObjectName("lblChave")
        self.lblDigitos = QtWidgets.QLabel(self.centralwidget)
        self.lblDigitos.setGeometry(QtCore.QRect(180, 501, 311, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lblDigitos.setFont(font)
        self.lblDigitos.setText("")
        self.lblDigitos.setObjectName("lblDigitos")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 775, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbTitulo.setText(_translate("MainWindow", "Lista de Cupons"))
        self.lblChave.setText(_translate("MainWindow", "Chave de Acesso"))
