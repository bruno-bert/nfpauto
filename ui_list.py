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
        MainWindow.resize(1737, 751)
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
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 1601, 381))
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
        self.lbl_message = QtWidgets.QLabel(self.centralwidget)
        self.lbl_message.setGeometry(QtCore.QRect(20, 450, 821, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_message.setFont(font)
        self.lbl_message.setAutoFillBackground(False)
        self.lbl_message.setStyleSheet("background-color: rgb(253, 255, 226);")
        self.lbl_message.setText("")
        self.lbl_message.setObjectName("lbl_message")
        self.btn_limpa_banco = QtWidgets.QPushButton(self.centralwidget)
        self.btn_limpa_banco.setGeometry(QtCore.QRect(1460, 20, 151, 31))
        self.btn_limpa_banco.setObjectName("btn_limpa_banco")
        self.grupo_atalhos = QtWidgets.QGroupBox(self.centralwidget)
        self.grupo_atalhos.setGeometry(QtCore.QRect(980, 460, 631, 261))
        self.grupo_atalhos.setObjectName("grupo_atalhos")
        self.lbl_atalho1 = QtWidgets.QLabel(self.grupo_atalhos)
        self.lbl_atalho1.setGeometry(QtCore.QRect(20, 30, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_atalho1.setFont(font)
        self.lbl_atalho1.setObjectName("lbl_atalho1")
        self.lbl_atalho1_2 = QtWidgets.QLabel(self.grupo_atalhos)
        self.lbl_atalho1_2.setGeometry(QtCore.QRect(20, 70, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_atalho1_2.setFont(font)
        self.lbl_atalho1_2.setObjectName("lbl_atalho1_2")
        self.lbl_atalho1_3 = QtWidgets.QLabel(self.grupo_atalhos)
        self.lbl_atalho1_3.setGeometry(QtCore.QRect(20, 110, 591, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_atalho1_3.setFont(font)
        self.lbl_atalho1_3.setObjectName("lbl_atalho1_3")
        self.lbl_atalho1_4 = QtWidgets.QLabel(self.grupo_atalhos)
        self.lbl_atalho1_4.setGeometry(QtCore.QRect(20, 150, 591, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_atalho1_4.setFont(font)
        self.lbl_atalho1_4.setObjectName("lbl_atalho1_4")
        self.lbl_atalho1_5 = QtWidgets.QLabel(self.grupo_atalhos)
        self.lbl_atalho1_5.setGeometry(QtCore.QRect(20, 190, 591, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_atalho1_5.setFont(font)
        self.lbl_atalho1_5.setObjectName("lbl_atalho1_5")
        self.tab_opcao = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_opcao.setGeometry(QtCore.QRect(20, 510, 911, 201))
        self.tab_opcao.setObjectName("tab_opcao")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.grupo_chave_completa = QtWidgets.QGroupBox(self.tab)
        self.grupo_chave_completa.setGeometry(QtCore.QRect(30, 30, 821, 121))
        self.grupo_chave_completa.setObjectName("grupo_chave_completa")
        self.txtChave = QtWidgets.QPlainTextEdit(self.grupo_chave_completa)
        self.txtChave.setGeometry(QtCore.QRect(200, 30, 591, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtChave.setFont(font)
        self.txtChave.setAutoFillBackground(False)
        self.txtChave.setPlainText("")
        self.txtChave.setBackgroundVisible(False)
        self.txtChave.setCenterOnScroll(False)
        self.txtChave.setPlaceholderText("")
        self.txtChave.setObjectName("txtChave")
        self.lblChave = QtWidgets.QLabel(self.grupo_chave_completa)
        self.lblChave.setGeometry(QtCore.QRect(30, 30, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lblChave.setFont(font)
        self.lblChave.setObjectName("lblChave")
        self.lblDigitos = QtWidgets.QLabel(self.grupo_chave_completa)
        self.lblDigitos.setGeometry(QtCore.QRect(200, 70, 311, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lblDigitos.setFont(font)
        self.lblDigitos.setText("")
        self.lblDigitos.setObjectName("lblDigitos")
        self.tab_opcao.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.grupo_chave_completa_2 = QtWidgets.QGroupBox(self.tab_2)
        self.grupo_chave_completa_2.setGeometry(QtCore.QRect(30, 30, 851, 121))
        self.grupo_chave_completa_2.setObjectName("grupo_chave_completa_2")
        self.txtChave_2 = QtWidgets.QPlainTextEdit(self.grupo_chave_completa_2)
        self.txtChave_2.setEnabled(False)
        self.txtChave_2.setGeometry(QtCore.QRect(280, 30, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtChave_2.setFont(font)
        self.txtChave_2.setAutoFillBackground(False)
        self.txtChave_2.setPlainText("")
        self.txtChave_2.setBackgroundVisible(False)
        self.txtChave_2.setCenterOnScroll(False)
        self.txtChave_2.setPlaceholderText("")
        self.txtChave_2.setObjectName("txtChave_2")
        self.lblChave_2 = QtWidgets.QLabel(self.grupo_chave_completa_2)
        self.lblChave_2.setGeometry(QtCore.QRect(30, 30, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lblChave_2.setFont(font)
        self.lblChave_2.setObjectName("lblChave_2")
        self.lblDigitos_2 = QtWidgets.QLabel(self.grupo_chave_completa_2)
        self.lblDigitos_2.setGeometry(QtCore.QRect(200, 70, 311, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lblDigitos_2.setFont(font)
        self.lblDigitos_2.setText("")
        self.lblDigitos_2.setObjectName("lblDigitos_2")
        self.txtChave_3 = QtWidgets.QPlainTextEdit(self.grupo_chave_completa_2)
        self.txtChave_3.setGeometry(QtCore.QRect(620, 30, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtChave_3.setFont(font)
        self.txtChave_3.setAutoFillBackground(False)
        self.txtChave_3.setPlainText("")
        self.txtChave_3.setBackgroundVisible(False)
        self.txtChave_3.setCenterOnScroll(False)
        self.txtChave_3.setPlaceholderText("")
        self.txtChave_3.setObjectName("txtChave_3")
        self.tab_opcao.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.grupo_chave_completa_3 = QtWidgets.QGroupBox(self.tab_3)
        self.grupo_chave_completa_3.setGeometry(QtCore.QRect(20, 20, 821, 121))
        self.grupo_chave_completa_3.setObjectName("grupo_chave_completa_3")
        self.txt_arquivo = QtWidgets.QPlainTextEdit(self.grupo_chave_completa_3)
        self.txt_arquivo.setEnabled(False)
        self.txt_arquivo.setGeometry(QtCore.QRect(10, 30, 591, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txt_arquivo.setFont(font)
        self.txt_arquivo.setAutoFillBackground(False)
        self.txt_arquivo.setPlainText("")
        self.txt_arquivo.setBackgroundVisible(False)
        self.txt_arquivo.setCenterOnScroll(False)
        self.txt_arquivo.setPlaceholderText("")
        self.txt_arquivo.setObjectName("txt_arquivo")
        self.lblDigitos_3 = QtWidgets.QLabel(self.grupo_chave_completa_3)
        self.lblDigitos_3.setGeometry(QtCore.QRect(200, 70, 311, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lblDigitos_3.setFont(font)
        self.lblDigitos_3.setText("")
        self.lblDigitos_3.setObjectName("lblDigitos_3")
        self.btn_arquivo = QtWidgets.QPushButton(self.grupo_chave_completa_3)
        self.btn_arquivo.setGeometry(QtCore.QRect(620, 30, 131, 41))
        self.btn_arquivo.setObjectName("btn_arquivo")
        self.tab_opcao.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.grupo_chave_completa_4 = QtWidgets.QGroupBox(self.tab_4)
        self.grupo_chave_completa_4.setGeometry(QtCore.QRect(20, 20, 821, 121))
        self.grupo_chave_completa_4.setObjectName("grupo_chave_completa_4")
        self.lblDigitos_4 = QtWidgets.QLabel(self.grupo_chave_completa_4)
        self.lblDigitos_4.setGeometry(QtCore.QRect(200, 70, 311, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lblDigitos_4.setFont(font)
        self.lblDigitos_4.setText("")
        self.lblDigitos_4.setObjectName("lblDigitos_4")
        self.btn_portal = QtWidgets.QPushButton(self.grupo_chave_completa_4)
        self.btn_portal.setGeometry(QtCore.QRect(20, 30, 731, 41))
        self.btn_portal.setObjectName("btn_portal")
        self.tab_opcao.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1737, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab_opcao.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbTitulo.setText(_translate("MainWindow", "Lista de Cupons"))
        self.btn_limpa_banco.setText(_translate("MainWindow", "Limpar Banco de Dados"))
        self.grupo_atalhos.setTitle(_translate("MainWindow", "Teclas de Atalhos"))
        self.lbl_atalho1.setText(_translate("MainWindow", "ESC - limpa campo de chave"))
        self.lbl_atalho1_2.setText(_translate("MainWindow", "A - Captura por Leitor de Código de Barras"))
        self.lbl_atalho1_3.setText(_translate("MainWindow", "B - Captura por Digitação da Chave (5 últimos grupos)"))
        self.lbl_atalho1_4.setText(_translate("MainWindow", "C - Importar Arquivo"))
        self.lbl_atalho1_5.setText(_translate("MainWindow", "D - Buscar do Portal Nota do Bem"))
        self.grupo_chave_completa.setTitle(_translate("MainWindow", "Carga Pela Chave Completa"))
        self.txtChave.setToolTip(_translate("MainWindow", "Digite a Chave de Acesso Aqui"))
        self.lblChave.setText(_translate("MainWindow", "Chave de Acesso"))
        self.tab_opcao.setTabText(self.tab_opcao.indexOf(self.tab), _translate("MainWindow", "&Leitor de código de Barras"))
        self.grupo_chave_completa_2.setTitle(_translate("MainWindow", "Digitar 5 ultimos subgrupos"))
        self.txtChave_2.setToolTip(_translate("MainWindow", "Digite a Chave de Acesso Aqui"))
        self.lblChave_2.setText(_translate("MainWindow", "Chave de Acesso (parcial)"))
        self.txtChave_3.setToolTip(_translate("MainWindow", "Digite os ultimos 5 subgrupos da chave aqui"))
        self.tab_opcao.setTabText(self.tab_opcao.indexOf(self.tab_2), _translate("MainWindow", "&Digitar "))
        self.grupo_chave_completa_3.setTitle(_translate("MainWindow", "Buscar Arquivo"))
        self.txt_arquivo.setToolTip(_translate("MainWindow", "Digite a Chave de Acesso Aqui"))
        self.btn_arquivo.setText(_translate("MainWindow", "Buscar Arquivo"))
        self.tab_opcao.setTabText(self.tab_opcao.indexOf(self.tab_3), _translate("MainWindow", "Importar Arquivo"))
        self.grupo_chave_completa_4.setTitle(_translate("MainWindow", "Clique no botão abaixo para buscar chaves de acesso disponíveis no portal do Bem"))
        self.btn_portal.setText(_translate("MainWindow", "Baixar Chaves de Acesso"))
        self.tab_opcao.setTabText(self.tab_opcao.indexOf(self.tab_4), _translate("MainWindow", "Baixar notas do Portal"))
