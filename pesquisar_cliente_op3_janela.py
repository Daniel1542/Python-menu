# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

database=('loja',)


def conecta_b(b=None):
    if b==None:
        banco=mysql.connector.connect(host='localhost',user='root',password='')
        return banco
    else:
        banco=mysql.connector.connect(host='localhost',user='root',password='',database=b)
        return banco


class Ui_pesquisar_cliente_janela(object):

    def transfere(self,name):
        banco=conecta_b(database[0])
        cursor=banco.cursor()
        sq='SELECT * FROM clientes WHERE nome=%s'
        val=(name,)
        cursor.execute(sq,val)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(cursor):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


    def mandar(self,adress):
        banco=conecta_b(database[0])
        cursor=banco.cursor()
        sq='SELECT * FROM clientes WHERE endereço=%s'
        val=(adress,)
        cursor.execute(sq,val)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(cursor):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


    def setupUi(self, pesquisar_cliente_janela):
        pesquisar_cliente_janela.setObjectName("pesquisar_cliente_janela")
        pesquisar_cliente_janela.resize(1038, 436)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("visualizar_cliente_op5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pesquisar_cliente_janela.setWindowIcon(icon)
        self.tableWidget = QtWidgets.QTableWidget(pesquisar_cliente_janela)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 1001, 401))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(250)

        self.retranslateUi(pesquisar_cliente_janela)
        QtCore.QMetaObject.connectSlotsByName(pesquisar_cliente_janela)

    def retranslateUi(self, pesquisar_cliente_janela):
        _translate = QtCore.QCoreApplication.translate
        pesquisar_cliente_janela.setWindowTitle(_translate("pesquisar_cliente_janela", "Clientes"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("pesquisar_cliente_janela", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("pesquisar_cliente_janela", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("pesquisar_cliente_janela", "Endereço"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("pesquisar_cliente_janela", "Valor/Compras"))
