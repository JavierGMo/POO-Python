class Vehiculo:
	def __init__(self, color, ruedas):
		self.color = color
		self.ruedas = ruedas

class Coche(Vehiculo):
	def __init__(self, color, ruedas):
		self.color = color
		self.ruedas = ruedas


class Bicicleta(Vehiculo):
	def __init__(self, color, ruedas):
		self.color = color
		self.ruedas = ruedas


class Camioneta(Coche):
	def __init__(self, color, ruedas):
		self.color = color
		self.ruedas = ruedas


class Motocicleta(Bicicleta):
	def __init__(self, color, ruedas):
		self.color = color
		self.ruedas = ruedas
