class Cadena:
	def revertir(self, frase):
		palabras = frase.split(' ')
		palabras = palabras[::-1]
		fraseinvertida = ''
		for recorrer in palabras:
			fraseinvertida = fraseinvertida + recorrer + ' '
		print(fraseinvertida)

if __name__ == '__main__':
	fraseinvertida = Cadena()
	fraseinvertida.revertir("Monoku We Go Beyond")