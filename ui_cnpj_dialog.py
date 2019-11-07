# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\development\projects\gacc\nfpauto\cnpj_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(821, 466)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        Dialog.setStyleSheet("QPushButton {\n"
"    box-shadow:inset 0px 1px 0px 0px #ffffff;\n"
"    background:linear-gradient(to bottom, #f9f9f9 5%, #e9e9e9 100%);\n"
"    background-color:#f9f9f9;\n"
"    border-radius:6px;\n"
"    border:1px solid #dcdcdc;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#666666;\n"
"    font-family:Arial;\n"
"    font-size:15px;\n"
"    font-weight:bold;\n"
"    padding:6px 24px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px 1px 0px #ffffff;\n"
"}\n"
"QPushButton:hover {\n"
"  background:linear-gradient(to bottom, #e9e9e9 5%, #f9f9f9 100%);\n"
"    background-color:#e9e9e9;\n"
"}\n"
"QPushButton:active {\n"
"  position:relative;\n"
"    top:1px;\n"
"}")
        self.dialog_buttons = QtWidgets.QDialogButtonBox(Dialog)
        self.dialog_buttons.setGeometry(QtCore.QRect(710, 10, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.dialog_buttons.setFont(font)
        self.dialog_buttons.setOrientation(QtCore.Qt.Vertical)
        self.dialog_buttons.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.dialog_buttons.setCenterButtons(False)
        self.dialog_buttons.setObjectName("dialog_buttons")
        self.lista_empresas = QtWidgets.QTableWidget(Dialog)
        self.lista_empresas.setEnabled(True)
        self.lista_empresas.setGeometry(QtCore.QRect(10, 10, 691, 271))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        self.lista_empresas.setFont(font)
        self.lista_empresas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.lista_empresas.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.lista_empresas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.lista_empresas.setObjectName("lista_empresas")
        self.lista_empresas.setColumnCount(0)
        self.lista_empresas.setRowCount(0)
        self.lista_empresas.verticalHeader().setVisible(False)
        self.grupo_atalhos = QtWidgets.QGroupBox(Dialog)
        self.grupo_atalhos.setGeometry(QtCore.QRect(10, 290, 471, 151))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.grupo_atalhos.setFont(font)
        self.grupo_atalhos.setObjectName("grupo_atalhos")
        self.lbl_atalho1 = QtWidgets.QLabel(self.grupo_atalhos)
        self.lbl_atalho1.setGeometry(QtCore.QRect(30, 100, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_atalho1.setFont(font)
        self.lbl_atalho1.setObjectName("lbl_atalho1")
        self.lbl_atalho1_3 = QtWidgets.QLabel(self.grupo_atalhos)
        self.lbl_atalho1_3.setGeometry(QtCore.QRect(30, 60, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_atalho1_3.setFont(font)
        self.lbl_atalho1_3.setObjectName("lbl_atalho1_3")
        self.lbl_atalho1_4 = QtWidgets.QLabel(self.grupo_atalhos)
        self.lbl_atalho1_4.setGeometry(QtCore.QRect(30, 20, 481, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_atalho1_4.setFont(font)
        self.lbl_atalho1_4.setObjectName("lbl_atalho1_4")
        self.grupo_atalhos_2 = QtWidgets.QGroupBox(Dialog)
        self.grupo_atalhos_2.setGeometry(QtCore.QRect(500, 290, 301, 151))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.grupo_atalhos_2.setFont(font)
        self.grupo_atalhos_2.setObjectName("grupo_atalhos_2")
        self.lbl_mes_atual = QtWidgets.QLabel(self.grupo_atalhos_2)
        self.lbl_mes_atual.setGeometry(QtCore.QRect(20, 80, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_mes_atual.setFont(font)
        self.lbl_mes_atual.setStyleSheet("")
        self.lbl_mes_atual.setWordWrap(True)
        self.lbl_mes_atual.setObjectName("lbl_mes_atual")
        self.lbl_mes = QtWidgets.QLabel(self.grupo_atalhos_2)
        self.lbl_mes.setGeometry(QtCore.QRect(10, 30, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_mes.setFont(font)
        self.lbl_mes.setStyleSheet("")
        self.lbl_mes.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_mes.setObjectName("lbl_mes")

        self.retranslateUi(Dialog)
        self.dialog_buttons.accepted.connect(Dialog.accept)
        self.dialog_buttons.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Lista de Empresas Pre Cadastradas"))
        self.grupo_atalhos.setTitle(_translate("Dialog", "Teclas de Atalhos"))
        self.lbl_atalho1.setText(_translate("Dialog", "ESC - Sair"))
        self.lbl_atalho1_3.setText(_translate("Dialog", "ENTER - Confirmar Estabelecimento"))
        self.lbl_atalho1_4.setText(_translate("Dialog", "Setas para Cima / Baixo - Selecionar Estabelecimento"))
        self.grupo_atalhos_2.setTitle(_translate("Dialog", "Qual mês e ano da nota?"))
        self.lbl_mes_atual.setText(_translate("Dialog", "Pressione a tecla ESPAÇO no teclado para trocar o mês da nota"))
        self.lbl_mes.setText(_translate("Dialog", "Mes Nota"))
