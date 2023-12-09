# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector

database=('loja',)


def conecta_b(b=None):
    if b==None:
        banco=mysql.connector.connect(host='localhost',user='root',password='')
        return banco
    else:
        banco=mysql.connector.connect(host='localhost',user='root',password='',database=b)
        return banco

class Ui_cadastro(object):

    def menssage(self):
        ms=QMessageBox()
        ms.setText('Usuário cadastrado')
        ms.setWindowTitle('Cadastrado')
        ms.setDefaultButton(QMessageBox.Ok)
        if QMessageBox.Ok:
            pass
        ms.exec_()


    def is_validate(self):
        regex = QtCore.QRegExp("[a-z-A-Z_]+[0-9_]+")
        department_validator = QtGui.QRegExpValidator(regex, self.lineEdit_user)
        self.lineEdit_user.setValidator(department_validator)


    def cadastrar(self,nome,senha,confirma):
        try:
            banco=conecta_b(database[0])
            cursor=banco.cursor()
            if nome=='' or senha=='' or confirma=='':
                self.lbl_report.setText('Preencha os todos os campos')
            elif len(senha)<5 and len(confirma)<5:
                self.lbl_report.setText('senha muito curta')
            else:
                if senha==confirma:
                    sq = 'SELECT * FROM usuários WHERE login LIKE %s'
                    val=(nome,)
                    cursor.execute(sq,val)
                    result=cursor.fetchall()
                    if len(result)==0:
                        sq = 'INSERT INTO usuários(login,senha) VALUES(%s,%s)'
                        tudo = (nome, senha)
                        cursor.execute(sq, tudo)
                        banco.commit()
                        self.lbl_report.setText('Você pode fechar esta janela')
                        self.lineEdit_user.setText("")
                        self.lineEdit_senha.setText("")
                        self.lineEdit_confirma_senha.setText("")
                        self.menssage()
                    else:
                        self.lbl_report.setText('Usuário ja existente')
                else:
                    self.lbl_report.setText('As senhas são diferentes')

        except BaseException as erro:
            print('erro ao abrir janela'+str(erro))
        finally:
            cursor.close()
            banco.close()


    def setupUi(self, cadastro):
        cadastro.setObjectName("cadastro")
        cadastro.resize(334, 246)
        font = QtGui.QFont()
        font.setPointSize(12)
        cadastro.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("menu_cadastrar_op1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        cadastro.setWindowIcon(icon)
        cadastro.setStyleSheet('background-color:rgb(255,255,255)')


        self.lbl_report = QtWidgets.QLabel(cadastro)
        self.lbl_report.setGeometry(QtCore.QRect(20, 190, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_report.setFont(font)
        self.lbl_report.setText("")
        self.lbl_report.setObjectName("lbl_report")
        self.new_user_lbl = QtWidgets.QLabel(cadastro)
        self.new_user_lbl.setGeometry(QtCore.QRect(20, 30, 111, 21))
        self.new_user_lbl.setObjectName("new_user_lbl")
        self.lineEdit_senha = QtWidgets.QLineEdit(cadastro)
        self.lineEdit_senha.setGeometry(QtCore.QRect(130, 70, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_senha.setFont(font)
        self.lineEdit_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_senha.setMaxLength(15)
        self.lineEdit_senha.setObjectName("lineEdit_senha")

        self.password_lbl = QtWidgets.QLabel(cadastro)
        self.password_lbl.setGeometry(QtCore.QRect(20, 70, 111, 20))
        self.password_lbl.setObjectName("password_lbl")
        self.lineEdit_user = QtWidgets.QLineEdit(cadastro)
        self.lineEdit_user.setGeometry(QtCore.QRect(130, 30, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_user.setFont(font)
        self.lineEdit_user.setMaxLength(15)
        self.lineEdit_user.setObjectName("lineEdit_user")


        self.button_criar = QtWidgets.QPushButton(cadastro)
        self.button_criar.setGeometry(QtCore.QRect(130, 150, 75, 23))
        self.button_criar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_criar.setIcon(icon)
        self.button_criar.setObjectName("button_criar")
        self.button_criar.clicked.connect(lambda:self.cadastrar(self.lineEdit_user.text(),self.lineEdit_senha.text(),self.lineEdit_confirma_senha.text()))


        self.label = QtWidgets.QLabel(cadastro)
        self.label.setGeometry(QtCore.QRect(20, 110, 131, 21))
        self.label.setObjectName("label")


        self.lineEdit_confirma_senha = QtWidgets.QLineEdit(cadastro)
        self.lineEdit_confirma_senha.setGeometry(QtCore.QRect(160, 110, 151, 20))
        self.lineEdit_confirma_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_confirma_senha.setMaxLength(15)
        self.lineEdit_confirma_senha.setObjectName("lineEdit_confirma_senha")

        self.retranslateUi(cadastro)
        QtCore.QMetaObject.connectSlotsByName(cadastro)

    def retranslateUi(self, cadastro):
        _translate = QtCore.QCoreApplication.translate
        cadastro.setWindowTitle(_translate("cadastro", "Cadastro"))
        self.new_user_lbl.setText(_translate("cadastro", "Novo Usuario"))
        self.password_lbl.setText(_translate("cadastro", "Senha"))
        self.button_criar.setText(_translate("cadastro", "Criar"))
        self.label.setText(_translate("cadastro", "Confirmar senha"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cadastro = QtWidgets.QWidget()
    ui = Ui_cadastro()
    ui.setupUi(cadastro)
    ui.is_validate()
    cadastro.show()
    sys.exit(app.exec_())
