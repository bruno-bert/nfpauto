# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\development\projects\gacc\nfpauto\dialog_postar.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(887, 772)
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
        self.lista_notas = QtWidgets.QTableWidget(Dialog)
        self.lista_notas.setEnabled(True)
        self.lista_notas.setGeometry(QtCore.QRect(10, 10, 681, 261))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lista_notas.setFont(font)
        self.lista_notas.setStyleSheet("color: rgb(45, 45, 45);")
        self.lista_notas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.lista_notas.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.lista_notas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.lista_notas.setGridStyle(QtCore.Qt.SolidLine)
        self.lista_notas.setObjectName("lista_notas")
        self.lista_notas.setColumnCount(0)
        self.lista_notas.setRowCount(0)
        self.lista_notas.horizontalHeader().setStretchLastSection(False)
        self.grupo_atalhos = QtWidgets.QGroupBox(Dialog)
        self.grupo_atalhos.setGeometry(QtCore.QRect(710, 150, 171, 91))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.grupo_atalhos.setFont(font)
        self.grupo_atalhos.setStyleSheet("color: rgb(45, 45, 45);")
        self.grupo_atalhos.setObjectName("grupo_atalhos")
        self.lbl_atalho1 = QtWidgets.QLabel(self.grupo_atalhos)
        self.lbl_atalho1.setGeometry(QtCore.QRect(40, 30, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_atalho1.setFont(font)
        self.lbl_atalho1.setObjectName("lbl_atalho1")
        self.btn_iniciar_postagem = QtWidgets.QPushButton(Dialog)
        self.btn_iniciar_postagem.setGeometry(QtCore.QRect(700, 10, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_iniciar_postagem.setFont(font)
        self.btn_iniciar_postagem.setStyleSheet("color: rgb(45, 45, 45);")
        self.btn_iniciar_postagem.setObjectName("btn_iniciar_postagem")
        self.btn_fechar = QtWidgets.QPushButton(Dialog)
        self.btn_fechar.setGeometry(QtCore.QRect(700, 70, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_fechar.setFont(font)
        self.btn_fechar.setStyleSheet("color: rgb(45, 45, 45);")
        self.btn_fechar.setObjectName("btn_fechar")
        self.label_log = QtWidgets.QLabel(Dialog)
        self.label_log.setGeometry(QtCore.QRect(10, 290, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_log.setFont(font)
        self.label_log.setStyleSheet("color: rgb(45, 45, 45);")
        self.label_log.setObjectName("label_log")
        self.list_log = QtWidgets.QListView(Dialog)
        self.list_log.setGeometry(QtCore.QRect(10, 330, 861, 431))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.list_log.setFont(font)
        self.list_log.setStyleSheet("color: rgb(45, 45, 45);")
        self.list_log.setObjectName("list_log")
        self.btn_limpar = QtWidgets.QPushButton(Dialog)
        self.btn_limpar.setGeometry(QtCore.QRect(640, 290, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_limpar.setFont(font)
        self.btn_limpar.setStyleSheet("color: rgb(45, 45, 45);")
        self.btn_limpar.setObjectName("btn_limpar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Notas fiscais a serem postadas"))
        self.grupo_atalhos.setTitle(_translate("Dialog", "Teclas de Atalhos"))
        self.lbl_atalho1.setStyleSheet(_translate("Dialog", "color: rgb(45, 45, 45);"))
        self.lbl_atalho1.setText(_translate("Dialog", "ESC - Sair"))
        self.btn_iniciar_postagem.setText(_translate("Dialog", "Iniciar Postagem"))
        self.btn_fechar.setText(_translate("Dialog", "Fechar"))
        self.label_log.setText(_translate("Dialog", "Log de Atividades"))
        self.btn_limpar.setText(_translate("Dialog", "Limpar Log"))
