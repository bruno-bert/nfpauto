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
        Dialog.resize(806, 287)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        self.dialog_buttons = QtWidgets.QDialogButtonBox(Dialog)
        self.dialog_buttons.setGeometry(QtCore.QRect(700, 10, 81, 241))
        self.dialog_buttons.setOrientation(QtCore.Qt.Vertical)
        self.dialog_buttons.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.dialog_buttons.setObjectName("dialog_buttons")
        self.lista_empresas = QtWidgets.QTableWidget(Dialog)
        self.lista_empresas.setEnabled(True)
        self.lista_empresas.setGeometry(QtCore.QRect(10, 10, 661, 271))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lista_empresas.setFont(font)
        self.lista_empresas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.lista_empresas.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.lista_empresas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.lista_empresas.setObjectName("lista_empresas")
        self.lista_empresas.setColumnCount(0)
        self.lista_empresas.setRowCount(0)

        self.retranslateUi(Dialog)
        self.dialog_buttons.accepted.connect(Dialog.accept)
        self.dialog_buttons.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Lista de Empresas Pre Cadastradas"))
