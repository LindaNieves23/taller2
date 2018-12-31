import math

class ConvertirRomanos:
	def __init__(self):
		self.Unidad = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
		self.Decena = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
		self.Centena = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
	def convertidor(self, numero):
		u= numero % 10
		d=int(math.floor(numero/10))%10
		c=int(math.floor(numero/100))
		if(numero>=100): 
			print(self.Centena[c]+self.Decena[d]+self.Unidad[u])
		else:
			if(numero>=10):
				print(self.Decena[d]+self.Unidad[u])
			else:
				print(self.Unidad[numero])

if __name__ == '__main__':
	romano = ConvertirRomanos()
	romano.convertidor(10)