# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\development\projects\gacc\nfpauto\ui\stats.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import QRect, QSize, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QPlainTextEdit, QGroupBox, QLabel, QLineEdit, QPushButton


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(644, 228)
        font = QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        Dialog.setWindowOpacity(0.95)
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
        self.grupo_atalhos_2 = QGroupBox(Dialog)
        self.grupo_atalhos_2.setGeometry(QRect(20, 20, 451, 191))
        font = QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.grupo_atalhos_2.setFont(font)
        self.grupo_atalhos_2.setObjectName("grupo_atalhos_2")
        self.lbl_desc_hoje = QLabel(self.grupo_atalhos_2)
        self.lbl_desc_hoje.setGeometry(QRect(40, 50, 251, 16))
        font = QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_desc_hoje.setFont(font)
        self.lbl_desc_hoje.setObjectName("lbl_desc_hoje")
        self.lbl_desc_pendentes = QLabel(self.grupo_atalhos_2)
        self.lbl_desc_pendentes.setGeometry(QRect(100, 80, 191, 20))
        font = QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_desc_pendentes.setFont(font)
        self.lbl_desc_pendentes.setObjectName("lbl_desc_pendentes")
        self.lbl_desc_postadas = QLabel(self.grupo_atalhos_2)
        self.lbl_desc_postadas.setGeometry(QRect(150, 120, 151, 16))
        font = QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_desc_postadas.setFont(font)
        self.lbl_desc_postadas.setObjectName("lbl_desc_postadas")
        self.lbl_desc_erro = QLabel(self.grupo_atalhos_2)
        self.lbl_desc_erro.setGeometry(QRect(10, 150, 291, 16))
        font = QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_desc_erro.setFont(font)
        self.lbl_desc_erro.setObjectName("lbl_desc_erro")
        self.lbl_hoje = QLabel(self.grupo_atalhos_2)
        self.lbl_hoje.setGeometry(QRect(300, 50, 81, 16))
        font = QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_hoje.setFont(font)
        self.lbl_hoje.setStyleSheet("color: red;")
        self.lbl_hoje.setObjectName("lbl_hoje")
        self.lbl_pendentes = QLabel(self.grupo_atalhos_2)
        self.lbl_pendentes.setGeometry(QRect(300, 80, 81, 16))
        font = QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_pendentes.setFont(font)
        self.lbl_pendentes.setStyleSheet("color: red;")
        self.lbl_pendentes.setObjectName("lbl_pendentes")
        self.lbl_postadas = QLabel(self.grupo_atalhos_2)
        self.lbl_postadas.setGeometry(QRect(300, 120, 81, 16))
        font = QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_postadas.setFont(font)
        self.lbl_postadas.setStyleSheet("color: red;")
        self.lbl_postadas.setObjectName("lbl_postadas")
        self.lbl_erro = QLabel(self.grupo_atalhos_2)
        self.lbl_erro.setGeometry(QRect(300, 150, 81, 16))
        font = QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_erro.setFont(font)
        self.lbl_erro.setStyleSheet("color: red;")
        self.lbl_erro.setObjectName("lbl_erro")
        self.btn_ok = QPushButton(Dialog)
        self.btn_ok.setGeometry(QRect(480, 30, 141, 41))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_ok.setFont(font)
        icon = QIcon()
        icon.addPixmap(QPixmap("assets/icons/checked.png"), QIcon.Normal, QIcon.Off)
        self.btn_ok.setIcon(icon)
        self.btn_ok.setObjectName("btn_ok")
        self.txt_palavras_chave = QPlainTextEdit(Dialog)
        self.txt_palavras_chave.setGeometry(QRect(920, 200, 461, 61))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txt_palavras_chave.setFont(font)
        self.txt_palavras_chave.setObjectName("txt_palavras_chave")
        self.lbl_palavras_chave = QLabel(Dialog)
        self.lbl_palavras_chave.setGeometry(QRect(920, 170, 161, 16))
        font = QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_palavras_chave.setFont(font)
        self.lbl_palavras_chave.setObjectName("lbl_palavras_chave")
        self.btn_ok.raise_()
        self.grupo_atalhos_2.raise_()
        self.txt_palavras_chave.raise_()
        self.lbl_palavras_chave.raise_()

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Estatísticas"))
        self.grupo_atalhos_2.setTitle(_translate("Dialog", "Estatísticas de Hoje"))
        self.lbl_desc_hoje.setText(_translate("Dialog", "Total de Notas coletadas hoje: "))
        self.lbl_desc_pendentes.setText(_translate("Dialog", "Postagens Pendentes:"))
        self.lbl_desc_postadas.setText(_translate("Dialog", "Postadas no site:"))
        self.lbl_desc_erro.setText(_translate("Dialog", "Tentativas de postagem com erro:"))
        self.lbl_hoje.setText(_translate("Dialog", "[lbl_hoje]"))
        self.lbl_pendentes.setText(_translate("Dialog", "[lbl_pendentes]"))
        self.lbl_postadas.setText(_translate("Dialog", "[lbl_postadas]"))
        self.lbl_erro.setText(_translate("Dialog", "[lbl_erro]"))
        self.btn_ok.setText(_translate("Dialog", "Fechar"))
        self.txt_palavras_chave.setToolTip(_translate("Dialog", "<H2>Caso não seja possível encontrar a entidade pela descrição, estas palavras-chave ajudarão a encontrar a entidade na lista de entidades no site da Nota Fiscal Paulista </H2>\n"
"<p>\n"
"<img alt=\"entidade\" src=\"assets/entidade.jpg\" />\n"
"</p>"))
        self.lbl_palavras_chave.setText(_translate("Dialog", "Palavras-Chave"))
