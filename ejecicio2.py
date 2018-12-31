import math

class ConvertirEntero:
	def __init__(self):
		self.romano=['I','V','X','L','C','D','M']
		self.entero=[1,5,10,50,100,500,1000]
	def convertidor(self, numeroromano):
		dato = numeroromano.upper()
		dato=list(dato)
		conversion=[]
		for i in range(0, len(dato)):  
			for n in range(0,len(self.romano)): 
				if self.romano[n]==dato[i]:  
					conversion.append(self.entero[n]) 
		for i in range(0,len(conversion)):
			for j in range(1,len(conversion)):
				if j-i==1:
					if conversion[j]>conversion[i]: 
						conversion[i]=conversion[i]*-1 
		suma=0  
		for i in conversion:
			suma=suma+i
		print(suma)

if __name__ == '__main__':
	romanos = ConvertirEntero()
	romanos.convertidor('X')