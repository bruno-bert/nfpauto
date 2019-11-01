# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\development\projects\gacc\nfpauto\list.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1630, 788)
        MainWindow.setStyleSheet("#centralwidget {\n"
" background-color: #fffafa\n"
"}\n"
"\n"
"QPushButton {\n"
"    box-shadow:inset 0px 1px 0px 0px #dcecfb;\n"
"    background:linear-gradient(to bottom, #bddbfa 5%, #80b5ea 100%);\n"
"    background-color:#bddbfa;\n"
"    border-radius:6px;\n"
"    border:1px solid #84bbf3;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#555;\n"
"    font-family:Arial;\n"
"    font-size:15px;\n"
"    font-weight:bold;\n"
"    padding:6px 24px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px 1px 0px #528ecc;\n"
"}\n"
"QPushButton:hover {\n"
"    background:linear-gradient(to bottom, #80b5ea 5%, #bddbfa 100%);\n"
"    background-color:#80b5ea;\n"
"}\n"
"QPushButton:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"}\n"
"\n"
"\n"
"#btn_postar {\n"
"    box-shadow: 0px 1px 0px 0px #f0f7fa;\n"
"    background:linear-gradient(to bottom, #33bdef 5%, #019ad2 100%);\n"
"    background-color:#33bdef;\n"
"    border-radius:6px;\n"
"    border:1px solid #057fd0;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#ffffff;\n"
"    font-family: Arial;\n"
"    font-size:15px;\n"
"    font-weight:bold;\n"
"    padding:6px 24px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px -1px 0px #5b6178;\n"
"}\n"
"#btn_postar:hover {\n"
"    background:linear-gradient(to bottom, #019ad2 5%, #33bdef 100%);\n"
"    background-color:#019ad2;\n"
"}\n"
"#btn_postar:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"}\n"
"\n"
"\n"
"QPlainTextEdit, QLineEdit\n"
"{\n"
"    -webkit-transition: all 0.30s ease-in-out;\n"
"    -moz-transition: all 0.30s ease-in-out;\n"
"    -ms-transition: all 0.30s ease-in-out;\n"
"    -o-transition: all 0.30s ease-in-out;\n"
"    outline: none;\n"
"    box-sizing: border-box;\n"
"    -webkit-box-sizing: border-box;\n"
"    -moz-box-sizing: border-box;\n"
"    width: 100%;\n"
"    background: #fff;\n"
"    margin-bottom: 4%;\n"
"    border: 1px solid #ccc;\n"
"    padding: 8%;\n"
"    color: #555;\n"
"    font: 95% Arial, Helvetica, sans-serif;\n"
"}\n"
"\n"
"QPlainTextEdit:focus, QLineEdit:focus\n"
"{\n"
"    box-shadow: 0 0 5px #84bbf3;\n"
"    padding: 3%;\n"
"    border: 2px solid #84bbf3;\n"
"}\n"
"\n"
"#txt_chave:focus{\n"
"    box-shadow: 0 0 5px #84bbf3;\n"
"    padding: 3%;\n"
"    border: 2px solid #84bbf3;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbTitulo = QtWidgets.QLabel(self.centralwidget)
        self.lbTitulo.setGeometry(QtCore.QRect(630, 30, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbTitulo.setFont(font)
        self.lbTitulo.setObjectName("lbTitulo")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 1601, 251))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.lbl_message = QtWidgets.QLabel(self.centralwidget)
        self.lbl_message.setGeometry(QtCore.QRect(20, 700, 921, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_message.setFont(font)
        self.lbl_message.setAutoFillBackground(False)
        self.lbl_message.setStyleSheet("#lbl_message {\n"
"margin: 10px 0px;\n"
"padding:12px;\n"
" \n"
"}\n"
"#lbl_message {\n"
"    color: #9F6000;\n"
"    background-color: #ffffcc;\n"
"  margin:10px 22px;\n"
"    font-size:2em;\n"
"    vertical-align:middle;\n"
"border-style: dashed\n"
"}")
        self.lbl_message.setText("")
        self.lbl_message.setObjectName("lbl_message")
        self.grupo_atalhos = QtWidgets.QGroupBox(self.centralwidget)
        self.grupo_atalhos.setGeometry(QtCore.QRect(980, 350, 631, 351))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.grupo_atalhos.setFont(font)
        self.grupo_atalhos.setObjectName("grupo_atalhos")
        self.lbl_atalho1 = QtWidgets.QLabel(self.grupo_atalhos)
        self.lbl_atalho1.setGeometry(QtCore.QRect(20, 30, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_atalho1.setFont(font)
        self.lbl_atalho1.setObjectName("lbl_atalho1")
        self.lbl_atalho1_2 = QtWidgets.QLabel(self.grupo_atalhos)
        self.lbl_atalho1_2.setGeometry(QtCore.QRect(20, 70, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_atalho1_2.setFont(font)
        self.lbl_atalho1_2.setObjectName("lbl_atalho1_2")
        self.lbl_atalho1_3 = QtWidgets.QLabel(self.grupo_atalhos)
        self.lbl_atalho1_3.setGeometry(QtCore.QRect(20, 110, 591, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_atalho1_3.setFont(font)
        self.lbl_atalho1_3.setObjectName("lbl_atalho1_3")
        self.lbl_atalho1_4 = QtWidgets.QLabel(self.grupo_atalhos)
        self.lbl_atalho1_4.setGeometry(QtCore.QRect(20, 150, 591, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_atalho1_4.setFont(font)
        self.lbl_atalho1_4.setObjectName("lbl_atalho1_4")
        self.lbl_atalho1_5 = QtWidgets.QLabel(self.grupo_atalhos)
        self.lbl_atalho1_5.setGeometry(QtCore.QRect(20, 190, 591, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_atalho1_5.setFont(font)
        self.lbl_atalho1_5.setObjectName("lbl_atalho1_5")
        self.lbl_atalho1_6 = QtWidgets.QLabel(self.grupo_atalhos)
        self.lbl_atalho1_6.setGeometry(QtCore.QRect(20, 230, 591, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_atalho1_6.setFont(font)
        self.lbl_atalho1_6.setObjectName("lbl_atalho1_6")
        self.lbl_atalho1_7 = QtWidgets.QLabel(self.grupo_atalhos)
        self.lbl_atalho1_7.setGeometry(QtCore.QRect(20, 270, 591, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_atalho1_7.setFont(font)
        self.lbl_atalho1_7.setObjectName("lbl_atalho1_7")
        self.lbl_atalho1_8 = QtWidgets.QLabel(self.grupo_atalhos)
        self.lbl_atalho1_8.setGeometry(QtCore.QRect(20, 310, 591, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_atalho1_8.setFont(font)
        self.lbl_atalho1_8.setObjectName("lbl_atalho1_8")
        self.tab_opcao = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_opcao.setGeometry(QtCore.QRect(20, 430, 921, 261))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_opcao.setFont(font)
        self.tab_opcao.setStyleSheet("QTabWidget{\n"
" background-color: #fffafa;\n"
"box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);\n"
"\n"
"}")
        self.tab_opcao.setObjectName("tab_opcao")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.grupo_chave_completa = QtWidgets.QGroupBox(self.tab)
        self.grupo_chave_completa.setGeometry(QtCore.QRect(30, 60, 821, 121))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.grupo_chave_completa.setFont(font)
        self.grupo_chave_completa.setObjectName("grupo_chave_completa")
        self.txtChave = QtWidgets.QPlainTextEdit(self.grupo_chave_completa)
        self.txtChave.setGeometry(QtCore.QRect(190, 30, 591, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.txtChave.setFont(font)
        self.txtChave.setToolTipDuration(3)
        self.txtChave.setAutoFillBackground(False)
        self.txtChave.setStyleSheet("")
        self.txtChave.setPlainText("")
        self.txtChave.setBackgroundVisible(False)
        self.txtChave.setCenterOnScroll(False)
        self.txtChave.setPlaceholderText("")
        self.txtChave.setObjectName("txtChave")
        self.lblChave = QtWidgets.QLabel(self.grupo_chave_completa)
        self.lblChave.setGeometry(QtCore.QRect(30, 30, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblChave.setFont(font)
        self.lblChave.setObjectName("lblChave")
        self.lblDigitos = QtWidgets.QLabel(self.grupo_chave_completa)
        self.lblDigitos.setGeometry(QtCore.QRect(200, 70, 311, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lblDigitos.setFont(font)
        self.lblDigitos.setText("")
        self.lblDigitos.setObjectName("lblDigitos")
        self.tab_opcao.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.grupo_chave_completa_2 = QtWidgets.QGroupBox(self.tab_2)
        self.grupo_chave_completa_2.setGeometry(QtCore.QRect(30, 60, 851, 121))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.grupo_chave_completa_2.setFont(font)
        self.grupo_chave_completa_2.setObjectName("grupo_chave_completa_2")
        self.txtChave_2 = QtWidgets.QPlainTextEdit(self.grupo_chave_completa_2)
        self.txtChave_2.setEnabled(False)
        self.txtChave_2.setGeometry(QtCore.QRect(280, 30, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.txtChave_2.setFont(font)
        self.txtChave_2.setAutoFillBackground(False)
        self.txtChave_2.setPlainText("")
        self.txtChave_2.setBackgroundVisible(False)
        self.txtChave_2.setCenterOnScroll(False)
        self.txtChave_2.setPlaceholderText("")
        self.txtChave_2.setObjectName("txtChave_2")
        self.lblChave_2 = QtWidgets.QLabel(self.grupo_chave_completa_2)
        self.lblChave_2.setGeometry(QtCore.QRect(30, 30, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblChave_2.setFont(font)
        self.lblChave_2.setObjectName("lblChave_2")
        self.lblDigitos_2 = QtWidgets.QLabel(self.grupo_chave_completa_2)
        self.lblDigitos_2.setGeometry(QtCore.QRect(200, 70, 311, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lblDigitos_2.setFont(font)
        self.lblDigitos_2.setText("")
        self.lblDigitos_2.setObjectName("lblDigitos_2")
        self.txtChave_3 = QtWidgets.QPlainTextEdit(self.grupo_chave_completa_2)
        self.txtChave_3.setGeometry(QtCore.QRect(620, 30, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.txtChave_3.setFont(font)
        self.txtChave_3.setAutoFillBackground(False)
        self.txtChave_3.setPlainText("")
        self.txtChave_3.setBackgroundVisible(False)
        self.txtChave_3.setCenterOnScroll(False)
        self.txtChave_3.setPlaceholderText("")
        self.txtChave_3.setObjectName("txtChave_3")
        self.tab_opcao.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.grupo_chave_completa_3 = QtWidgets.QGroupBox(self.tab_3)
        self.grupo_chave_completa_3.setGeometry(QtCore.QRect(20, 50, 871, 141))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.grupo_chave_completa_3.setFont(font)
        self.grupo_chave_completa_3.setObjectName("grupo_chave_completa_3")
        self.txt_arquivo = QtWidgets.QPlainTextEdit(self.grupo_chave_completa_3)
        self.txt_arquivo.setEnabled(False)
        self.txt_arquivo.setGeometry(QtCore.QRect(10, 30, 601, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.txt_arquivo.setFont(font)
        self.txt_arquivo.setAutoFillBackground(False)
        self.txt_arquivo.setPlainText("")
        self.txt_arquivo.setBackgroundVisible(False)
        self.txt_arquivo.setCenterOnScroll(False)
        self.txt_arquivo.setPlaceholderText("")
        self.txt_arquivo.setObjectName("txt_arquivo")
        self.lblDigitos_3 = QtWidgets.QLabel(self.grupo_chave_completa_3)
        self.lblDigitos_3.setGeometry(QtCore.QRect(200, 70, 311, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblDigitos_3.setFont(font)
        self.lblDigitos_3.setText("")
        self.lblDigitos_3.setObjectName("lblDigitos_3")
        self.btn_arquivo = QtWidgets.QPushButton(self.grupo_chave_completa_3)
        self.btn_arquivo.setGeometry(QtCore.QRect(640, 30, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_arquivo.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/icons/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_arquivo.setIcon(icon)
        self.btn_arquivo.setIconSize(QtCore.QSize(24, 24))
        self.btn_arquivo.setObjectName("btn_arquivo")
        self.btn_importar = QtWidgets.QPushButton(self.grupo_chave_completa_3)
        self.btn_importar.setGeometry(QtCore.QRect(10, 80, 851, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_importar.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/icons/up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_importar.setIcon(icon1)
        self.btn_importar.setIconSize(QtCore.QSize(32, 32))
        self.btn_importar.setObjectName("btn_importar")
        self.check_dir = QtWidgets.QCheckBox(self.tab_3)
        self.check_dir.setGeometry(QtCore.QRect(650, 30, 241, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.check_dir.setFont(font)
        self.check_dir.setObjectName("check_dir")
        self.tab_opcao.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.grupo_chave_completa_4 = QtWidgets.QGroupBox(self.tab_4)
        self.grupo_chave_completa_4.setGeometry(QtCore.QRect(20, 20, 871, 201))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.grupo_chave_completa_4.setFont(font)
        self.grupo_chave_completa_4.setObjectName("grupo_chave_completa_4")
        self.btn_portal = QtWidgets.QPushButton(self.grupo_chave_completa_4)
        self.btn_portal.setGeometry(QtCore.QRect(20, 110, 821, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_portal.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/icons/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_portal.setIcon(icon2)
        self.btn_portal.setIconSize(QtCore.QSize(32, 32))
        self.btn_portal.setObjectName("btn_portal")
        self.barra_progresso_portal = QtWidgets.QProgressBar(self.grupo_chave_completa_4)
        self.barra_progresso_portal.setGeometry(QtCore.QRect(20, 160, 821, 23))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.barra_progresso_portal.setFont(font)
        self.barra_progresso_portal.setProperty("value", 0)
        self.barra_progresso_portal.setTextVisible(False)
        self.barra_progresso_portal.setInvertedAppearance(False)
        self.barra_progresso_portal.setObjectName("barra_progresso_portal")
        self.lbl_cnpj_estab = QtWidgets.QLabel(self.grupo_chave_completa_4)
        self.lbl_cnpj_estab.setGeometry(QtCore.QRect(20, 40, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_cnpj_estab.setFont(font)
        self.lbl_cnpj_estab.setObjectName("lbl_cnpj_estab")
        self.lbl_qtde_notas = QtWidgets.QLabel(self.grupo_chave_completa_4)
        self.lbl_qtde_notas.setGeometry(QtCore.QRect(580, 40, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_qtde_notas.setFont(font)
        self.lbl_qtde_notas.setObjectName("lbl_qtde_notas")
        self.txt_cnpj_estab = QtWidgets.QLineEdit(self.grupo_chave_completa_4)
        self.txt_cnpj_estab.setGeometry(QtCore.QRect(240, 40, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.txt_cnpj_estab.setFont(font)
        self.txt_cnpj_estab.setObjectName("txt_cnpj_estab")
        self.txt_num_notas = QtWidgets.QLineEdit(self.grupo_chave_completa_4)
        self.txt_num_notas.setGeometry(QtCore.QRect(780, 40, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.txt_num_notas.setFont(font)
        self.txt_num_notas.setText("")
        self.txt_num_notas.setMaxLength(3)
        self.txt_num_notas.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_num_notas.setPlaceholderText("")
        self.txt_num_notas.setObjectName("txt_num_notas")
        self.tab_opcao.addTab(self.tab_4, "")
        self.btn_cnpj = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cnpj.setGeometry(QtCore.QRect(290, 30, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_cnpj.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/icons/cnpj.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cnpj.setIcon(icon3)
        self.btn_cnpj.setIconSize(QtCore.QSize(32, 32))
        self.btn_cnpj.setCheckable(False)
        self.btn_cnpj.setChecked(False)
        self.btn_cnpj.setAutoExclusive(False)
        self.btn_cnpj.setAutoDefault(False)
        self.btn_cnpj.setDefault(False)
        self.btn_cnpj.setObjectName("btn_cnpj")
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(10, 30, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_login.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("assets/icons/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_login.setIcon(icon4)
        self.btn_login.setIconSize(QtCore.QSize(32, 32))
        self.btn_login.setObjectName("btn_login")
        self.btn_limpa_banco = QtWidgets.QPushButton(self.centralwidget)
        self.btn_limpa_banco.setGeometry(QtCore.QRect(1340, 30, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_limpa_banco.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("assets/icons/database.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_limpa_banco.setIcon(icon5)
        self.btn_limpa_banco.setIconSize(QtCore.QSize(32, 32))
        self.btn_limpa_banco.setObjectName("btn_limpa_banco")
        self.btn_postar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_postar.setGeometry(QtCore.QRect(10, 340, 391, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_postar.setFont(font)
        self.btn_postar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_postar.setToolTipDuration(3)
        self.btn_postar.setStyleSheet("#btn_postar{\n"
"font-size: 16px;\n"
"font-family: Montserrat\n"
"}\n"
"")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("assets/icons/ai.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_postar.setIcon(icon6)
        self.btn_postar.setIconSize(QtCore.QSize(40, 40))
        self.btn_postar.setCheckable(False)
        self.btn_postar.setChecked(False)
        self.btn_postar.setAutoExclusive(False)
        self.btn_postar.setAutoDefault(False)
        self.btn_postar.setDefault(False)
        self.btn_postar.setFlat(False)
        self.btn_postar.setObjectName("btn_postar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 760, 261, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tab_opcao.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbTitulo.setText(_translate("MainWindow", "Cupons disponíveis"))
        self.grupo_atalhos.setTitle(_translate("MainWindow", "Teclas de Atalhos"))
        self.lbl_atalho1.setText(_translate("MainWindow", "ESC - limpa campo de chave"))
        self.lbl_atalho1_2.setText(_translate("MainWindow", "A - Captura por Leitor de Código de Barras"))
        self.lbl_atalho1_3.setText(_translate("MainWindow", "B - Captura por Digitação da Chave (5 últimos grupos)"))
        self.lbl_atalho1_4.setText(_translate("MainWindow", "C - Importar Arquivo"))
        self.lbl_atalho1_5.setText(_translate("MainWindow", "D - Buscar do Portal Nota do Bem"))
        self.lbl_atalho1_6.setText(_translate("MainWindow", "E - Atualizar CNPJ da instituição"))
        self.lbl_atalho1_7.setText(_translate("MainWindow", "L - Fazer Login no Portal"))
        self.lbl_atalho1_8.setText(_translate("MainWindow", "P - Postar no ambiente do governo"))
        self.grupo_chave_completa.setTitle(_translate("MainWindow", "Carga Pela Chave Completa"))
        self.txtChave.setToolTip(_translate("MainWindow", "Digite a Chave de Acesso Aqui"))
        self.lblChave.setText(_translate("MainWindow", "Chave de Acesso"))
        self.tab_opcao.setTabText(self.tab_opcao.indexOf(self.tab), _translate("MainWindow", "&Leitor de código de Barras"))
        self.grupo_chave_completa_2.setTitle(_translate("MainWindow", "Digitar 5 ultimos subgrupos"))
        self.txtChave_2.setToolTip(_translate("MainWindow", "Digite a Chave de Acesso Aqui"))
        self.lblChave_2.setText(_translate("MainWindow", "Chave de Acesso (parcial)"))
        self.txtChave_3.setToolTip(_translate("MainWindow", "Digite os ultimos 5 subgrupos da chave aqui"))
        self.tab_opcao.setTabText(self.tab_opcao.indexOf(self.tab_2), _translate("MainWindow", "&Digitar "))
        self.grupo_chave_completa_3.setTitle(_translate("MainWindow", "Buscar Arquivo"))
        self.txt_arquivo.setToolTip(_translate("MainWindow", "Digite a Chave de Acesso Aqui"))
        self.btn_arquivo.setText(_translate("MainWindow", "   Buscar Arquivo"))
        self.btn_importar.setText(_translate("MainWindow", "     Importar"))
        self.check_dir.setText(_translate("MainWindow", "Modo Diretório XMLs"))
        self.tab_opcao.setTabText(self.tab_opcao.indexOf(self.tab_3), _translate("MainWindow", "Importar Arquivo"))
        self.grupo_chave_completa_4.setTitle(_translate("MainWindow", "Clique no botão abaixo para buscar chaves de acesso disponíveis no Portal do Bem"))
        self.btn_portal.setText(_translate("MainWindow", "      Baixar Chaves de Acesso"))
        self.lbl_cnpj_estab.setText(_translate("MainWindow", "CNPJ do Estabelecimento"))
        self.lbl_qtde_notas.setText(_translate("MainWindow", "Quantidade de Notas"))
        self.tab_opcao.setTabText(self.tab_opcao.indexOf(self.tab_4), _translate("MainWindow", "Baixar notas do Portal"))
        self.btn_cnpj.setText(_translate("MainWindow", "      Atualizar Meu CNPJ"))
        self.btn_login.setText(_translate("MainWindow", "     Login no Portal do Bem"))
        self.btn_limpa_banco.setText(_translate("MainWindow", "  Limpar Banco de Dados"))
        self.btn_postar.setToolTip(_translate("MainWindow", "<H2>\n"
"  Clique aqui para iniciar a postagem automática no site da Nota Fiscal Paulista\n"
"</H2>"))
        self.btn_postar.setText(_translate("MainWindow", "      Iniciar Postagem de Notas"))
        self.label.setText(_translate("MainWindow", "<div>Icons made by <a href=\"https://www.flaticon.com/authors/icongeek26\" title=\"Icongeek26\">Icongeek26</a> from <a href=\"https://www.flaticon.com/\"             title=\"Flaticon\">www.flaticon.com</a></div>"))
