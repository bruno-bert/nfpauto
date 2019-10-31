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
        Dialog.resize(871, 772)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        self.lista_notas = QtWidgets.QTableWidget(Dialog)
        self.lista_notas.setEnabled(True)
        self.lista_notas.setGeometry(QtCore.QRect(10, 10, 591, 261))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lista_notas.setFont(font)
        self.lista_notas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.lista_notas.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.lista_notas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.lista_notas.setObjectName("lista_notas")
        self.lista_notas.setColumnCount(0)
        self.lista_notas.setRowCount(0)
        self.grupo_atalhos = QtWidgets.QGroupBox(Dialog)
        self.grupo_atalhos.setGeometry(QtCore.QRect(720, 670, 131, 91))
        self.grupo_atalhos.setObjectName("grupo_atalhos")
        self.lbl_atalho1 = QtWidgets.QLabel(self.grupo_atalhos)
        self.lbl_atalho1.setGeometry(QtCore.QRect(10, 30, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_atalho1.setFont(font)
        self.lbl_atalho1.setObjectName("lbl_atalho1")
        self.btn_iniciar_postagem = QtWidgets.QPushButton(Dialog)
        self.btn_iniciar_postagem.setGeometry(QtCore.QRect(730, 12, 131, 51))
        self.btn_iniciar_postagem.setObjectName("btn_iniciar_postagem")
        self.btn_fechar = QtWidgets.QPushButton(Dialog)
        self.btn_fechar.setGeometry(QtCore.QRect(730, 80, 131, 51))
        self.btn_fechar.setObjectName("btn_fechar")
        self.label_log = QtWidgets.QLabel(Dialog)
        self.label_log.setGeometry(QtCore.QRect(10, 290, 581, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_log.setFont(font)
        self.label_log.setObjectName("label_log")
        self.list_log = QtWidgets.QListView(Dialog)
        self.list_log.setGeometry(QtCore.QRect(10, 330, 701, 431))
        self.list_log.setObjectName("list_log")
        self.btn_limpar = QtWidgets.QPushButton(Dialog)
        self.btn_limpar.setGeometry(QtCore.QRect(580, 300, 131, 31))
        self.btn_limpar.setObjectName("btn_limpar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Notas fiscais a serem postadas"))
        self.grupo_atalhos.setTitle(_translate("Dialog", "Teclas de Atalhos"))
        self.lbl_atalho1.setText(_translate("Dialog", "ESC - Sair"))
        self.btn_iniciar_postagem.setText(_translate("Dialog", "Iniciar Postagem"))
        self.btn_fechar.setText(_translate("Dialog", "Fechar"))
        self.label_log.setText(_translate("Dialog", "Log de Atividades"))
        self.btn_limpar.setText(_translate("Dialog", "Limpar Log"))
