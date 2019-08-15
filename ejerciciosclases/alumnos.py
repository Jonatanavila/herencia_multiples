class Persona:
	def __init__(self, nombre, apellido, dni, edad,**kw):
		self.nombre=nombre
		self.apellido=apellido
		self.dni=dni
		self.edad=edad

	def __eq__(self,otro):
			print('La edad de los alumnos son iguales?:',end='')
			if self.edad==otro.edad:
					return True
			else:
					return False

	def __cmp__(self, otro):
			diferencia = (self.edad) - (otro.edad)
			if diferencia < 0:
					return -1
			elif diferencia > 0:
					return 1
			else:
					return 0
		
class Alumno(Persona):
	def __init__(self,año_de_egreso,**kw):
		self.año_de_egreso=año_de_egreso
		super().__init__(**kw)

	def cursada(self):
		if self.año_de_egreso == 2010 :
			print('este alumno ya egreso')
		elif self.año_de_egreso < 2010:
				print('este alumno todabia no egreso')

	def __str__(self):
		return "Nombre: {},apellido: {}, dni: {},año_de_egreso: {},".format(
		self.nombre, self.apellido, self.dni,self.año_de_egreso,)

if __name__ == '__main__':
	per=Alumno (año_de_egreso=2010,dni=34824346,edad=27,nombre="juan",apellido="antoni")
	estd=Alumno (año_de_egreso=2010,dni=34572343,edad=27,nombre="pedro",apellido="garcia")
	print(str(estd))
	print(per.__eq__(estd))
	print(estd.__cmp__(per))
