# Calculadora  Basica en Python con PyQt5
# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren
import sys      
from Calculadora import *

class MiFormulario(QtWidgets.QWidget):
	def __init__(self, parent=None):   
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_Form()  
		self.ui.setupUi(self)
		self.ui.boton_cero.clicked.connect(self.obtener)
		self.ui.boton_uno.clicked.connect(self.obtener1)
		self.ui.boton_dos.clicked.connect(self.obtener2)
		self.ui.boton_tres.clicked.connect(self.obtener3)
		self.ui.boton_cuatro.clicked.connect(self.obtener4)
		self.ui.boton_cinco.clicked.connect(self.obtener5)
		self.ui.boton_seis.clicked.connect(self.obtener6)
		self.ui.boton_siete.clicked.connect(self.obtener7)		
		self.ui.boton_ocho.clicked.connect(self.obtener8)  
		self.ui.boton_nueve.clicked.connect(self.obtener9)   
		self.ui.boton_menos.clicked.connect(self.obtener10)     
		self.ui.boton_mas.clicked.connect(self.obtener11)
		self.ui.boton_por.clicked.connect(self.obtener12)
		self.ui.boton_entre.clicked.connect(self.obtener13)		
		self.ui.boton_100.clicked.connect(self.obtener14)
		self.ui.boton_igual.clicked.connect(self.obtener15)
		self.ui.boton_abrir.clicked.connect(self.obtener16)
		self.ui.boton_cerrar.clicked.connect(self.obtener17)
		self.ui.boton_punto.clicked.connect(self.obtener18)
		self.ui.boton_ac.clicked.connect(self.obtener19)

	def obtener(self):
		entrada= self.ui.valor.text()
		entrada += "0"
		self.ui.valor.setText(entrada)
	def obtener1(self):
		entrada= self.ui.valor.text()
		entrada += "1"
		self.ui.valor.setText(entrada)
	def obtener2(self):
		entrada= self.ui.valor.text()
		entrada += "2"
		self.ui.valor.setText(entrada)
	def obtener3(self):
		entrada= self.ui.valor.text()
		entrada += "3"
		self.ui.valor.setText(entrada)
	def obtener4(self):
		entrada= self.ui.valor.text()
		entrada += "4"
		self.ui.valor.setText(entrada)
	def obtener5(self):
		entrada= self.ui.valor.text()
		entrada += "5"
		self.ui.valor.setText(entrada)
	def obtener6(self):
		entrada= self.ui.valor.text()
		entrada += "6"
		self.ui.valor.setText(entrada)		
	def obtener7(self):
		entrada= self.ui.valor.text()
		entrada += "7"
		self.ui.valor.setText(entrada)
	def obtener8(self):
		entrada= self.ui.valor.text()
		entrada += "8"
		self.ui.valor.setText(entrada)
	def obtener9(self):
		entrada= self.ui.valor.text()
		entrada += "9"
		self.ui.valor.setText(entrada)		
	def obtener10(self):
		entrada= self.ui.valor.text()
		entrada += "-"
		self.ui.valor.setText(entrada)
	def obtener11(self):
		entrada= self.ui.valor.text()
		entrada += "+"
		self.ui.valor.setText(entrada)	
	def obtener12(self):
		entrada= self.ui.valor.text()
		entrada += "*"
		self.ui.valor.setText(entrada)
	def obtener13(self):
		entrada= self.ui.valor.text()
		entrada += "/"
		self.ui.valor.setText(entrada)      
	def obtener14(self):
		entrada= self.ui.valor.text()
		try:
			self.an = (entrada+"/100")
			self.ui.valor.setText(self.an)
		except:
			self.ui.valor.setText("")

	def obtener15(self):
		entrada= self.ui.valor.text()
		try:
				ans= eval(entrada)
				self.ui.valor.setText(str(ans))
		except:
				self.ui.valor.setText("ERROR") 
	def obtener16(self):
		entrada = self.ui.valor.text()
		entrada += "("
		self.ui.valor.setText(entrada)      
	def obtener17(self):
		entrada = self.ui.valor.text()
		entrada += ")"
		self.ui.valor.setText(entrada)

	def obtener18(self):
		entrada = self.ui.valor.text()
		entrada += "."
		self.ui.valor.setText(entrada) 

	def obtener19(self):
		entrada = self.ui.valor.text()
		self.ui.valor.setText(entrada[:len(entrada)-1])
if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv) 
	mi_app = MiFormulario()    
	mi_app.show()				
	sys.exit(app.exec_())		         
