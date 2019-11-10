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
        Dialog.resize(884, 281)
        font = QtGui.QFont()
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
        self.grupo_atalhos_2 = QtWidgets.QGroupBox(Dialog)
        self.grupo_atalhos_2.setGeometry(QtCore.QRect(20, 20, 691, 251))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.grupo_atalhos_2.setFont(font)
        self.grupo_atalhos_2.setObjectName("grupo_atalhos_2")
        self.txt_cnpj_padrao = QtWidgets.QPlainTextEdit(self.grupo_atalhos_2)
        self.txt_cnpj_padrao.setGeometry(QtCore.QRect(20, 40, 451, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.txt_cnpj_padrao.setFont(font)
        self.txt_cnpj_padrao.setObjectName("txt_cnpj_padrao")
        self.lbl_message_cnpj_padrao = QtWidgets.QLabel(self.grupo_atalhos_2)
        self.lbl_message_cnpj_padrao.setGeometry(QtCore.QRect(30, 200, 451, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_message_cnpj_padrao.setFont(font)
        self.lbl_message_cnpj_padrao.setText("")
        self.lbl_message_cnpj_padrao.setObjectName("lbl_message_cnpj_padrao")
        self.txt_descricao_entidade = QtWidgets.QPlainTextEdit(self.grupo_atalhos_2)
        self.txt_descricao_entidade.setGeometry(QtCore.QRect(20, 130, 641, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txt_descricao_entidade.setFont(font)
        self.txt_descricao_entidade.setObjectName("txt_descricao_entidade")
        self.lbl_descricao_entidade = QtWidgets.QLabel(self.grupo_atalhos_2)
        self.lbl_descricao_entidade.setGeometry(QtCore.QRect(20, 110, 651, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_descricao_entidade.setFont(font)
        self.lbl_descricao_entidade.setObjectName("lbl_descricao_entidade")
        self.btn_ok = QtWidgets.QPushButton(Dialog)
        self.btn_ok.setGeometry(QtCore.QRect(730, 40, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_ok.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/icons/checked.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_ok.setIcon(icon)
        self.btn_ok.setObjectName("btn_ok")
        self.btn_cancel = QtWidgets.QPushButton(Dialog)
        self.btn_cancel.setGeometry(QtCore.QRect(730, 100, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_cancel.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/icons/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancel.setIcon(icon1)
        self.btn_cancel.setObjectName("btn_cancel")
        self.txt_palavras_chave = QtWidgets.QPlainTextEdit(Dialog)
        self.txt_palavras_chave.setGeometry(QtCore.QRect(920, 200, 461, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txt_palavras_chave.setFont(font)
        self.txt_palavras_chave.setObjectName("txt_palavras_chave")
        self.lbl_palavras_chave = QtWidgets.QLabel(Dialog)
        self.lbl_palavras_chave.setGeometry(QtCore.QRect(920, 170, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_palavras_chave.setFont(font)
        self.lbl_palavras_chave.setObjectName("lbl_palavras_chave")
        self.btn_ok.raise_()
        self.btn_cancel.raise_()
        self.grupo_atalhos_2.raise_()
        self.txt_palavras_chave.raise_()
        self.lbl_palavras_chave.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CNPJ Padrão"))
        self.grupo_atalhos_2.setTitle(_translate("Dialog", "Digite o CNPJ Padrão da Instituição"))
        self.txt_descricao_entidade.setToolTip(_translate("Dialog", "<H2>Este nome deve ser idêntico a descrição da entidade no site da nota fiscal paulista\n"
" </H2>\n"
"<p>\n"
"<img alt=\"entidade\" src=\"assets/entidade.jpg\" />\n"
"</p>"))
        self.lbl_descricao_entidade.setText(_translate("Dialog", "Nome da Entidade (Identico ao que aparece no site da Nota Fiscal Paulista)"))
        self.btn_ok.setText(_translate("Dialog", "Confirmar"))
        self.btn_cancel.setText(_translate("Dialog", "Cancelar"))
        self.txt_palavras_chave.setToolTip(_translate("Dialog", "<H2>Caso não seja possível encontrar a entidade pela descrição, estas palavras-chave ajudarão a encontrar a entidade na lista de entidades no site da Nota Fiscal Paulista </H2>\n"
"<p>\n"
"<img alt=\"entidade\" src=\"assets/entidade.jpg\" />\n"
"</p>"))
        self.lbl_palavras_chave.setText(_translate("Dialog", "Palavras-Chave"))
