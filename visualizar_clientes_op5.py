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


class Ui_visualizar_clientes(object):

    def visualizar(self):
        try:
            banco = conecta_b(database[0])
            cursor = banco.cursor()
            cursor.execute('SELECT * FROM clientes')
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(cursor):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        except BaseException as erro:
            print('erro')+str(erro)
        finally:
            cursor.close()
            banco.close()


    def setupUi(self, visualizar_clientes):
        visualizar_clientes.setObjectName("visualizar_clientes")
        visualizar_clientes.resize(1050, 440)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("visualizar_cliente_op5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        visualizar_clientes.setWindowIcon(icon)
        self.tableWidget = QtWidgets.QTableWidget(visualizar_clientes)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 1011, 401))
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

        self.retranslateUi(visualizar_clientes)
        QtCore.QMetaObject.connectSlotsByName(visualizar_clientes)

    def retranslateUi(self, visualizar_clientes):
        _translate = QtCore.QCoreApplication.translate
        visualizar_clientes.setWindowTitle(_translate("visualizar_clientes", "Clientes"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("visualizar_clientes", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("visualizar_clientes", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("visualizar_clientes", "Endereço"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("visualizar_clientes", "Valor/Compras"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    visualizar_clientes = QtWidgets.QWidget()
    ui = Ui_visualizar_clientes()
    ui.setupUi(visualizar_clientes)
    ui.visualizar()
    visualizar_clientes.show()
    sys.exit(app.exec_())
