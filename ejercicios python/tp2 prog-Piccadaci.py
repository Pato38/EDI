#1-Escriba un programa que pida un número de dados y muestre los valores de ese número de dados, al azar. 
import random
def juego():
	num=int(input("ingrese el número de dados:   "))
	if num<1:
		print("no puede jugar el juego")
	else:
		for i in range (num):
			print(f"dado {i+1}:   ",random.randrange(1,7))
	return num
	
num=juego()	

#2-Escriba un programa que pida un número de jugadores y tire un dado para cada jugador.


def juego_2():
	jugador=int(input("ingrese el número de jugadores:   "))
	if jugador<=1:
		print("no puede jugar el juego")
	else:
		for i in range (jugador):
			print(f"jugador {i+1} :   ",random.randrange(1,7))
	return 
	
jugador=juego_2()
	


#3-Escriba un programa que pida un número de jugadores, 
#que pida un valor a conseguir, que tire un dado para cada jugador y
# diga si han conseguido obtener el valor. 

def juego_3():
	jugador=int (input("ingrese el número de jugadores:  "))
	if jugador < 1:
		print("no puede jugar el juego")
	else:
		objetivo=int(input("ingrese el valor a conseguir:  "))
		if objetivo < 1 or objetivo > 6:
			print(f"el {objetivo} está fuera de rango")
		else:
			for i in range (jugador):
				dado=random.randrange(1,7)
		
				if dado==objetivo: 
					print(f"jugador{i+1}:{dado} objetivo conseguido")
				else:
					print(f"jugador{i+1}:{dado}")


juego_objetivo=juego_3()
print(juego_objetivo)					

# 4-Escriba un programa que pida un número de dados, que pida un valor a conseguir y
# que tire después el número de dados indicado. El jugador gana si saca el valor ganador. 
#OBTENER 

def juego_4():
	num=int(input("ingrese el número de dados:   "))
	if num<1:
		print("no puede jugar el juego")
	else:
		objetivo=int(input("ingrese el valor a conseguir:  "))
		if objetivo < 1 or objetivo > 6:
			print(f"el {objetivo} está fuera de rango")
		else:
			gana=False
			for i in range (num):
				valor=random.randrange(1,7)
				print(f"dado {i+1}:   ",valor)
				
				if valor==objetivo: 
					gana=True
					print(f" dado {i+1} usted es el ganador")
				else:
					print("no se ha logrado el objetivo")
			
juego_ganador=juego_4()
print(juego_ganador)

#5. Escriba un programa que pida un número de dados, que tire el número de dados indicado 
#y diga cuál es el valor más alto obtenido. 

def juego_5():
	num=int(input("ingrese el número de dados:   "))
	if num<1:
		print("no puede jugar el juego")
	else:
		mayor=1
		for i in range (num):
			valor=random.randrange(1,7)
			print(f"dado {i+1}:   ",valor)
			
			if valor > mayor:
				mayor=valor
				i=i+1
		print(f" el valor más alto obtenido es : {mayor}")

dado_mayor=juego_5()  


#6. Escriba un programa que pida un número de dados y tire esa cantidad para dos jugadores. 
#El jugador que saque el valor más alto, gana



def juego_6():
	num=int(input("ingrese el número de dados:   "))
	if num<1:
		print("no puede jugar el juego")
	else:
		mayor_1=0
		print(f"jugador 1:  ")
		for i in range (num):
			
			valor=random.randrange(1,7)
			print(f"dado {i+1}:   ",valor)
			
			if valor > mayor_1:
				mayor_1= valor
				i=i+1
		print()
		mayor_2=0
		print(f"jugador 2:  ")
		for i in range (num):

			valor=random.randrange(1,7)
			print(f"dado {i+1}:   ",valor)
			if valor > mayor_2:
				mayor_2=valor
				i=i+1
		print()
		if mayor_1 > mayor_2:
			print("ha ganado el jugador nro 1")
		elif mayor_2> mayor_1:
			print(" ha ganado el jugador nro 2")
		else:
			print("han empatado")

jugador_valor_alto=juego_6() 

#7. Escriba un programa que pida un número de dados y tire esa cantidad de dados.
# El primer jugador obtiene un punto por cada dado par. El segundo jugador obtiene un punto por cada dado impar. 
#El jugador que saque más puntos, gana	

def juego_7():
	num=int(input("ingrese el número de dados:   "))
	if num<1:
		print("no puede jugar el juego")
	else:
		pares=0
		impares=0
		for i in range (num):
			dado=random.randrange(1,7)
			print(f"dado {i+1}:   ",random.randrange(1,7))
			if dado % 2 == 0:
				pares= pares + 1
			else:
				impares= impares + 1
		print()
		if pares > impares:
			print("ha ganado el jugador par")
		elif impares > pares:
			print("ha ganado el jugador impar")
		else:
			print("han empatado")

par_impar=juego_7()

#8. Escriba un programa que pida un número de jugadores y tire un dado para cada jugador.
# El último jugador que saque el valor más bajo, gana. 


def juego_8():

	cant_jugador=int(input("ingrese el número de jugadores:   "))
	if cant_jugador<=1:
			print("no puede jugar el juego")
	else: 
		for i in range (cant_jugador):
			valor=random.randrange(1,7)
			print(f"jugador {i+1} :   ",valor)
			if i ==0:
				menor=valor
				j=1
			else:
				if menor > valor:
					menor=valor
					j=i+1

		print("el jugador que tiene el valor menor es:    ",j)
	
	
menor_valor=juego_8()

#9. Escriba un programa que pida un número de dados y tire esa cantidad de dados para dos jugadores. 
#El jugador que saque más puntos sumando su valor más alto y su valor más bajo, gana

def juego_9():  
	
	num=int(input("ingrese el número de dados:   "))
	if num<1:
		print("no puede jugar el juego")
	else:
		jugador_1=suma(num)
		jugador_2=suma(num)
		if jugador_1 > jugador_2:
			print("ha ganado el jugador 1")
		elif jugador_2 > jugador_1:
			print("ha ganado el jugador 2")
		else:
			print("han empatado")










def suma(num):

	
	i=0	
	for i in range (num):
		valor=random.randrange(1,7)
		print(f"dado {i+1}:   ",valor)

		if i==0:
			menor=valor
		if i==1:
			if menor> valor:
				mayor=menor
				menor=valor
			else:
				mayor=valor
		if i>=2:

			if valor > mayor:
				mayor=valor
			else:
				if valor < menor:
					menor=valor
		
	
	print(f" el valor mayor obtenido es : {mayor}")
	print(f" el valor menor obtenido es :  {menor}")

	suma= mayor+ menor
	print(suma)

	return suma

#10. Escriba un programa que pida un número de dados y tire esa cantidad de dados. Si no salen dos dados iguales seguidos, el jugador gana.
# Si salen, pierde
def juego_10():
	num=int(input("ingrese el número de dados:   "))
	if num<=1:
		print("no puede jugar el juego")
	else:
		i=0
		actual=random.randrange(1,7)
		print(f"dado {i+1}:   ",actual)
		i=1
		repetido=False
		for i in range (num):
			anterior=actual
			actual=random.randrange(1,7)
			print(f"dado {i+1}:   ",actual)
			if actual == anterior:
				repetido=True

		if repetido ==True:
			print("usted ha perdido")
		else:
			print("usted ha ganado")		

			
	
juego_10()
