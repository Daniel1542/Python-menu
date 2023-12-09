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


class Ui_cadastrar_cliente(object):

    def menssage_box(self):
        ms=QMessageBox()
        ms.setText('Cliente cadastrado')
        ms.setWindowTitle('Cadastrado')
        ms.setDefaultButton(QMessageBox.Ok)
        if QMessageBox.Ok:
            pass
        ms.exec_()


    def is_validate(self):
        regex = QtCore.QRegExp("[0-9_]+")
        department_validator = QtGui.QRegExpValidator(regex, self.lineEdit_valor)
        self.lineEdit_valor.setValidator(department_validator)


    def cadastro(self,nome,adress,valor):
        try:
            banco=conecta_b(database[0])
            cursor=banco.cursor()
            n=nome.strip()
            endereco=adress.strip()
            try:
                if all(x.isalpha() or x.isspace() for x in n):
                    f = True
                else:
                    self.lineEdit_nome.setText("Preencha o nome com letras")
                    f = False
            except BaseException as erro:
                print('erro'+str(erro))

            if self.lineEdit_nome.displayText()=='' or self.lineEdit_adress.displayText()=='' or self.lineEdit_valor.displayText()=='':
                self.label_report.setText('Preencha todos os campos')

            elif self.lineEdit_nome.displayText()!=''  and self.lineEdit_adress.displayText()!=''  and self.lineEdit_valor.displayText()!='' and n!='' and endereco!='' and f==True:
                sq = 'SELECT * FROM clientes WHERE nome=%s'
                val = (n,)
                cursor.execute(sq, val)
                r = cursor.fetchall()
                if len(r) ==0:
                    for no in r:
                        print(no)
                    sq = 'INSERT INTO clientes(nome,endereço,compras) VALUES(%s,%s,%s)'
                    val=(n,endereco,valor)
                    cursor.execute(sq,val)
                    banco.commit()
                    self.lineEdit_nome.setText('')
                    self.lineEdit_adress.setText('')
                    self.lineEdit_valor.setText('')
                    self.label_report.setText('Você pode fechar essa janela')
                    self.menssage_box()
                else:
                    self.label_report.setText('Cliente já existente')

            elif n=='':
                self.lineEdit_nome.setText("Preencha o nome com letras")
            elif endereco=='':
                self.lineEdit_adress.setText("Preencha o endereço")

        except BaseException as erro:
            print('Erro de cadastro'+str(erro))
        finally:
            cursor.close()
            banco.close()


    def setupUi(self, cadastrar_cliente):
        cadastrar_cliente.setObjectName("cadastrar_cliente")
        cadastrar_cliente.resize(465, 292)
        font = QtGui.QFont()
        font.setPointSize(12)
        cadastrar_cliente.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("menu_cadastrar_op1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        cadastrar_cliente.setWindowIcon(icon)
        cadastrar_cliente.setStyleSheet('background-color:rgb(255,255,255)')
        self.label_nome = QtWidgets.QLabel(cadastrar_cliente)
        self.label_nome.setGeometry(QtCore.QRect(40, 20, 71, 21))
        self.label_nome.setObjectName("label_nome")
        self.label_adress = QtWidgets.QLabel(cadastrar_cliente)
        self.label_adress.setGeometry(QtCore.QRect(40, 60, 81, 21))
        self.label_adress.setObjectName("label_adress")
        self.label_valor = QtWidgets.QLabel(cadastrar_cliente)
        self.label_valor.setGeometry(QtCore.QRect(40, 100, 141, 21))
        self.label_valor.setObjectName("label_valor")
        self.lineEdit_nome = QtWidgets.QLineEdit(cadastrar_cliente)
        self.lineEdit_nome.setGeometry(QtCore.QRect(130, 20, 311, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_nome.setFont(font)
        self.lineEdit_nome.setText("")
        self.lineEdit_nome.setMaxLength(35)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.lineEdit_adress = QtWidgets.QLineEdit(cadastrar_cliente)
        self.lineEdit_adress.setGeometry(QtCore.QRect(130, 60, 311, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_adress.setFont(font)
        self.lineEdit_adress.setText("")
        self.lineEdit_adress.setMaxLength(35)
        self.lineEdit_adress.setObjectName("lineEdit_adress")
        self.label_report = QtWidgets.QLabel(cadastrar_cliente)
        self.label_report.setGeometry(QtCore.QRect(20, 220, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_report.setFont(font)
        self.label_report.setText("")
        self.label_report.setObjectName("label_report")
        self.pushButton_cadastrar = QtWidgets.QPushButton(cadastrar_cliente)
        self.pushButton_cadastrar.setGeometry(QtCore.QRect(140, 160, 101, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_cadastrar.setFont(font)
        self.pushButton_cadastrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_cadastrar.setIcon(icon)
        self.pushButton_cadastrar.setObjectName("pushButton_cadastrar")
        self.pushButton_cadastrar.clicked.connect(lambda:self.cadastro(self.lineEdit_nome.text(),self.lineEdit_adress.text(),self.lineEdit_valor.text()))

        self.lineEdit_valor = QtWidgets.QLineEdit(cadastrar_cliente)
        self.lineEdit_valor.setGeometry(QtCore.QRect(190, 100, 251, 20))
        self.lineEdit_valor.setMaxLength(8)
        self.lineEdit_valor.setObjectName("lineEdit_valor")

        self.retranslateUi(cadastrar_cliente)
        QtCore.QMetaObject.connectSlotsByName(cadastrar_cliente)

    def retranslateUi(self, cadastrar_cliente):
        _translate = QtCore.QCoreApplication.translate
        cadastrar_cliente.setWindowTitle(_translate("cadastrar_cliente", "Cadastrando"))
        self.label_nome.setText(_translate("cadastrar_cliente", "Nome"))
        self.label_adress.setText(_translate("cadastrar_cliente", "Endereço"))
        self.label_valor.setText(_translate("cadastrar_cliente", "Valor em compras"))
        self.pushButton_cadastrar.setText(_translate("cadastrar_cliente", "Cadastrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cadastrar_cliente = QtWidgets.QWidget()
    ui = Ui_cadastrar_cliente()
    ui.setupUi(cadastrar_cliente)
    ui.is_validate()
    cadastrar_cliente.show()
    sys.exit(app.exec_())
