# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\development\projects\gacc\nfpauto\cnpj_padrao_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(659, 164)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        self.grupo_atalhos_2 = QtWidgets.QGroupBox(Dialog)
        self.grupo_atalhos_2.setGeometry(QtCore.QRect(20, 20, 511, 131))
        self.grupo_atalhos_2.setObjectName("grupo_atalhos_2")
        self.txt_cnpj_padrao = QtWidgets.QPlainTextEdit(self.grupo_atalhos_2)
        self.txt_cnpj_padrao.setGeometry(QtCore.QRect(30, 30, 441, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.txt_cnpj_padrao.setFont(font)
        self.txt_cnpj_padrao.setObjectName("txt_cnpj_padrao")
        self.lbl_message_cnpj_padrao = QtWidgets.QLabel(self.grupo_atalhos_2)
        self.lbl_message_cnpj_padrao.setGeometry(QtCore.QRect(30, 100, 331, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_message_cnpj_padrao.setFont(font)
        self.lbl_message_cnpj_padrao.setText("")
        self.lbl_message_cnpj_padrao.setObjectName("lbl_message_cnpj_padrao")
        self.btn_ok = QtWidgets.QPushButton(Dialog)
        self.btn_ok.setGeometry(QtCore.QRect(550, 30, 75, 23))
        self.btn_ok.setObjectName("btn_ok")
        self.btn_cancel = QtWidgets.QPushButton(Dialog)
        self.btn_cancel.setGeometry(QtCore.QRect(550, 60, 75, 23))
        self.btn_cancel.setObjectName("btn_cancel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CNPJ Padrão"))
        self.grupo_atalhos_2.setTitle(_translate("Dialog", "Digite o CNPJ Padrão da Instituição"))
        self.btn_ok.setText(_translate("Dialog", "OK"))
        self.btn_cancel.setText(_translate("Dialog", "Cancelar"))
