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


class Ui_editar_cliente_2(object):

    def is_validate(self):
        regex = QtCore.QRegExp("[0-9_]+")
        department_validator = QtGui.QRegExpValidator(regex, self.lineEdit_valor)
        self.lineEdit_valor.setValidator(department_validator)


    def message(self):
        ms=QMessageBox()
        ms.setText('Cliente editado')
        ms.setWindowTitle('Editado')
        ms.setDefaultButton(QMessageBox.Ok)
        if QMessageBox.Ok:
            pass
        ms.exec_()


    def transferencia(self,no):
        banco = conecta_b(database[0])
        cursor = banco.cursor()
        sq = 'SELECT * FROM clientes WHERE nome LIKE %s'
        val = (no,)
        cursor.execute(sq, val)
        result = cursor.fetchall()
        for n in result:
            print(n)
            self.lineEdit_nome_2.setText(str(n[1]))
            self.lineEdit_adress.setText(str(n[2]))
            self.lineEdit_valor.setText(str(n[3]))
            self.label_cliente.setText(str(n[1]))


    def editar(self,nome,endereco):
        try:
            banco=conecta_b(database[0])
            cursor=banco.cursor()
            no=nome.strip()
            end=endereco.strip()
            try:
                if all(x.isalpha() or x.isspace() for x in no):
                    f = True
                else:
                    self.lineEdit_nome_2.setText('Preencha o nome com letras')
                    f = False
            except BaseException as erro:
                print('erro'+str(erro))

            if self.lineEdit_nome_2.displayText()!= '' and self.lineEdit_adress.displayText()!= '' and self.lineEdit_valor.displayText()!= '' and no!='' and end!='' and f==True:
                sq = 'SELECT * FROM clientes WHERE nome LIKE %s'
                val=(self.label_cliente.text(),)
                cursor.execute(sq, val)
                r = cursor.fetchone()
                if r[1]!=no:
                    sq = 'UPDATE clientes SET nome=%s,endereço=%s,compras=%s WHERE clientes.id=' + str(r[0])
                    val = (no, end, self.lineEdit_valor.text())
                    cursor.execute(sq, val)
                    banco.commit()
                    self.label_cliente.setText(no)
                    self.label_report_editar.setText('Você pode fechar esta janela')
                    self.message()
                else:
                    self.label_report_editar.setText('Cliente ja existente')
            elif self.lineEdit_nome_2.displayText()== '' or self.lineEdit_adress.displayText()== '' or self.lineEdit_valor.displayText()== '':
                self.label_report_editar.setText('Preencha todos os campos')
            elif no=='':
                self.lineEdit_nome_2.setText('Preencha o nome com letras')
            elif end=='':
                self.lineEdit_adress.setText("Preencha o endereço")

        except BaseException as erro:
            print('erro'+str(erro))
        finally:
            cursor.close()
            banco.close()


    def setupUi(self, editar_cliente_2):
        editar_cliente_2.setObjectName("editar_cliente_2")
        editar_cliente_2.resize(493, 377)
        font = QtGui.QFont()
        font.setPointSize(12)
        editar_cliente_2.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("editar_cliente_op2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        editar_cliente_2.setWindowIcon(icon)
        editar_cliente_2.setStyleSheet('background-color:rgb(255,255,255)')

        self.label_report_editar = QtWidgets.QLabel(editar_cliente_2)
        self.label_report_editar.setGeometry(QtCore.QRect(30, 320, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_report_editar.setFont(font)
        self.label_report_editar.setText("")
        self.label_report_editar.setObjectName("label_report_editar")
        self.label_titulo2 = QtWidgets.QLabel(editar_cliente_2)
        self.label_titulo2.setGeometry(QtCore.QRect(60, 30, 291, 21))
        self.label_titulo2.setObjectName("label_titulo2")
        self.lineEdit_nome_2 = QtWidgets.QLineEdit(editar_cliente_2)
        self.lineEdit_nome_2.setGeometry(QtCore.QRect(100, 120, 371, 20))
        self.lineEdit_nome_2.setText("")
        self.lineEdit_nome_2.setMaxLength(35)
        self.lineEdit_nome_2.setObjectName("lineEdit_nome_2")
        self.label_nome2 = QtWidgets.QLabel(editar_cliente_2)
        self.label_nome2.setGeometry(QtCore.QRect(30, 120, 61, 21))
        self.label_nome2.setObjectName("label_nome2")
        self.lineEdit_adress = QtWidgets.QLineEdit(editar_cliente_2)
        self.lineEdit_adress.setGeometry(QtCore.QRect(130, 170, 341, 20))
        self.lineEdit_adress.setText("")
        self.lineEdit_adress.setMaxLength(35)
        self.lineEdit_adress.setObjectName("lineEdit_adress")
        self.label_adress = QtWidgets.QLabel(editar_cliente_2)
        self.label_adress.setGeometry(QtCore.QRect(30, 170, 81, 21))
        self.label_adress.setObjectName("label_adress")
        self.pushButton_editar = QtWidgets.QPushButton(editar_cliente_2)
        self.pushButton_editar.setGeometry(QtCore.QRect(160, 270, 91, 23))
        self.pushButton_editar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_editar.setIcon(icon)
        self.pushButton_editar.setObjectName("pushButton_editar")
        self.pushButton_editar.clicked.connect(lambda:self.editar(self.lineEdit_nome_2.text(),self.lineEdit_adress.text()))


        self.label_valor = QtWidgets.QLabel(editar_cliente_2)
        self.label_valor.setGeometry(QtCore.QRect(30, 220, 141, 21))
        self.label_valor.setObjectName("label_valor")
        self.label_cliente = QtWidgets.QLabel(editar_cliente_2)
        self.label_cliente.setGeometry(QtCore.QRect(26, 72, 381, 21))
        self.label_cliente.setText("")
        self.label_cliente.setObjectName("label_cliente")
        self.lineEdit_valor = QtWidgets.QLineEdit(editar_cliente_2)
        self.lineEdit_valor.setGeometry(QtCore.QRect(190, 220, 201, 20))
        self.lineEdit_valor.setInputMask("")
        self.lineEdit_valor.setText("")
        self.lineEdit_valor.setMaxLength(8)
        self.lineEdit_valor.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_valor.setClearButtonEnabled(False)
        self.lineEdit_valor.setObjectName("lineEdit_valor")

        self.retranslateUi(editar_cliente_2)
        QtCore.QMetaObject.connectSlotsByName(editar_cliente_2)

    def retranslateUi(self, editar_cliente_2):
        _translate = QtCore.QCoreApplication.translate
        editar_cliente_2.setWindowTitle(_translate("editar_cliente_2", "Editando cliente"))
        self.label_titulo2.setText(_translate("editar_cliente_2", "Digite os campos a serem editados"))
        self.label_nome2.setText(_translate("editar_cliente_2", "Nome:"))
        self.label_adress.setText(_translate("editar_cliente_2", "Endereço:"))
        self.pushButton_editar.setText(_translate("editar_cliente_2", "Editar"))
        self.label_valor.setText(_translate("editar_cliente_2", "Valor em compras:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    editar_cliente_2 = QtWidgets.QWidget()
    ui = Ui_editar_cliente_2()
    ui.setupUi(editar_cliente_2)
    ui.is_validate()
    editar_cliente_2.show()
    sys.exit(app.exec_())
