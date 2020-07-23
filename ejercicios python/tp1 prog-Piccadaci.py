# Realiza una función llamada area_rectangulo(base, altura) que devuelva el área del rectángulo a partir de una base y una altura.
# Calcula el área de un rectángulo de 15 de base y 10 de altura:

def area_rectangulo(base,altura):
	return base*altura

area_rect= area_rectangulo(15,10)
print("el área del rectángulo es:    ",area_rect)


#Realiza una función llamada area_circulo(radio) que devuelva el área de un círculo a partir de un radio.
# Calcula el área de un círculo de 5 de radio: 
import math
def area_circulo(radio):
	return (radio**2)*math.pi

area_circ= area_circulo(5)
print("el área del círculo es:  ", area_circ)

#Realiza una función llamada relacion(a, b) que a partir de dos números cumpla lo siguiente: 
# Si el primer número es mayor que el segundo, debe devolver 1. 
# Si el primer número es menor que el segundo, debe devolver -1. 
# Si ambos números son iguales, debe devolver un 0. 
#Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'. 

def relacion(a,b):
	if a > b:
		return 1
	elif a < b:
		return -1
	else:
		return 0

r_a=(relacion(5,10))
r_b=(relacion(10,5))
r_c=(relacion(5,5))
print("la relación a es:   ",(r_a),(r_b),(r_c))

#Realiza una función llamada intermedio(a, b) que a partir de dos números, devuelva su punto intermedio. 
#Cuando lo tengas comprueba el punto intermedio entre -12 y 24: 
def intermedio(a,b):
	return (a+b)/2

prom=intermedio(-12,24)
print("el número intermedio es:    ",prom)

#Realiza una función llamada recortar(numero, minimo, maximo) que reciba tres parámetros. El primero es el número a recortar,
# el segundo es el límite inferior y el tercero el límite superior. La función tendrá que cumplir lo siguiente: 
# Devolver el límite inferior si el número es menor que éste  
#Devolver el límite superior si el número es mayor que éste.
#  Devolver el número sin cambios si no se supera ningún límite. 
#Comprueba el resultado de recortar 15 entre los límites 0 y 10. 

def recortar(num,min,max):
	if num<min:
		return min
	elif num>max:
		return max
	else:
		return num

rec=recortar(15,0,10)
print ("el resultado de recortar 15 entre 0 y 10 es:    ",rec)

#Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas. 
#La primera con los números pares y la segunda con los números impares. 


def separar(lista):
	lista.sort()
	pares=[]
	impares=[]
	for i in lista:
		if (i % 2==0):
			pares.append(i)
		else:
			impares.append(i)
	return pares,impares


num=[3,6,2,9,4,7]
pares,impares=separar(num)
print(pares)
print(impares)


