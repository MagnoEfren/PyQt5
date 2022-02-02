# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabla.ui'
# Created by: PyQt5 UI code generator 5.12.3
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(676, 441)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("background-color: rgb(128, 111, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_abrir = QtWidgets.QPushButton(self.frame_2)
        self.bt_abrir.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(0, 255, 127);\n"
"    font: 87 10pt \"Arial\";\n"
"border:1px solid #000000;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(0, 0, 255);\n"
"    font: 87 10pt \"Arial\";\n"
"border:1px solid #000000;\n"
"    border-radius:5px;\n"
"}")
        self.bt_abrir.setObjectName("bt_abrir")
        self.horizontalLayout.addWidget(self.bt_abrir)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(0, 170, 0);\n"
"    font: 87 10pt \"Arial \";\n"
"border:1px solid #000000;\n"
"    border-radius:5px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(85, 255, 0);\n"
"    font: 87 10pt \"Arial \";\n"
"border:1px solid #000000;\n"
"    border-radius:5px;\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setStyleSheet("font: 75 20pt \"Rockwell Condensed\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.bt_salir = QtWidgets.QPushButton(self.frame_2)
        self.bt_salir.setStyleSheet("\n"
"QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"    font: 87 10pt \"Arial\";\n"
"border:1px solid #000000;\n"
"    border-radius:5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 87 10pt \"Arial\";\n"
"border:1px solid #000000;\n"
"    border-radius:5px;\n"
"\n"
"}")
        self.bt_salir.setObjectName("bt_salir")
        self.horizontalLayout.addWidget(self.bt_salir)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setStyleSheet("QWidget {\n"
"    background-color: #ffffff;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #aa00ff;\n"
"    padding: 2px;\n"
"\n"
"    border: 1px solid #fffff8;\n"
"    font-size: 14pt;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    gridline-color: #aa00ff;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #646464;\n"
"    border: 1px solid #ff0000;\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout.setStretch(0, 10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.bt_salir.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Leer archivos Excel"))
        self.bt_abrir.setText(_translate("MainWindow", "ABRIR ARCHIVO"))
        self.pushButton.setText(_translate("MainWindow", "MOSTRAR DATOS"))
        self.label.setText(_translate("MainWindow", "LEER ARCHIVOS EXCEL"))
        self.bt_salir.setText(_translate("MainWindow", "SALIR"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
