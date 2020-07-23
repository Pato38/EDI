print("ingrese carrera isfdyt 210")
carrera_1=input()
print("ingrese código de la carrera")
code_carrera_1=int(input())
print("ingrese duración de la carrera")
durac_carrera1=int(input())
print("ingrese cantidad de alumnos primer año")
cant_alum_1ro=int(input())
print("ingrese cantidad de alumnos segundo año")
cant_alum_2do=int(input())
print("ingrese cantidad de alumnos tercer año")
cant_alum_3er=int(input())
suma_cant_alum_carrera_1=0
suma_cant_alum_carrera_1=cant_alum_1ro+cant_alum_2do+cant_alum_3er
prom_carrera_1=suma_cant_alum_carrera_1//3
print("el promedio de alumnos es: ",prom_carrera_1)




print("ingrese el codigo de la carrera")
code=int(input())
code_impares=1
while(code>1):
	digito=code%10
	code=code//10
	if(digito%2==1):
		code_impares=digito
		print("el código tiene numeros impares")