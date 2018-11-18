class plano:
	x1 = int()
	y1 = int()
	x2 = int()
	y2 = int()
	def __init__(self,x1=None,y1=None):
		self.x1 = x1
		self.y1 = y1
	def __str__(self):
		return f"P({self.x1}, {self.y1})"

	def cuadrante(self):
		if self.x1 > 0 and self.y1 > 0:
			print(f"\nCuadrante 1: " + self.__str__())
		elif self.x1 < 0 and self.y1 > 0:
			print("\nCuadrante 2: " + self.__str__())
		elif self.x1 < 0 and self.y1 < 0:
			print("\nCuadrante 3: " + self.__str__())
		elif self.x1 > 0 and self.y1 < 0:
			print("\nCuadrante 4: " + self.__str__())
		elif self.x1 == 0 and self.y1 == 0:
			print("\nOrigen: " + self.__str__())
	def vector(self,x2,y2):
		self.x2 = x2
		self.y2 = y2
		print(f"\nAB = ({self.x2-self.x1},{self.y2-self.y1})")

	def distancia(self):
		d = ((self.x2-self.x1)**2 + (self.y2-self.y1)**2 )**(1/2)
		return f"\nDistancia entre:" + self.__str__() + f"y P({self.x2}, {self.y2})" +f" Distancia = {d}"
