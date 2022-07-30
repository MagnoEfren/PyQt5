# PyQt5 con Matplotlib
# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren

import sys
import numpy as np
from GUI import*
from PyQt5 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class MiApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        self.grafica = Canvas_grafica()
        self.ui.verticalLayout_grafica.addWidget(self.grafica)
        self.ui.slider1.valueChanged.connect(self.slider_uno)
        self.ui.slider2.valueChanged.connect(self.slider_dos)

    def slider_uno(self, event):
        self.grafica.datos1(event) 

    def slider_dos(self, event):
        self.grafica.datos2(event) 

class Canvas_grafica(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig , self.ax = plt.subplots(facecolor='gray')
        super().__init__(self.fig) 
        self.ax.grid()
        self.ax.margins(x=0)
        self.nivel1 = 10
        self.nivel2 = 1
        self.grafica_datos()

    def datos1(self, valor1):
        self.nivel1 = valor1*0.1

    def datos2(self, valor2):
        self.nivel2 = valor2*0.05

    def grafica_datos(self):
        plt.title("Grafica en PyQt5 con Matplotlib")
        x = np.arange(-np.pi, 10*np.pi, 0.01) 
        line, = self.ax.plot(x, self.nivel1*np.sin(self.nivel2*x), color='r',linewidth=2)
        self.draw()     
        line.set_ydata(np.sin(x)+24)
        QtCore.QTimer.singleShot(10, self.grafica_datos)


if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())  

