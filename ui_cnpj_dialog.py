# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\development\projects\gacc\nfpauto\cnpj_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt, QRect, QSize, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QLabel, QPlainTextEdit, QAbstractItemView, QTableWidget, QGroupBox,  QPushButton, QDialogButtonBox


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(821, 466)
        font = QFont()
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
        self.dialog_buttons = QDialogButtonBox(Dialog)
        self.dialog_buttons.setGeometry(QRect(710, 10, 101, 61))
        font = QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.dialog_buttons.setFont(font)
        self.dialog_buttons.setOrientation(Qt.Vertical)
        self.dialog_buttons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.dialog_buttons.setCenterButtons(False)
        self.dialog_buttons.setObjectName("dialog_buttons")
        self.lista_empresas = QTableWidget(Dialog)
        self.lista_empresas.setEnabled(True)
        self.lista_empresas.setGeometry(QRect(10, 10, 691, 271))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        self.lista_empresas.setFont(font)
        self.lista_empresas.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.lista_empresas.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.lista_empresas.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.lista_empresas.setObjectName("lista_empresas")
        self.lista_empresas.setColumnCount(0)
        self.lista_empresas.setRowCount(0)
        self.lista_empresas.verticalHeader().setVisible(False)
        self.grupo_atalhos = QGroupBox(Dialog)
        self.grupo_atalhos.setGeometry(QRect(10, 290, 471, 151))
        font = QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.grupo_atalhos.setFont(font)
        self.grupo_atalhos.setObjectName("grupo_atalhos")
        self.lbl_atalho1 = QLabel(self.grupo_atalhos)
        self.lbl_atalho1.setGeometry(QRect(30, 100, 211, 41))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_atalho1.setFont(font)
        self.lbl_atalho1.setObjectName("lbl_atalho1")
        self.lbl_atalho1_3 = QLabel(self.grupo_atalhos)
        self.lbl_atalho1_3.setGeometry(QRect(30, 60, 411, 41))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_atalho1_3.setFont(font)
        self.lbl_atalho1_3.setObjectName("lbl_atalho1_3")
        self.lbl_atalho1_4 = QLabel(self.grupo_atalhos)
        self.lbl_atalho1_4.setGeometry(QRect(30, 20, 481, 41))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_atalho1_4.setFont(font)
        self.lbl_atalho1_4.setObjectName("lbl_atalho1_4")
        self.grupo_atalhos_2 = QGroupBox(Dialog)
        self.grupo_atalhos_2.setGeometry(QRect(500, 290, 301, 151))
        font = QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.grupo_atalhos_2.setFont(font)
        self.grupo_atalhos_2.setObjectName("grupo_atalhos_2")
        self.lbl_mes_atual = QLabel(self.grupo_atalhos_2)
        self.lbl_mes_atual.setGeometry(QRect(20, 80, 271, 41))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_mes_atual.setFont(font)
        self.lbl_mes_atual.setStyleSheet("")
        self.lbl_mes_atual.setWordWrap(True)
        self.lbl_mes_atual.setObjectName("lbl_mes_atual")
        self.lbl_mes = QLabel(self.grupo_atalhos_2)
        self.lbl_mes.setGeometry(QRect(10, 30, 271, 41))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_mes.setFont(font)
        self.lbl_mes.setStyleSheet("")
        self.lbl_mes.setAlignment(Qt.AlignCenter)
        self.lbl_mes.setObjectName("lbl_mes")

        self.retranslateUi(Dialog)
        self.dialog_buttons.accepted.connect(Dialog.accept)
        self.dialog_buttons.rejected.connect(Dialog.reject)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Lista de Empresas Pre Cadastradas"))
        self.grupo_atalhos.setTitle(_translate("Dialog", "Teclas de Atalhos"))
        self.lbl_atalho1.setText(_translate("Dialog", "ESC - Sair"))
        self.lbl_atalho1_3.setText(_translate("Dialog", "ENTER - Confirmar Estabelecimento"))
        self.lbl_atalho1_4.setText(_translate("Dialog", "Setas para Cima / Baixo - Selecionar Estabelecimento"))
        self.grupo_atalhos_2.setTitle(_translate("Dialog", "Qual mês e ano da nota?"))
        self.lbl_mes_atual.setText(_translate("Dialog", "Pressione a tecla ESPAÇO no teclado para trocar o mês da nota"))
        self.lbl_mes.setText(_translate("Dialog", "Mes Nota"))
