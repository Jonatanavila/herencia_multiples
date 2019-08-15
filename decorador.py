def cargar_limite(limt):
	def nuevo_limt(self):
		if self.kilos > 300:
			print("el camion esta no va arrancar porque tiene sobre carga")
		limt(self)

	return nuevo_limt

def verifico_rueda(func):
	def nueva_funcion(self):
		print("revisar la rueda antes de empezar a andar")
		func(self)

	return nueva_funcion

class vehiculo():
	def __init__(self):
		self.posicion= 0

class auto(vehiculo):
	def __init__(self,**kw):
		super().__init__(**kw)

	def tipo(self):
		print("auto")

	def andar(self):
		self.posicion += 20

	def ver_posicion(self):
		print (self.posicion)

	def verificar_rueda(self):
		if self.posicion %100== 0: 
			print("rotar rueda") 
		else:
			print("no rotar")

class camion(vehiculo):
	def __init__(self,**kw):
		super().__init__(**kw)

	@verifico_rueda
	@cargar_limite
	def andar(self):
		self.posicion +=5

	def tipo(self):
		print ("camion")

	def cargar(self,kilos):
		self.kilos = kilos
		print ((str(self.kilos)) + " " + "kgs cargados correctamente")

	def verificar_rueda(self):
		if self.posicion %20== 0: 
			print("rotar rueda") 
		else:
			print("no rotar")
		
def manejar_vehiculo(vehiculo):
	for i in range (3):
		vehiculo.andar()
	print ("el vehiculo quedo:" + (str(vehiculo.posicion)))


