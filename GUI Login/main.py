# Youtube: Magno Efren
# https://www.youtube.com/c/MagnoEfren

from PyQt5.QtWidgets import QMainWindow, QApplication,QLineEdit
from PyQt5.QtGui import QGuiApplication,QIcon
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi 
from PyQt5.QtCore import Qt
import sys

class Login(QMainWindow):
	def __init__(self):
		super(Login, self).__init__()
		loadUi('design.ui', self)
		self.bt_normal.hide()
		self.click_posicion = None
		self.bt_minimize.clicked.connect(lambda :self.showMinimized())
		self.bt_normal.clicked.connect(self.control_bt_normal)
		self.bt_maximize.clicked.connect(self.control_bt_maximize)
		self.bt_close.clicked.connect(lambda: self.close())
           
        # Eliminar barra de titulo y opacidad
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setWindowOpacity(1)
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

		# SizeGrip
		self.gripSize = 10
		self.grip = QtWidgets.QSizeGrip(self)
		self.grip.resize(self.gripSize, self.gripSize)
		# mover ventana
		self.frame_superior.mouseMoveEvent = self.mover_ventana


		icon_user = QIcon("image/user.svg")
		icon_lock = QIcon("image/lock.svg")
		self.lineEdit1.addAction(icon_user, QLineEdit.LeadingPosition) #QLineEdit.TrailingPosition		
		self.lineEdit2.addAction(icon_lock, QLineEdit.LeadingPosition) 


	def  control_bt_normal(self): 
	    self.showNormal()       
	    self.bt_normal.hide()
	    self.bt_maximize.show()

	def  control_bt_maximize(self): 
	    self.showMaximized()
	    self.bt_maximize.hide()
	    self.bt_normal.show()

	## SizeGrip
	def resizeEvent(self, event):
	    rect = self.rect()
	    self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

	## mover ventana
	def mousePressEvent(self, event):
	    self.click_posicion = event.globalPos()

	def mover_ventana(self, event):
	    if self.isMaximized() == False:         
	        if event.buttons() == QtCore.Qt.LeftButton:
	            self.move(self.pos() + event.globalPos() - self.click_posicion)
	            self.click_posicion = event.globalPos()
	            event.accept()
	    if event.globalPos().y() <=5 or event.globalPos().x() <=5 :
	        self.showMaximized()
	        self.bt_maximize.hide()
	        self.bt_normal.show()
	    else:
	        self.showNormal()
	        self.bt_normal.hide()
	        self.bt_maximize.show()
	    
if __name__ == '__main__':
	app = QApplication(sys.argv)
	my_app = Login()
	my_app.show()
	sys.exit(app.exec_())
