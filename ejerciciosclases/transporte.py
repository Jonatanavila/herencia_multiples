class transporte:
	def __init__(self, marca, tipo, color, años_antiguedad,**kw):
		self.marca=marca
		self.tipo=tipo
		self.color=color
		self.años_antiguedad=años_antiguedad
		print(marca,tipo,color,años_antiguedad)

	def __cmp__(self,otro):
			diferencia = (self.años_antiguedad) - (otro.años_antiguedad)
			if diferencia < 0:
					return -1
			elif diferencia > 0:
					return 1
			else:
					return 0

	def __eq__(self,igualdad):
			print('Los años de antiguedad son iguales?:',end='')
			if self.años_antiguedad==igualdad.años_antiguedad:
					return True
			else:
					return False

	def __repr__(self):
			return "%s %s" % (self.velocidad, self.ruedas)

class camion(transporte):
	def __init__(self,ruedas,velocidad,**kw):
		self.velocidad=velocidad
		self.ruedas=ruedas
		super().__init__(**kw)

class taxi(transporte):
	def __init__(self,numero_de_vehiculo,**kw):
		self.numero_de_vehiculo=numero_de_vehiculo
		super().__init__(**kw)

if __name__ == '__main__':
	trans=camion(velocidad=180,ruedas=4,marca="nissa",tipo="taxi",color="rojo",años_antiguedad=85)
	cam=camion(velocidad=250,ruedas=8,marca="susuki",tipo="camion",color="azul",años_antiguedad=65)
	print(cam)
	print(trans.__cmp__(cam))
	print(repr(trans))
	print(trans.__eq__(cam))
