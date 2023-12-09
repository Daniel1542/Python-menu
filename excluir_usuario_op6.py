# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from excluir_usuario_op6_janela import Ui_excluir_usuario
import mysql.connector

database=('loja',)


def conecta_b(b=None):
    if b==None:
        banco=mysql.connector.connect(host='localhost',user='root',password='')
        return banco
    else:
        banco=mysql.connector.connect(host='localhost',user='root',password='',database=b)
        return banco


class Ui_excluir_user(object):

    def buscar(self,nome):
        try:
            banco=conecta_b(database[0])
            cursor=banco.cursor()
            no=nome.strip()
            if no!='':
                sq='SELECT * FROM usuários WHERE login LIKE %s'
                val=(no,)
                cursor.execute(sq,val)
                r=cursor.fetchall()
                if len(r)>0:
                    self.window=QtWidgets.QWidget()
                    self.ui=Ui_excluir_usuario()
                    self.ui.setupUi(self.window)
                    self.ui.transferir(no)
                    self.window.show()
                else:
                    self.label_report.setText('Usuário não encontrado')
            else:
                self.lineEdit_nome.setText('Preencha este campo')
        except BaseException as erro:
            print('erro')+str(erro)
        finally:
            cursor.close()
            banco.close()


    def setupUi(self, excluir_user):
        excluir_user.setObjectName("excluir_user")
        excluir_user.resize(293, 213)
        font = QtGui.QFont()
        font.setPointSize(12)
        excluir_user.setFont(font)
        excluir_user.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("excluir_cliente_op4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        excluir_user.setWindowIcon(icon)
        excluir_user.setStyleSheet('background-color:rgb(255,255,255)')


        self.label_nome = QtWidgets.QLabel(excluir_user)
        self.label_nome.setGeometry(QtCore.QRect(30, 30, 201, 21))
        self.label_nome.setObjectName("label_nome")
        self.lineEdit_nome = QtWidgets.QLineEdit(excluir_user)
        self.lineEdit_nome.setGeometry(QtCore.QRect(30, 70, 201, 20))
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.lineEdit_nome.setMaxLength(15)

        self.pushButton = QtWidgets.QPushButton(excluir_user)
        self.pushButton.setGeometry(QtCore.QRect(70, 110, 75, 23))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:self.buscar(self.lineEdit_nome.text()))


        self.label_report = QtWidgets.QLabel(excluir_user)
        self.label_report.setGeometry(QtCore.QRect(16, 152, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_report.setFont(font)
        self.label_report.setText("")
        self.label_report.setObjectName("label_report")

        self.retranslateUi(excluir_user)
        QtCore.QMetaObject.connectSlotsByName(excluir_user)

    def retranslateUi(self, excluir_user):
        _translate = QtCore.QCoreApplication.translate
        excluir_user.setWindowTitle(_translate("excluir_user", "Excluir usuário"))
        self.label_nome.setText(_translate("excluir_user", "Digite o nome do usuário"))
        self.pushButton.setText(_translate("excluir_user", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    excluir_user = QtWidgets.QWidget()
    ui = Ui_excluir_user()
    ui.setupUi(excluir_user)
    excluir_user.show()
    sys.exit(app.exec_())
