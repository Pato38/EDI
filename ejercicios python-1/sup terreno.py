i = 1
area = 0
while (area > 1000):
	print ("ingrese el valor del frente del area")
	frente = int(input())
	print ("ingrese el valor del fondo del area")
	fondo = int(input())
	area = int(frente) * int(fondo)
	print ("superficie",i,":",area)
	i = i + 1