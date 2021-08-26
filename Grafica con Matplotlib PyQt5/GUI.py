# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(627, 345)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(400, 200))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_grafica = QtWidgets.QVBoxLayout()
        self.verticalLayout_grafica.setObjectName("verticalLayout_grafica")
        self.horizontalLayout.addLayout(self.verticalLayout_grafica)
        self.frame_control = QtWidgets.QFrame(self.frame)
        self.frame_control.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_control.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.frame_control.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_control.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_control.setObjectName("frame_control")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_control)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_control)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 10pt \"Arial Black\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.slider1 = QtWidgets.QSlider(self.frame_control)
        self.slider1.setMinimumSize(QtCore.QSize(0, 30))
        self.slider1.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #00ff00;\n"
"    height: 4px; \n"
"    background: #00ff00;\n"
" \n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background:   rgb(215, 0, 255);\n"
"    \n"
"    width: 28px;\n"
"    height:28px;\n"
"\n"
"left: 11px;\n"
"right: 11px;\n"
"\n"
"\n"
"    margin: -12px; \n"
"    border-radius:14px;\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal{\n"
"background-color:white;\n"
"border: 1px solid white;\n"
"}\n"
"")
        self.slider1.setMaximum(100)
        self.slider1.setSingleStep(1)
        self.slider1.setOrientation(QtCore.Qt.Horizontal)
        self.slider1.setObjectName("slider1")
        self.verticalLayout_2.addWidget(self.slider1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.slider2 = QtWidgets.QSlider(self.frame_control)
        self.slider2.setMinimumSize(QtCore.QSize(0, 30))
        self.slider2.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #00ff00;\n"
"    height: 4px; \n"
"    background: #00ff00;\n"
" \n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background:   rgb(245, 10, 15);\n"
"    \n"
"\n"
"    width: 28px;\n"
"    height:28px;\n"
"\n"
"left: 11px;\n"
"right: 11px;\n"
"\n"
"\n"
"    margin: -12px; \n"
"    border-radius:14px;\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal{\n"
"background-color:white;\n"
"border: 1px solid white;\n"
"}\n"
"")
        self.slider2.setMaximum(100)
        self.slider2.setSingleStep(1)
        self.slider2.setOrientation(QtCore.Qt.Horizontal)
        self.slider2.setObjectName("slider2")
        self.verticalLayout_2.addWidget(self.slider2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.frame_control)
        self.pushButton.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout.addWidget(self.frame_control)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "VARIAR AMPLITUD Y FRECUENCIA"))
        self.pushButton.setText(_translate("MainWindow", "SALIR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
