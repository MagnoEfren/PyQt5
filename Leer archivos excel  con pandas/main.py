# Leer archivos excel desde una GUI en PyQt5 
# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren
import sys
from tabla import*
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog, QMessageBox
import pandas as pd

class MiApp(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow() 
		self.ui.setupUi(self)		
		self.ui.bt_abrir.clicked.connect(self.abrir_archivo)
		self.ui.pushButton.clicked.connect(self.crear_tabla)

	def abrir_archivo(self):
		file = QFileDialog.getOpenFileName(self,"Abrir Archivo Excel", "","Excel Files (*.xlsx) ;; All Files (*)")
		self.direccion = file[0]
	def crear_tabla(self):
		try:	
			df = pd.read_excel(self.direccion)
			columnas = list(df.columns)
			df_fila = df.to_numpy().tolist()
			x = len(columnas)
			y = len(df_fila)
		except ValueError:
			QMessageBox.about (self,'Informacion', 'Formato incorrecto')
			return None
		except FileNotFoundError:
			QMessageBox.about (self,'Informacion', 'El archivo esta \n malogrado')
			return None
		#print(x, y)
		self.ui.tableWidget.setRowCount(y)
		self.ui.tableWidget.setColumnCount(x)

		for j in range(x):
			#print(columnas[j])
			encabezado = QtWidgets.QTableWidgetItem(columnas[j])
			self.ui.tableWidget.setHorizontalHeaderItem(j,encabezado )
			for i in range(y):
				dato = str(df_fila[i][j])
				if dato == 'nan':
					dato =''
				self.ui.tableWidget.setItem(i,j, QTableWidgetItem(dato))
		#print(df_fila)
if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())
