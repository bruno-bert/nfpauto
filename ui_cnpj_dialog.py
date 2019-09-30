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
        Dialog.resize(801, 466)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        self.dialog_buttons = QtWidgets.QDialogButtonBox(Dialog)
        self.dialog_buttons.setGeometry(QtCore.QRect(700, 10, 81, 61))
        self.dialog_buttons.setOrientation(QtCore.Qt.Vertical)
        self.dialog_buttons.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.dialog_buttons.setObjectName("dialog_buttons")
        self.lista_empresas = QtWidgets.QTableWidget(Dialog)
        self.lista_empresas.setEnabled(True)
        self.lista_empresas.setGeometry(QtCore.QRect(10, 10, 671, 271))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lista_empresas.setFont(font)
        self.lista_empresas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.lista_empresas.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.lista_empresas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.lista_empresas.setObjectName("lista_empresas")
        self.lista_empresas.setColumnCount(0)
        self.lista_empresas.setRowCount(0)
        self.grupo_atalhos = QtWidgets.QGroupBox(Dialog)
        self.grupo_atalhos.setGeometry(QtCore.QRect(20, 290, 371, 151))
        self.grupo_atalhos.setObjectName("grupo_atalhos")
        self.lbl_atalho1 = QtWidgets.QLabel(self.grupo_atalhos)
        self.lbl_atalho1.setGeometry(QtCore.QRect(30, 100, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_atalho1.setFont(font)
        self.lbl_atalho1.setObjectName("lbl_atalho1")
        self.lbl_atalho1_3 = QtWidgets.QLabel(self.grupo_atalhos)
        self.lbl_atalho1_3.setGeometry(QtCore.QRect(30, 60, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_atalho1_3.setFont(font)
        self.lbl_atalho1_3.setObjectName("lbl_atalho1_3")
        self.lbl_atalho1_4 = QtWidgets.QLabel(self.grupo_atalhos)
        self.lbl_atalho1_4.setGeometry(QtCore.QRect(30, 20, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_atalho1_4.setFont(font)
        self.lbl_atalho1_4.setObjectName("lbl_atalho1_4")

        self.retranslateUi(Dialog)
        self.dialog_buttons.accepted.connect(Dialog.accept)
        self.dialog_buttons.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Lista de Empresas Pre Cadastradas"))
        self.grupo_atalhos.setTitle(_translate("Dialog", "Teclas de Atalhos"))
        self.lbl_atalho1.setText(_translate("Dialog", "ESC - Sair"))
        self.lbl_atalho1_3.setText(_translate("Dialog", "ENTER - Confirmar estabelecimento"))
        self.lbl_atalho1_4.setText(_translate("Dialog", "Setas para Cima / Baixo - selecionar estabelecimento"))
