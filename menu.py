# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from menu_cadastrar_op1 import Ui_cadastrar_cliente
from editar_cliente_op2 import Ui_editar_cliente
from pesquisar_cliente_op3 import Ui_pesquisar_cliente
from excluir_cliente_op4 import Ui_excluir_cliente_op4
from visualizar_clientes_op5 import Ui_visualizar_clientes
from excluir_usuario_op6 import Ui_excluir_user


class Ui_menu(object):

    def cadastrar(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_cadastrar_cliente()
        self.ui.setupUi(self.window)
        self.ui.is_validate()
        self.window.show()


    def editar(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_editar_cliente()
        self.ui.setupUi(self.window)
        self.window.show()


    def pesquisar(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_pesquisar_cliente()
        self.ui.setupUi(self.window)
        self.window.show()


    def excluir_cliente(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_excluir_cliente_op4()
        self.ui.setupUi(self.window)
        self.window.show()


    def visualizar(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_visualizar_clientes()
        self.ui.setupUi(self.window)
        self.ui.visualizar()
        self.window.show()


    def excluir_user(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_excluir_user()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, menu):
        menu.setObjectName("menu")
        menu.resize(337, 407)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("menu.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        menu.setWindowIcon(icon)
        menu.setStyleSheet('background-color:rgb(255,255,255)')

        self.label_excluir_cliente = QtWidgets.QLabel(menu)
        self.label_excluir_cliente.setGeometry(QtCore.QRect(30, 250, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_excluir_cliente.setFont(font)
        self.label_excluir_cliente.setObjectName("label_excluir_cliente")
        self.pushButton_excluir_user = QtWidgets.QPushButton(menu)
        self.pushButton_excluir_user.setGeometry(QtCore.QRect(230, 350, 75, 31))
        self.pushButton_excluir_user.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_excluir_user.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("menu-botoes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_excluir_user.setIcon(icon1)
        self.pushButton_excluir_user.setObjectName("pushButton_excluir_user")
        self.pushButton_excluir_user.clicked.connect(self.excluir_user)


        self.label_menu = QtWidgets.QLabel(menu)
        self.label_menu.setGeometry(QtCore.QRect(140, 30, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_menu.setFont(font)
        self.label_menu.setObjectName("label_menu")
        self.pushButton_pesquisar = QtWidgets.QPushButton(menu)
        self.pushButton_pesquisar.setGeometry(QtCore.QRect(230, 200, 75, 31))
        self.pushButton_pesquisar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_pesquisar.setText("")
        self.pushButton_pesquisar.setIcon(icon1)
        self.pushButton_pesquisar.setObjectName("pushButton_pesquisar")
        self.pushButton_pesquisar.clicked.connect(self.pesquisar)


        self.pushButton_visualizar = QtWidgets.QPushButton(menu)
        self.pushButton_visualizar.setGeometry(QtCore.QRect(230, 300, 75, 31))
        self.pushButton_visualizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_visualizar.setText("")
        self.pushButton_visualizar.setIcon(icon1)
        self.pushButton_visualizar.setObjectName("pushButton_visualizar")
        self.pushButton_visualizar.clicked.connect(self.visualizar)


        self.label_pesquisar = QtWidgets.QLabel(menu)
        self.label_pesquisar.setGeometry(QtCore.QRect(30, 200, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_pesquisar.setFont(font)
        self.label_pesquisar.setObjectName("label_pesquisar")
        self.label_cadastrar = QtWidgets.QLabel(menu)
        self.label_cadastrar.setGeometry(QtCore.QRect(30, 100, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_cadastrar.setFont(font)
        self.label_cadastrar.setObjectName("label_cadastrar")
        self.pushButton_cadastrar = QtWidgets.QPushButton(menu)
        self.pushButton_cadastrar.setGeometry(QtCore.QRect(230, 100, 75, 31))
        self.pushButton_cadastrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_cadastrar.setText("")
        self.pushButton_cadastrar.setIcon(icon1)
        self.pushButton_cadastrar.setObjectName("pushButton_cadastrar")
        self.pushButton_cadastrar.clicked.connect(self.cadastrar)


        self.label_exclui_user = QtWidgets.QLabel(menu)
        self.label_exclui_user.setGeometry(QtCore.QRect(30, 350, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_exclui_user.setFont(font)
        self.label_exclui_user.setObjectName("label_exclui_user")
        self.label_editar = QtWidgets.QLabel(menu)
        self.label_editar.setGeometry(QtCore.QRect(30, 150, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_editar.setFont(font)
        self.label_editar.setObjectName("label_editar")
        self.label_relatorio = QtWidgets.QLabel(menu)
        self.label_relatorio.setGeometry(QtCore.QRect(30, 300, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_relatorio.setFont(font)
        self.label_relatorio.setObjectName("label_relatorio")
        self.pushButton_editar = QtWidgets.QPushButton(menu)
        self.pushButton_editar.setGeometry(QtCore.QRect(230, 150, 75, 31))
        self.pushButton_editar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_editar.setText("")
        self.pushButton_editar.setIcon(icon1)
        self.pushButton_editar.setObjectName("pushButton_editar")
        self.pushButton_editar.clicked.connect(self.editar)


        self.pushButton_excluir_cliente = QtWidgets.QPushButton(menu)
        self.pushButton_excluir_cliente.setGeometry(QtCore.QRect(230, 250, 75, 31))
        self.pushButton_excluir_cliente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_excluir_cliente.setText("")
        self.pushButton_excluir_cliente.setIcon(icon1)
        self.pushButton_excluir_cliente.setObjectName("pushButton_excluir_cliente")
        self.pushButton_excluir_cliente.clicked.connect(self.excluir_cliente)


        self.retranslateUi(menu)
        QtCore.QMetaObject.connectSlotsByName(menu)

    def retranslateUi(self, menu):
        _translate = QtCore.QCoreApplication.translate
        menu.setWindowTitle(_translate("menu", "Menu"))
        self.label_excluir_cliente.setText(_translate("menu", "4-Excluir cliente"))
        self.label_menu.setText(_translate("menu", "Menu"))
        self.label_pesquisar.setText(_translate("menu", "3-Pesquisar cliente"))
        self.label_cadastrar.setText(_translate("menu", "1-Cadastrar cliente"))
        self.label_exclui_user.setText(_translate("menu", "6-Excluir usuário"))
        self.label_editar.setText(_translate("menu", "2-Editar cliente"))
        self.label_relatorio.setText(_translate("menu", "5-Visualizar clientes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menu = QtWidgets.QWidget()
    ui = Ui_menu()
    ui.setupUi(menu)
    menu.show()
    sys.exit(app.exec_())
