#Localiza el error en el siguiente bloque de código. Crea una excepción para
#evitar que el programa se bloquee y además explica en un mensaje al usuario
#la causa y/o solución

try:
	resultado = 10/0
except ZeroDivisionError:
	print("Error:\tNo es posible realizar la operación con divisor 0,\n"
		"\tdebe introducir un número distinto")



#Localiza el error en el siguiente bloque de código. Crea una excepción para
#evitar que el programa se bloquee y además explica en un mensaje al usuario
#la causa y/o solución
lista = [1, 2, 3, 4, 5]
try:
	lista[10]
except IndexError:
	print("Error:\tEl índice no pertenece a los códigos de libro,\n"
		"\tdebes utilizar los códigos reconocidos\n"
		"\ty una cantidad menor que la longitud de la lista")



#Localiza el error en el siguiente bloque de código. Crea una excepción para
#evitar que el programa se bloquee y además explica en un mensaje al usuario
#la causa y/o solución

colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }

try:
	colores['blanco'] 
except KeyError:
	print("Error:\tLa clave no se encuentra ,\n"
		"\tpuedes probar con otra que si exista")


#Localiza el error en el siguiente bloque de código. Crea una excepción para
#evitar que el programa se bloquee y además explica en un mensaje al usuario
#la causa y/o solución
try:
	resultado = 15 + "20"
except TypeError:
	print("Error:\tSolo es posible sumar datos del mismo tipo\n"
		"\tdebes convertir el número en cadena o viceversa")

#Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y
#un elemento. La función debe añadir el elemento al final de la lista con la
#condición de no repetir ningún elemento. Además si este elemento ya se
#encuentra en la lista se debe invocar un error de tipo ValueError que debes
#capturar y mostrar este mensaje en su lugar

lista_a = [22,23,-2]

def agregar_una_vez(lista_a,el):
	try:
		if el in lista_a:
			raise ValueError
		else:
			lista_a.append(el)
	except ValueError:
		print("Error: Imposible añadir elementos duplicados :   ",lista_a)

agregar_una_vez(lista_a,10)
agregar_una_vez(lista_a,-2)
agregar_una_vez(lista_a, "Hola")

print(lista_a)




