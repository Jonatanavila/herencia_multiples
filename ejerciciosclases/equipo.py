class partido:
	def __init__(self,nombre,año_de_fundacion,color,cantidad_jugadores,**kw):
		self.nombre=nombre
		self.año_de_fundacion=año_de_fundacion
		self.color=color
		self.cantidad_jugadores=cantidad_jugadores
		print(nombre,año_de_fundacion,color,cantidad_jugadores)

	def __str__(self):
		return "nombre: {},año_de_fundacion: {},color: {}".format(self.nombre,self.año_de_fundacion,self.color)

	def __cmp__(self,otro):
			diferencia = (self.cantidad_jugadores) - (otro.cantidad_jugadores)
			if diferencia < 0:
					return -1
			elif diferencia > 0:
					return 1
			else:
					return 0

class equipo(partido):
	def __init__(self,**kw):
		super().__init__(**kw)
	
	def jugar(self):
		if self.cantidad_jugadores > 11:
			print("tiene equipoco completo y puede jugar")
		else:
			print("no se puede jugar el partido")

class jugadores(partido):
	def __init__(self,altura,**kw):
		self.altura=altura
		super().__init__(**kw)
		print(altura)

	def posicion(self):
		self.posicion=0

	def correr(self):
		self.pocision +=10

	def dar_pase(self):
		if self.posicion %20==0:
			print ("tocar pase")
		else:
			print("no tocar pase")
	
if __name__ == '__main__':
	par=equipo(altura=1.75,nombre="jonatan",año_de_fundacion=1993,color="azul y blanco",cantidad_jugadores=17)
	tiemp=equipo(altura=1.56,nombre="pedro",año_de_fundacion=1945,color="verde y rojo",cantidad_jugadores=19)
	print(tiemp)	
	print(str(par))
	print(par.__cmp__(tiemp))
