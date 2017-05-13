

class MaxNum:
	def max_de_tres(n1,n2,n3):
		if n1 > n2 and n1 > n3:
			print('El numero ', n1, 'es el maximo')
		elif n2 > n3 and n2 > n1:
			print('El numero ', n2, 'es el maximo')
		elif n3 > n1 and n3 > n2:
			print('El numero ', n3, 'es el maximo')

n1 = input("Dame el prime numero: ")
n2 = input("Dame el segundo numero: ")
n3 = input("Dame el tercer numero: ")

MaxNum.max_de_tres(n1,n2,n3)


class Phrase:
	def inversa(phrase):
		temp = phrase.replace(' ', '').lower()
		print(temp[::-1])

phrase = input('Dame la frase: ')
Phrase.inversa(phrase)

class Number:
	def generar_n_caracteres(num, character):
		res = num * character
		print(res)

num = int(input('Dame el numero'))
character = ('x')
Number.generar_n_caracteres(num,character)

def procedimiento (lista):
	for i in lista:
		print (int(i) * "x")

lista = [1,3,4,5,18,5,50]
procedimiento(lista)

def superpocion(lista1,lista2):
	for i in lista1:
		for x in lista2:
			if i == x:
				return True
	return False

lista1 = input('Dame la lista 1: ')
lista2 = input('Dame la lista 2: ')
print(superpocion(lista1,lista2))





