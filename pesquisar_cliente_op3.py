# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from pesquisar_cliente_op3_janela import Ui_pesquisar_cliente_janela
import mysql.connector

database=('loja',)


def conecta_b(b=None):
    if b==None:
        banco=mysql.connector.connect(host='localhost',user='root',password='')
        return banco
    else:
        banco=mysql.connector.connect(host='localhost',user='root',password='',database=b)
        return banco


class Ui_pesquisar_cliente(object):

    def pesquisar_nome(self):
        try:
            banco=conecta_b(database[0])
            cursor=banco.cursor()
            n=self.lineEdit_nome.text()
            no=n.strip()
            if no=='':
                self.lineEdit_nome.setText('Preencha este campo')
            else:
                sq='SELECT * FROM clientes WHERE nome=%s'
                val=(no,)
                cursor.execute(sq,val)
                r=cursor.fetchone()
                if r is not None:
                    self.window=QtWidgets.QWidget()
                    self.ui=Ui_pesquisar_cliente_janela()
                    self.ui.setupUi(self.window)
                    self.ui.transfere(no)
                    self.window.show()
                else:
                    self.label_report.setText('Cliente não encontrado')
        except BaseException as erro:
            print('erro'+str(erro))
        finally:
            cursor.close()
            banco.close()


    def pesquisar_adress(self):
        try:
            banco=conecta_b(database[0])
            cursor=banco.cursor()
            a=self.lineEdit_adress.text()
            ad=a.strip()
            if ad=='':
                self.lineEdit_adress.setText('Preencha este campo')
            else:
                sq='SELECT * FROM clientes WHERE endereço=%s'
                val=(ad,)
                cursor.execute(sq,val)
                r=cursor.fetchall()
                if len(r)>0:
                    self.window=QtWidgets.QWidget()
                    self.ui=Ui_pesquisar_cliente_janela()
                    self.ui.setupUi(self.window)
                    self.ui.mandar(ad)
                    self.window.show()
                else:
                    self.label_report.setText('Cliente não encontrado')
        except BaseException as erro:
            print('erro'+str(erro))
        finally:
            cursor.close()
            banco.close()


    def setupUi(self, pesquisar_cliente):
        pesquisar_cliente.setObjectName("pesquisar_cliente")
        pesquisar_cliente.resize(526, 289)
        font = QtGui.QFont()
        font.setPointSize(12)
        pesquisar_cliente.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pesquisar_cliente_op3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pesquisar_cliente.setWindowIcon(icon)
        pesquisar_cliente.setStyleSheet('background-color:rgb(255,255,255)')

        self.label_1 = QtWidgets.QLabel(pesquisar_cliente)
        self.label_1.setGeometry(QtCore.QRect(30, 30, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_adress_2 = QtWidgets.QLabel(pesquisar_cliente)
        self.label_adress_2.setGeometry(QtCore.QRect(30, 100, 71, 21))
        self.label_adress_2.setObjectName("label_adress_2")
        self.label_adress = QtWidgets.QLabel(pesquisar_cliente)
        self.label_adress.setGeometry(QtCore.QRect(30, 150, 71, 21))
        self.label_adress.setObjectName("label_adress")
        self.lineEdit_nome = QtWidgets.QLineEdit(pesquisar_cliente)
        self.lineEdit_nome.setGeometry(QtCore.QRect(120, 100, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_nome.setFont(font)
        self.lineEdit_nome.setText("")
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.lineEdit_nome.setMaxLength(35)

        self.lineEdit_adress = QtWidgets.QLineEdit(pesquisar_cliente)
        self.lineEdit_adress.setGeometry(QtCore.QRect(120, 150, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_adress.setFont(font)
        self.lineEdit_adress.setObjectName("lineEdit_adress")
        self.label_report = QtWidgets.QLabel(pesquisar_cliente)
        self.label_report.setGeometry(QtCore.QRect(20, 200, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_report.setFont(font)
        self.label_report.setText("")
        self.label_report.setObjectName("label_report")
        self.pushButton = QtWidgets.QPushButton(pesquisar_cliente)
        self.pushButton.setGeometry(QtCore.QRect(410, 100, 91, 23))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.pesquisar_nome)

        self.pushButton_2 = QtWidgets.QPushButton(pesquisar_cliente)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 150, 91, 23))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.pesquisar_adress)

        self.retranslateUi(pesquisar_cliente)
        QtCore.QMetaObject.connectSlotsByName(pesquisar_cliente)

    def retranslateUi(self, pesquisar_cliente):
        _translate = QtCore.QCoreApplication.translate
        pesquisar_cliente.setWindowTitle(_translate("pesquisar_cliente", "Pesquisar cliente"))
        self.label_1.setText(_translate("pesquisar_cliente", "Escreva o nome ou o endereço do cliente"))
        self.label_adress_2.setText(_translate("pesquisar_cliente", "Nome"))
        self.label_adress.setText(_translate("pesquisar_cliente", "Endereço"))
        self.pushButton.setText(_translate("pesquisar_cliente", "Buscar"))
        self.pushButton_2.setText(_translate("pesquisar_cliente", "Buscar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pesquisar_cliente = QtWidgets.QWidget()
    ui = Ui_pesquisar_cliente()
    ui.setupUi(pesquisar_cliente)
    pesquisar_cliente.show()
    sys.exit(app.exec_())
