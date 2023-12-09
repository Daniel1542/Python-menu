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


class Ui_excluir_usuario(object):

    def message(self):
        ms=QMessageBox()
        ms.setText('Nenhuma mudança feita')
        ms.setWindowTitle('Sem mudança')
        ms.setDefaultButton(QMessageBox.Ok)
        if QMessageBox.Ok:
            pass
        ms.exec_()

    def transferir(self,nome):
        try:
            banco=conecta_b(database[0])
            cursor=banco.cursor()
            sq='SELECT * FROM usuários WHERE login LIKE %s'
            val=(nome,)
            cursor.execute(sq,val)
            r=cursor.fetchall()
            for n in r:
                print(n)
                self.lineEdit_login.setText(str(n[1]))
                self.lineEdit_senha.setText(str(n[2]))
        except BaseException as erro:
            print('erro')+str(erro)
        finally:
            cursor.close()
            banco.close()


    def deletar(self,nome):
        try:
            banco=conecta_b(database[0])
            cursor=banco.cursor()
            if nome!='':
                sq='SELECT * FROM usuários WHERE login LIKE %s'
                val=(nome,)
                cursor.execute(sq, val)
                r=cursor.fetchone()
                if r[1]=='adm':
                    self.label_report.setText('Você não pode excluir o adm')
                else:
                    cursor.execute('DELETE FROM usuários WHERE usuários.id='+str(r[0]))
                    banco.commit()
                    self.lineEdit_login.setText('')
                    self.lineEdit_senha.setText('')
                    self.label_report.setText('Usuário excluído')
            else:
                self.label_report.setText('Você pode fechar esta janela')
        except BaseException as erro:
            print('erro')+str(erro)
        finally:
            cursor.close()
            banco.close()


    def op_nao(self):
        try:
            self.lineEdit_login.setText('')
            self.lineEdit_senha.setText('')
            self.label_report.setText('Nada mudado')
            self.message()
        except BaseException as erro:
            print('erro') + str(erro)


    def setupUi(self, excluir_usuario):
        excluir_usuario.setObjectName("excluir_usuario")
        excluir_usuario.resize(313, 284)
        font = QtGui.QFont()
        font.setPointSize(12)
        excluir_usuario.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("excluir_cliente_op4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        excluir_usuario.setWindowIcon(icon)
        excluir_usuario.setStyleSheet('background-color:rgb(255,255,255)')


        self.label_login = QtWidgets.QLabel(excluir_usuario)
        self.label_login.setGeometry(QtCore.QRect(30, 80, 47, 21))
        self.label_login.setObjectName("label_login")
        self.label_senha = QtWidgets.QLabel(excluir_usuario)
        self.label_senha.setGeometry(QtCore.QRect(30, 130, 47, 21))
        self.label_senha.setObjectName("label_senha")
        self.lineEdit_login = QtWidgets.QLineEdit(excluir_usuario)
        self.lineEdit_login.setGeometry(QtCore.QRect(100, 80, 171, 20))
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.lineEdit_login.setReadOnly(True)


        self.lineEdit_senha = QtWidgets.QLineEdit(excluir_usuario)
        self.lineEdit_senha.setGeometry(QtCore.QRect(100, 130, 171, 20))
        self.lineEdit_senha.setObjectName("lineEdit_senha")
        self.lineEdit_senha.setReadOnly(True)


        self.pushButton_sim = QtWidgets.QPushButton(excluir_usuario)
        self.pushButton_sim.setGeometry(QtCore.QRect(60, 180, 75, 23))
        self.pushButton_sim.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_sim.setIcon(icon)
        self.pushButton_sim.setObjectName("pushButton_sim")
        self.pushButton_sim.clicked.connect(lambda:self.deletar(self.lineEdit_login.text()))


        self.pushButton_nao = QtWidgets.QPushButton(excluir_usuario)
        self.pushButton_nao.setGeometry(QtCore.QRect(200, 180, 75, 21))
        self.pushButton_nao.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("excluir_cliente_op4_btn_nao.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_nao.setIcon(icon1)
        self.pushButton_nao.setObjectName("pushButton_nao")
        self.pushButton_nao.clicked.connect(self.op_nao)


        self.label_titulo = QtWidgets.QLabel(excluir_usuario)
        self.label_titulo.setGeometry(QtCore.QRect(100, 30, 121, 21))
        self.label_titulo.setObjectName("label_titulo")
        self.label_report = QtWidgets.QLabel(excluir_usuario)
        self.label_report.setGeometry(QtCore.QRect(20, 222, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_report.setFont(font)
        self.label_report.setText("")
        self.label_report.setObjectName("label_report")

        self.retranslateUi(excluir_usuario)
        QtCore.QMetaObject.connectSlotsByName(excluir_usuario)

    def retranslateUi(self, excluir_usuario):
        _translate = QtCore.QCoreApplication.translate
        excluir_usuario.setWindowTitle(_translate("excluir_usuario", "Excluir usuário"))
        self.label_login.setText(_translate("excluir_usuario", "Login:"))
        self.label_senha.setText(_translate("excluir_usuario", "Senha:"))
        self.pushButton_sim.setText(_translate("excluir_usuario", "Sim"))
        self.pushButton_nao.setText(_translate("excluir_usuario", "Não"))
        self.label_titulo.setText(_translate("excluir_usuario", "Excluir usuário?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    excluir_usuario = QtWidgets.QWidget()
    ui = Ui_excluir_usuario()
    ui.setupUi(excluir_usuario)
    excluir_usuario.show()
    sys.exit(app.exec_())
