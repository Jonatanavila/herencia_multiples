class aves:
	def __init__(self,nombre,edad,color,**kw):
		self.nombre=nombre
		self.edad=edad
		self.color=color
		print(nombre,edad,color)

	def posicion(self):
		self.posicion=0

	def __str__(self):
		return "nombre: {},color: {}".format(self.nombre,self.color)

	def __cmp__(self,otro):
			diferencia = (self.edad) - (otro.edad)
			if diferencia < 0:
					return -1
			elif diferencia > 0:
					return 1
			else:
					return 0

class pinguino(aves):
	def __init__(self,tipo_comida,**kw):
		self.tipo_comida=tipo_comida
		super().__init__(**kw)
		print(tipo_comida)

	def caminar(self):
		self.pocision +=10

	def dar_comida(self):
		if self.posicion %20==0:
			print ("dar de comer")
		else:
			print("no dar de comer")

class cuervo(aves):
	def __init__(self,**kw):
		super().__init__(**kw)

	def volar(self):
		if self.posicion %30==0:
			print("esta volando")
		else:
			print("no vuela")
	


if __name__ == '__main__':
	ave=cuervo(tipo_comida="carne",nombre="cuervo",color="negro",edad=3)
	avee=cuervo(nombre="pingui",edad=10,color="blanco",tipo_comida="pescado")
	print(avee)	
	print(str(ave))
	print(ave.__cmp__(avee))	
