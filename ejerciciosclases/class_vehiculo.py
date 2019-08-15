class Vehiculo():
	def __init__(self, color, ruedas,**kw):
		self.color = color
		self.ruedas = ruedas

	def posicision(self):
		self.posicion= 0

	def __str__(self):
		return "Color: {},ruedas: {} ".format( self.color, self.ruedas )

	def __repr__(self):
		return "%s %s" % (self.color, self.ruedas)

class Coche(Vehiculo):
	def __init__(self,velocidad, cilindrada,**kw):
		self.velocidad = velocidad
		self.cilindrada = cilindrada
		super().__init__(**kw)

	def andar(self):
		self.posicion += 20


vehi= Vehiculo(velocidad=300,cilindra=1200,color="azul",ruedas=4)
print(vehi)
print(str(vehi))
print(repr(vehi))
