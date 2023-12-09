# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from criar_conta_usuario import Ui_cadastro
from menu import Ui_menu
import mysql.connector

database=('loja',)


def conecta_b(b=None):
    if b==None:
        banco=mysql.connector.connect(host='localhost',user='root',password='')
        return banco
    else:
        banco=mysql.connector.connect(host='localhost',user='root',password='',database=b)
        return banco


def criar_b():
    try:
        banco=conecta_b()
        cursor=banco.cursor()
        cursor.execute('CREATE DATABASE loja')
        print('banco criado')
        criar_tab()
    except BaseException as erro:
        print('erro criar banco')+str(erro)
    finally:
        cursor.close()
        banco.close()


def criar_tab():
    try:
        banco=conecta_b(database[0])
        cursor=banco.cursor()
        cursor.execute('CREATE TABLE clientes(id INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR (35),endereço VARCHAR (35),compras VARCHAR (15))')
        cursor.execute('CREATE TABLE usuários(id INT AUTO_INCREMENT PRIMARY KEY,login VARCHAR (15),senha VARCHAR (15))')
        sq='INSERT INTO usuários(login,senha) VALUES(%s,%s)'
        val=('adm','adm')
        cursor.execute(sq,val)
        banco.commit()
        print('tabela criada')
    except BaseException as erro:
        print('Erro criar tab')+str(erro)
    finally:
        cursor.close()
        banco.close()


def existe_b():
    status=False
    try:
        banco=conecta_b()
        cursor=banco.cursor()
        cursor.execute('SHOW DATABASES')
        for n in cursor:
            if n==database:
                status=True
    except BaseException as erro:
        print('Erro ao verificar banco')+str(erro)
    finally:
        cursor.close()
        banco.close()
    return status


class Ui_login(object):
    if not existe_b():
        criar_b()

    def is_validate(self):
        regex = QtCore.QRegExp("[a-z-A-Z_]+[0-9_]+")
        department_validator = QtGui.QRegExpValidator(regex, self.lineEdit_login)
        self.lineEdit_login.setValidator(department_validator)


    def abrir_cadastro(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_cadastro()
        self.ui.setupUi(self.window)
        self.ui.is_validate()
        self.window.show()


    def abra_menu(self):
        try:
            banco = conecta_b(database[0])
            cursor = banco.cursor()
            user=self.lineEdit_login.text()
            senha=self.lineEdit_senha.text()
            sq = 'SELECT * FROM usuários WHERE login LIKE %s'
            va = (user,)
            cursor.execute(sq, va)
            r = cursor.fetchone()
            if r is not None and r[2] == senha:
                self.lbl_report.setText('Logado')
                self.window = QtWidgets.QWidget()
                self.ui = Ui_menu()
                self.ui.setupUi(self.window)
                self.window.show()
            else:
                self.lbl_report.setText('Erro de usuário ou senha')
        except BaseException as erro:
            print('Erro Menu') + str(erro)
        finally:
            cursor.close()
            banco.close()


    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(313, 239)
        font = QtGui.QFont()
        font.setPointSize(12)
        login.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("criar_conta_usuario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        login.setWindowIcon(icon)
        login.setStyleSheet('background-color:rgb(255,255,255)')


        self.centralwidget = QtWidgets.QWidget(login)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_logar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_logar.setGeometry(QtCore.QRect(60, 110, 75, 31))
        self.btn_logar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_logar.setIcon(icon)
        self.btn_logar.setObjectName("btn_logar")
        self.btn_logar.clicked.connect(self.abra_menu)


        self.lineEdit_senha = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_senha.setGeometry(QtCore.QRect(100, 70, 181, 20))
        self.lineEdit_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_senha.setMaxLength(15)
        self.lineEdit_senha.setObjectName("lineEdit_senha")


        self.login_lbl = QtWidgets.QLabel(self.centralwidget)
        self.login_lbl.setGeometry(QtCore.QRect(30, 30, 51, 21))
        self.login_lbl.setObjectName("login_lbl")


        self.senha_lbl = QtWidgets.QLabel(self.centralwidget)
        self.senha_lbl.setGeometry(QtCore.QRect(30, 70, 51, 21))
        self.senha_lbl.setObjectName("senha_lbl")


        self.lineEdit_login = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_login.setGeometry(QtCore.QRect(100, 30, 181, 20))
        self.lineEdit_login.setMaxLength(15)
        self.lineEdit_login.setObjectName("lineEdit_login")


        self.lbl_report = QtWidgets.QLabel(self.centralwidget)
        self.lbl_report.setGeometry(QtCore.QRect(20, 160, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_report.setFont(font)
        self.lbl_report.setText("")
        self.lbl_report.setObjectName("lbl_report")
        self.pbn_new_user = QtWidgets.QPushButton(self.centralwidget)
        self.pbn_new_user.setGeometry(QtCore.QRect(160, 110, 121, 31))
        self.pbn_new_user.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("menu_cadastrar_op1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbn_new_user.setIcon(icon1)
        self.pbn_new_user.setObjectName("pbn_new_user")
        self.pbn_new_user.clicked.connect(self.abrir_cadastro)


        login.setCentralWidget(self.centralwidget)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Login"))
        self.btn_logar.setText(_translate("login", "Logar"))
        self.login_lbl.setText(_translate("login", "Login"))
        self.senha_lbl.setText(_translate("login", "Senha"))
        self.pbn_new_user.setText(_translate("login", "Novo usuário"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QMainWindow()
    ui = Ui_login()
    ui.setupUi(login)
    ui.is_validate()
    login.show()
    sys.exit(app.exec_())
