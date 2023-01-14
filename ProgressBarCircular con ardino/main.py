# ProgressBar Circular Arduino y PyQt5
# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren
import sys
from ui_progressBarCircular import *
from comunicacion_serial import Comunicacion
from PyQt5.QtCore import QTimer  

class MiApp(QtWidgets.QMainWindow):
	def __init__(self,*args, **kwargs):
		super().__init__()
		self.ui = Ui_MainWindow() 
		self.ui.setupUi(self)

		self.serial = Comunicacion()
		self.puertos_disponible()
		self.nivel = 0.0

		self.serial.datos_recibidos.connect(self.datos_arduino)
		self.ui.velocidad.addItems(self.serial.baudrates)
		self.ui.velocidad.setCurrentText("9600")

		self.ui.conectar.clicked.connect(self.conectar)
		self.ui.actualizar.clicked.connect(self.mostrar_barra)
		self.ui.desconectar.clicked.connect(self.desconectar)

	def datos_arduino(self, data):
		self.nivel = float(data)

	def conectar(self):		
		port = self.ui.puertos.currentText()   
		baud = self.ui.velocidad.currentText()   
		self.serial.arduino.port = port      
		self.serial.arduino.baudrate = baud  
		self.serial.conexion_serial()    

	def desconectar(self):
		self.serial.desconectar()

	def mostrar_barra(self):		
		self.progressbar()		
		QTimer.singleShot(20, self.mostrar_barra)

	def puertos_disponible(self):
		self.serial.puertos_disponibles()
		self.ui.puertos.clear()
		self.ui.puertos.addItems(self.serial.puertos)
		
	def progressbar(self):		
		estilo = """ QFrame{	
   			border-radius: 150px;
			background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{stop1}  
			rgba(255, 0, 55, 255), stop:{stop2} rgba(255, 0, 0, 30));
		}"""
		val = (self.nivel)/4.91
		stop1 = str(abs(val - 0.001))
		stop2 = str(val)
		valor1 = int(float(stop1)*1000)
		valor2 = int(float(stop2)*1000)
		if (valor1>=0 and valor2<=1000) and (valor2>=0 and valor1<=1000):	
			nuevo_estilo = estilo.replace('{stop1}', stop1).replace('{stop2}', stop2)
			self.ui.voltaje.setText(str(self.nivel))
			self.ui.progressbar.setStyleSheet(nuevo_estilo)
if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())		
