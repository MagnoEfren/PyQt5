# ProgressBar Circular Arduino y PyQt5
# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren

from PyQt5.QtCore import QObject, pyqtSignal,pyqtSlot 
import serial, serial.tools.list_ports
from threading import Thread, Event

class Comunicacion(QObject):                                                   
	datos_recibidos = pyqtSignal(str) 

	def __init__(self):
		super().__init__()
		self.arduino  = serial.Serial()
		self.arduino.timeout = 0.5		
		
		self.baudrates = ['1200', '2400', '4800', '9600', '19200', '38400', '115200']
		self.puertos = []

		self.hilo = None
		self.alive = Event() #indica que esta activo

	def puertos_disponibles(self):
		self.puertos = [port.device for port in serial.tools.list_ports.comports()]

	def conexion_serial(self):
		try:	
			self.arduino.open()
		except:
			pass

		if (self.arduino.is_open): # iniciamos el hilo cuando puerto esta abierto
			self.iniciar_hilo()  


	def desconectar(self):
		self.stop_hilo()
		self.arduino.close()

	def leer_datos(self):
		while(self.alive.isSet() and self.arduino.is_open):
			
			data = self.arduino.readline().decode("utf-8").strip() 
			if(len(data)>1): 
				self.datos_recibidos.emit(data) 			


	def iniciar_hilo(self):
		self.hilo = Thread(target= self.leer_datos) 
		self.hilo.setDaemon(1) 
		self.alive.set()		 
		self.hilo.start()	

	def stop_hilo(self):
		if(self.hilo is not None):
			self.alive.clear()
			self.hilo.join()
			self.hilo = None	
