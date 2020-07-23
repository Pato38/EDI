print("ingrese la cantidad de numeros")
cant=int(input())
multiplicacion=1
i=0
for i in range(cant):
	print("ingrese el valor del numero ",i,"\n")
	num=int(input())
	multiplicacion=multiplicacion*num
print("la multiplicacion de los numeros es:",multiplicacion)