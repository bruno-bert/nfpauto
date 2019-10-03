# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\development\projects\gacc\nfpauto\login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(391, 279)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        self.grupo_login = QtWidgets.QGroupBox(Dialog)
        self.grupo_login.setGeometry(QtCore.QRect(20, 20, 351, 241))
        self.grupo_login.setObjectName("grupo_login")
        self.lbl_message_login = QtWidgets.QLabel(self.grupo_login)
        self.lbl_message_login.setGeometry(QtCore.QRect(30, 200, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_message_login.setFont(font)
        self.lbl_message_login.setStyleSheet("color: rgb(255, 0, 0);")
        self.lbl_message_login.setObjectName("lbl_message_login")
        self.lbl_message_login_2 = QtWidgets.QLabel(self.grupo_login)
        self.lbl_message_login_2.setGeometry(QtCore.QRect(30, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_message_login_2.setFont(font)
        self.lbl_message_login_2.setObjectName("lbl_message_login_2")
        self.lbl_message_login_3 = QtWidgets.QLabel(self.grupo_login)
        self.lbl_message_login_3.setGeometry(QtCore.QRect(30, 100, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_message_login_3.setFont(font)
        self.lbl_message_login_3.setObjectName("lbl_message_login_3")
        self.txt_usuario = QtWidgets.QLineEdit(self.grupo_login)
        self.txt_usuario.setGeometry(QtCore.QRect(100, 39, 231, 31))
        self.txt_usuario.setObjectName("txt_usuario")
        self.txt_password = QtWidgets.QLineEdit(self.grupo_login)
        self.txt_password.setGeometry(QtCore.QRect(100, 100, 231, 31))
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_password.setObjectName("txt_password")
        self.btn_login = QtWidgets.QPushButton(self.grupo_login)
        self.btn_login.setGeometry(QtCore.QRect(40, 160, 131, 23))
        self.btn_login.setObjectName("btn_login")
        self.btn_cancel = QtWidgets.QPushButton(self.grupo_login)
        self.btn_cancel.setGeometry(QtCore.QRect(200, 160, 131, 23))
        self.btn_cancel.setObjectName("btn_cancel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.grupo_login.setTitle(_translate("Dialog", "Login"))
        self.lbl_message_login.setText(_translate("Dialog", "[message]"))
        self.lbl_message_login_2.setText(_translate("Dialog", "Usuário"))
        self.lbl_message_login_3.setText(_translate("Dialog", "Senha"))
        self.txt_usuario.setPlaceholderText(_translate("Dialog", "Digite seu usuário"))
        self.txt_password.setPlaceholderText(_translate("Dialog", "Digite sua senha"))
        self.btn_login.setText(_translate("Dialog", "Confirmar"))
        self.btn_cancel.setText(_translate("Dialog", "Sair"))
