# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculadora.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(342, 311)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icono.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.boton_uno = QtWidgets.QPushButton(Form)
        self.boton_uno.setGeometry(QtCore.QRect(12, 52, 75, 35))
        self.boton_uno.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.boton_uno.setObjectName("boton_uno")
        self.boton_dos = QtWidgets.QPushButton(Form)
        self.boton_dos.setGeometry(QtCore.QRect(93, 52, 75, 35))
        self.boton_dos.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.boton_dos.setObjectName("boton_dos")
        self.boton_tres = QtWidgets.QPushButton(Form)
        self.boton_tres.setGeometry(QtCore.QRect(174, 52, 75, 35))
        self.boton_tres.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.boton_tres.setObjectName("boton_tres")
        self.boton_abrir = QtWidgets.QPushButton(Form)
        self.boton_abrir.setGeometry(QtCore.QRect(255, 52, 75, 35))
        self.boton_abrir.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"font: 87 14pt \"Arial Black\";")
        self.boton_abrir.setObjectName("boton_abrir")
        self.valor = QtWidgets.QLabel(Form)
        self.valor.setGeometry(QtCore.QRect(10, 10, 321, 31))
        self.valor.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.valor.setText("")
        self.valor.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.valor.setIndent(0)
        self.valor.setObjectName("valor")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 321, 31))
        self.label_2.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setIndent(0)
        self.label_2.setObjectName("label_2")
        self.boton_cinco = QtWidgets.QPushButton(Form)
        self.boton_cinco.setGeometry(QtCore.QRect(93, 95, 75, 35))
        self.boton_cinco.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.boton_cinco.setObjectName("boton_cinco")
        self.boton_seis = QtWidgets.QPushButton(Form)
        self.boton_seis.setGeometry(QtCore.QRect(174, 95, 75, 35))
        self.boton_seis.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.boton_seis.setObjectName("boton_seis")
        self.boton_cerrar = QtWidgets.QPushButton(Form)
        self.boton_cerrar.setGeometry(QtCore.QRect(255, 95, 75, 35))
        self.boton_cerrar.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"font: 87 14pt \"Arial Black\";")
        self.boton_cerrar.setObjectName("boton_cerrar")
        self.boton_cuatro = QtWidgets.QPushButton(Form)
        self.boton_cuatro.setGeometry(QtCore.QRect(12, 95, 75, 35))
        self.boton_cuatro.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.boton_cuatro.setObjectName("boton_cuatro")
        self.boton_mas = QtWidgets.QPushButton(Form)
        self.boton_mas.setGeometry(QtCore.QRect(12, 181, 75, 35))
        self.boton_mas.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"font: 87 14pt \"Arial Black\";")
        self.boton_mas.setObjectName("boton_mas")
        self.boton_c = QtWidgets.QPushButton(Form)
        self.boton_c.setGeometry(QtCore.QRect(174, 181, 75, 35))
        self.boton_c.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"font: 87 14pt \"Arial Black\";")
        self.boton_c.setObjectName("boton_c")
        self.boton_cero = QtWidgets.QPushButton(Form)
        self.boton_cero.setGeometry(QtCore.QRect(93, 181, 75, 35))
        self.boton_cero.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.boton_cero.setObjectName("boton_cero")
        self.boton_menos = QtWidgets.QPushButton(Form)
        self.boton_menos.setGeometry(QtCore.QRect(12, 267, 75, 35))
        self.boton_menos.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"font: 87 14pt \"Arial Black\";")
        self.boton_menos.setObjectName("boton_menos")
        self.boton_100 = QtWidgets.QPushButton(Form)
        self.boton_100.setGeometry(QtCore.QRect(93, 267, 75, 35))
        self.boton_100.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"font: 87 14pt \"Arial Black\";")
        self.boton_100.setObjectName("boton_100")
        self.boton_salir = QtWidgets.QPushButton(Form)
        self.boton_salir.setGeometry(QtCore.QRect(174, 267, 155, 35))
        self.boton_salir.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 87 14pt \"Arial Black\";")
        self.boton_salir.setObjectName("boton_salir")
        self.boton_ac = QtWidgets.QPushButton(Form)
        self.boton_ac.setGeometry(QtCore.QRect(174, 224, 75, 35))
        self.boton_ac.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"font: 87 14pt \"Arial Black\";")
        self.boton_ac.setObjectName("boton_ac")
        self.boton_por = QtWidgets.QPushButton(Form)
        self.boton_por.setGeometry(QtCore.QRect(12, 224, 75, 35))
        self.boton_por.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"font: 87 14pt \"Arial Black\";")
        self.boton_por.setObjectName("boton_por")
        self.boton_entre = QtWidgets.QPushButton(Form)
        self.boton_entre.setGeometry(QtCore.QRect(93, 224, 75, 35))
        self.boton_entre.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"font: 87 14pt \"Arial Black\";")
        self.boton_entre.setObjectName("boton_entre")
        self.boton_igual = QtWidgets.QPushButton(Form)
        self.boton_igual.setGeometry(QtCore.QRect(255, 181, 75, 76))
        self.boton_igual.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 87 14pt \"Arial Black\";")
        self.boton_igual.setObjectName("boton_igual")
        self.boton_ocho = QtWidgets.QPushButton(Form)
        self.boton_ocho.setGeometry(QtCore.QRect(93, 138, 75, 35))
        self.boton_ocho.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.boton_ocho.setObjectName("boton_ocho")
        self.boton_siete = QtWidgets.QPushButton(Form)
        self.boton_siete.setGeometry(QtCore.QRect(12, 138, 75, 35))
        self.boton_siete.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.boton_siete.setObjectName("boton_siete")
        self.boton_nueve = QtWidgets.QPushButton(Form)
        self.boton_nueve.setGeometry(QtCore.QRect(174, 138, 75, 35))
        self.boton_nueve.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.boton_nueve.setObjectName("boton_nueve")
        self.boton_punto = QtWidgets.QPushButton(Form)
        self.boton_punto.setGeometry(QtCore.QRect(255, 138, 75, 35))
        self.boton_punto.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"font: 87 14pt \"Arial Black\";")
        self.boton_punto.setObjectName("boton_punto")
        self.label_2.raise_()
        self.boton_uno.raise_()
        self.boton_dos.raise_()
        self.boton_tres.raise_()
        self.boton_abrir.raise_()
        self.valor.raise_()

        self.retranslateUi(Form)
        self.boton_salir.clicked.connect(Form.close)
        self.boton_c.clicked.connect(self.valor.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculadora"))
        self.boton_uno.setText(_translate("Form", "1"))
        self.boton_uno.setShortcut(_translate("Form", "1"))
        self.boton_dos.setText(_translate("Form", "2"))
        self.boton_dos.setShortcut(_translate("Form", "2"))
        self.boton_tres.setText(_translate("Form", "3"))
        self.boton_tres.setShortcut(_translate("Form", "3"))
        self.boton_abrir.setText(_translate("Form", "("))
        self.boton_abrir.setShortcut(_translate("Form", "Ctrl+8"))
        self.boton_cinco.setText(_translate("Form", "5"))
        self.boton_cinco.setShortcut(_translate("Form", "5"))
        self.boton_seis.setText(_translate("Form", "6"))
        self.boton_seis.setShortcut(_translate("Form", "6"))
        self.boton_cerrar.setText(_translate("Form", ")"))
        self.boton_cerrar.setShortcut(_translate("Form", "Ctrl+9"))
        self.boton_cuatro.setText(_translate("Form", "4"))
        self.boton_mas.setText(_translate("Form", "+"))
        self.boton_mas.setShortcut(_translate("Form", "+"))
        self.boton_c.setText(_translate("Form", "C"))
        self.boton_c.setShortcut(_translate("Form", "Esc"))
        self.boton_cero.setText(_translate("Form", "0"))
        self.boton_menos.setText(_translate("Form", "-"))
        self.boton_menos.setShortcut(_translate("Form", "-"))
        self.boton_100.setText(_translate("Form", "%"))
        self.boton_salir.setText(_translate("Form", "SALIR"))
        self.boton_ac.setText(_translate("Form", "AC"))
        self.boton_ac.setShortcut(_translate("Form", "Backspace"))
        self.boton_por.setText(_translate("Form", "x"))
        self.boton_por.setShortcut(_translate("Form", "Ctrl++"))
        self.boton_entre.setText(_translate("Form", "÷"))
        self.boton_entre.setShortcut(_translate("Form", "Ctrl+7"))
        self.boton_igual.setText(_translate("Form", "="))
        self.boton_igual.setShortcut(_translate("Form", "Space"))
        self.boton_ocho.setText(_translate("Form", "8"))
        self.boton_ocho.setShortcut(_translate("Form", "8"))
        self.boton_siete.setText(_translate("Form", "7"))
        self.boton_siete.setShortcut(_translate("Form", "7"))
        self.boton_nueve.setText(_translate("Form", "9"))
        self.boton_nueve.setShortcut(_translate("Form", "9"))
        self.boton_punto.setText(_translate("Form", "."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

