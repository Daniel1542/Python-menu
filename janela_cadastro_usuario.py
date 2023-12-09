# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_janela_cadastro(object):
    def setupUi(self, janela_cadastro):
        janela_cadastro.setObjectName("janela_cadastro")
        janela_cadastro.resize(236, 138)
        font = QtGui.QFont()
        font.setPointSize(12)
        janela_cadastro.setFont(font)
        self.label = QtWidgets.QLabel(janela_cadastro)
        self.label.setGeometry(QtCore.QRect(50, 30, 161, 31))
        self.label.setObjectName("label")

        self.retranslateUi(janela_cadastro)
        QtCore.QMetaObject.connectSlotsByName(janela_cadastro)

    def retranslateUi(self, janela_cadastro):
        _translate = QtCore.QCoreApplication.translate
        janela_cadastro.setWindowTitle(_translate("janela_cadastro", "cadastrado"))
        self.label.setText(_translate("janela_cadastro", "Usuário Cadastrado"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    janela_cadastro = QtWidgets.QWidget()
    ui = Ui_janela_cadastro()
    ui.setupUi(janela_cadastro)
    janela_cadastro.show()
    sys.exit(app.exec_())
