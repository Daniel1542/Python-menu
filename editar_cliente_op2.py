# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from editar_cliente_op2_janela import Ui_editar_cliente_2
import mysql.connector

database=('loja',)


def conecta_b(b=None):
    if b==None:
        banco=mysql.connector.connect(host='localhost',user='root',password='')
        return banco
    else:
        banco=mysql.connector.connect(host='localhost',user='root',password='',database=b)
        return banco


class Ui_editar_cliente(object):


    def buscar(self,nome):
        try:
            banco=conecta_b(database[0])
            cursor=banco.cursor()
            n=nome.strip()
            sq = 'SELECT * FROM clientes WHERE nome LIKE %s'
            if n=='':
                self.label_report_procura.setText('Digite o nome do cliente')
            else:
                val=(n,)
                cursor.execute(sq,val)
                result=cursor.fetchall()
                if len(result)>0:
                    for no in result:
                        print(no)
                    self.label_report_procura.setText('Cliente encontrado')
                    self.window=QtWidgets.QWidget()
                    self.ui=Ui_editar_cliente_2()
                    self.ui.setupUi(self.window)
                    self.ui.is_validate()
                    self.ui.transferencia(n)
                    self.window.show()
                else:
                    self.label_report_procura.setText('Cliente não encontrado')

        except BaseException as erro:
            print('erro'+str(erro))
        finally:
            cursor.close()
            banco.close()


    def setupUi(self, editar_cliente):
        editar_cliente.setObjectName("editar_cliente")
        editar_cliente.resize(417, 247)
        font = QtGui.QFont()
        font.setPointSize(12)
        editar_cliente.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("editar_cliente_op2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        editar_cliente.setWindowIcon(icon)
        editar_cliente.setStyleSheet('background-color:rgb(255,255,255)')


        self.label_titulo = QtWidgets.QLabel(editar_cliente)
        self.label_titulo.setGeometry(QtCore.QRect(50, 30, 321, 21))
        self.label_titulo.setObjectName("label_titulo")
        self.label_nome = QtWidgets.QLabel(editar_cliente)
        self.label_nome.setGeometry(QtCore.QRect(20, 90, 51, 21))
        self.label_nome.setObjectName("label_nome")

        self.lineEdit_nome = QtWidgets.QLineEdit(editar_cliente)
        self.lineEdit_nome.setGeometry(QtCore.QRect(80, 90, 311, 20))
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.lineEdit_nome.setMaxLength(35)

        self.pushButton_procurar = QtWidgets.QPushButton(editar_cliente)
        self.pushButton_procurar.setGeometry(QtCore.QRect(150, 140, 91, 23))
        self.pushButton_procurar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pesquisar_cliente_op3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_procurar.setIcon(icon1)
        self.pushButton_procurar.setObjectName("pushButton_procurar")
        self.pushButton_procurar.clicked.connect(lambda:self.buscar(self.lineEdit_nome.text()))


        self.label_report_procura = QtWidgets.QLabel(editar_cliente)
        self.label_report_procura.setGeometry(QtCore.QRect(20, 180, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_report_procura.setFont(font)
        self.label_report_procura.setText("")
        self.label_report_procura.setObjectName("label_report_procura")

        self.retranslateUi(editar_cliente)
        QtCore.QMetaObject.connectSlotsByName(editar_cliente)

    def retranslateUi(self, editar_cliente):
        _translate = QtCore.QCoreApplication.translate
        editar_cliente.setWindowTitle(_translate("editar_cliente", "Editar cliente"))
        self.label_titulo.setText(_translate("editar_cliente", "Digite o nome do cliente que você procura"))
        self.label_nome.setText(_translate("editar_cliente", "Nome:"))
        self.pushButton_procurar.setText(_translate("editar_cliente", "Procurar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    editar_cliente = QtWidgets.QWidget()
    ui = Ui_editar_cliente()
    ui.setupUi(editar_cliente)
    editar_cliente.show()
    sys.exit(app.exec_())
