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


class Ui_excluir_cliente_op4(object):

    def message(self):
        ms=QMessageBox()
        ms.setText('Nenhuma mudança feita')
        ms.setWindowTitle('Sem mudança')
        ms.setDefaultButton(QMessageBox.Ok)
        if QMessageBox.Ok:
            pass
        ms.exec_()


    def buscar(self, nome):
        try:
            banco = conecta_b(database[0])
            cursor = banco.cursor()
            no=nome.strip()
            if no=='':
                self.lineEdit_nome.setText('Preencha este campo e clique em buscar')
            else:
                sq = 'SELECT * FROM clientes WHERE nome LIKE %s'
                val = (no,)
                cursor.execute(sq, val)
                resultado = cursor.fetchall()
                if len(resultado)>0:
                    for n in resultado:
                        print(n)
                    self.lineEdit_nome_2.setText(str(n[1]))
                    self.lineEdit_adress.setText(str(n[2]))
                    self.lineEdit_valor.setText(str(n[3]))
                else:
                    self.label_report.setText('Cliente não encontrado')
        except BaseException as erro:
            print('erro') + str(erro)
        finally:
            cursor.close()
            banco.close()


    def deletar(self,nome):
        try:
            banco=conecta_b(database[0])
            cursor=banco.cursor()
            if nome!='':
                sq='SELECT * FROM clientes WHERE nome LIKE %s'
                val=(nome,)
                cursor.execute(sq,val)
                r=cursor.fetchall()
                if len(r)>0:
                    for n in r:
                        print(n)
                    sq='DELETE FROM clientes WHERE clientes.id='+str(n[0])
                    cursor.execute(sq,)
                    banco.commit()
                    self.lineEdit_nome_2.setText('')
                    self.lineEdit_adress.setText('')
                    self.lineEdit_valor.setText('')
                    self.lineEdit_nome.setText('')
                    self.label_report_2.setText('Cliente excluido')
            else:
                self.lineEdit_nome.setText('Preencha este campo e clique em buscar')
        except BaseException as erro:
            print('erro')+str(erro)
        finally:
            cursor.close()
            banco.close()


    def op_nao(self):
        try:
            self.lineEdit_nome_2.setText('')
            self.lineEdit_adress.setText('')
            self.lineEdit_valor.setText('')
            self.lineEdit_nome.setText('')
            self.label_report_2.setText('Nenhuma mudança feita')
            self.message()
        except BaseException as erro:
            print('erro')+str(erro)


    def setupUi(self, excluir_cliente_op4):
        excluir_cliente_op4.setObjectName("excluir_cliente_op4")
        excluir_cliente_op4.resize(437, 459)
        font = QtGui.QFont()
        font.setPointSize(12)
        excluir_cliente_op4.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("excluir_cliente_op4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        excluir_cliente_op4.setWindowIcon(icon)
        excluir_cliente_op4.setStyleSheet('background-color:rgb(255,255,255)')


        self.label_titulo_2 = QtWidgets.QLabel(excluir_cliente_op4)
        self.label_titulo_2.setGeometry(QtCore.QRect(30, 190, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_titulo_2.setFont(font)
        self.label_titulo_2.setObjectName("label_titulo_2")


        self.pushButton_sim = QtWidgets.QPushButton(excluir_cliente_op4)
        self.pushButton_sim.setGeometry(QtCore.QRect(90, 360, 75, 23))
        self.pushButton_sim.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_sim.setIcon(icon)
        self.pushButton_sim.setObjectName("pushButton_sim")
        self.pushButton_sim.clicked.connect(lambda:self.deletar(self.lineEdit_nome_2.text()))


        self.pushButton_nao = QtWidgets.QPushButton(excluir_cliente_op4)
        self.pushButton_nao.setGeometry(QtCore.QRect(240, 360, 75, 23))
        self.pushButton_nao.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("excluir_cliente_op4_btn_nao.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_nao.setIcon(icon1)
        self.pushButton_nao.setObjectName("pushButton_nao")
        self.pushButton_nao.clicked.connect(self.op_nao)


        self.label_report_2 = QtWidgets.QLabel(excluir_cliente_op4)
        self.label_report_2.setGeometry(QtCore.QRect(20, 400, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_report_2.setFont(font)
        self.label_report_2.setText("")
        self.label_report_2.setObjectName("label_report_2")


        self.label_titulo = QtWidgets.QLabel(excluir_cliente_op4)
        self.label_titulo.setGeometry(QtCore.QRect(30, 30, 211, 21))
        self.label_titulo.setObjectName("label_titulo")


        self.label_nome = QtWidgets.QLabel(excluir_cliente_op4)
        self.label_nome.setGeometry(QtCore.QRect(30, 70, 47, 21))
        self.label_nome.setObjectName("label_nome")


        self.lineEdit_nome = QtWidgets.QLineEdit(excluir_cliente_op4)
        self.lineEdit_nome.setGeometry(QtCore.QRect(100, 70, 311, 20))
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.lineEdit_nome.setMaxLength(35)


        self.label_report = QtWidgets.QLabel(excluir_cliente_op4)
        self.label_report.setGeometry(QtCore.QRect(30, 150, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_report.setFont(font)
        self.label_report.setText("")
        self.label_report.setObjectName("label_report")


        self.label_nome_2 = QtWidgets.QLabel(excluir_cliente_op4)
        self.label_nome_2.setGeometry(QtCore.QRect(30, 230, 61, 21))
        self.label_nome_2.setObjectName("label_nome_2")


        self.label_adress = QtWidgets.QLabel(excluir_cliente_op4)
        self.label_adress.setGeometry(QtCore.QRect(30, 270, 81, 21))
        self.label_adress.setObjectName("label_adress")


        self.label_valor = QtWidgets.QLabel(excluir_cliente_op4)
        self.label_valor.setGeometry(QtCore.QRect(30, 310, 141, 21))
        self.label_valor.setObjectName("label_valor")


        self.lineEdit_nome_2 = QtWidgets.QLineEdit(excluir_cliente_op4)
        self.lineEdit_nome_2.setGeometry(QtCore.QRect(100, 230, 311, 20))
        self.lineEdit_nome_2.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.lineEdit_nome_2.setReadOnly(True)
        self.lineEdit_nome_2.setObjectName("lineEdit_nome_2")


        self.lineEdit_adress = QtWidgets.QLineEdit(excluir_cliente_op4)
        self.lineEdit_adress.setGeometry(QtCore.QRect(120, 270, 291, 20))
        self.lineEdit_adress.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.lineEdit_adress.setReadOnly(True)
        self.lineEdit_adress.setObjectName("lineEdit_adress")


        self.lineEdit_valor = QtWidgets.QLineEdit(excluir_cliente_op4)
        self.lineEdit_valor.setGeometry(QtCore.QRect(190, 310, 221, 20))
        self.lineEdit_valor.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.lineEdit_valor.setReadOnly(True)
        self.lineEdit_valor.setObjectName("lineEdit_valor")


        self.pushButton_buscar = QtWidgets.QPushButton(excluir_cliente_op4)
        self.pushButton_buscar.setGeometry(QtCore.QRect(170, 120, 81, 23))
        self.pushButton_buscar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pesquisar_cliente_op3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_buscar.setIcon(icon2)
        self.pushButton_buscar.setObjectName("pushButton_buscar")
        self.pushButton_buscar.clicked.connect(lambda:self.buscar(self.lineEdit_nome.text()))


        self.retranslateUi(excluir_cliente_op4)
        QtCore.QMetaObject.connectSlotsByName(excluir_cliente_op4)

    def retranslateUi(self, excluir_cliente_op4):
        _translate = QtCore.QCoreApplication.translate
        excluir_cliente_op4.setWindowTitle(_translate("excluir_cliente_op4", "Excluir cliente"))
        self.label_titulo_2.setText(_translate("excluir_cliente_op4", "Tem certeza que deseja excluir?"))
        self.pushButton_sim.setText(_translate("excluir_cliente_op4", "Sim"))
        self.pushButton_nao.setText(_translate("excluir_cliente_op4", "Não"))
        self.label_titulo.setText(_translate("excluir_cliente_op4", "Digite o nome do cliente"))
        self.label_nome.setText(_translate("excluir_cliente_op4", "Nome:"))
        self.label_nome_2.setText(_translate("excluir_cliente_op4", "Nome:"))
        self.label_adress.setText(_translate("excluir_cliente_op4", "Endereço:"))
        self.label_valor.setText(_translate("excluir_cliente_op4", "Valor em compras:"))
        self.pushButton_buscar.setText(_translate("excluir_cliente_op4", "Buscar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    excluir_cliente_op4 = QtWidgets.QWidget()
    ui = Ui_excluir_cliente_op4()
    ui.setupUi(excluir_cliente_op4)
    excluir_cliente_op4.show()
    sys.exit(app.exec_())
