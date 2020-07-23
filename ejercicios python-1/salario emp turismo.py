def carga(diml,sueldo):
	diml=0
	sueldo=float(input("ingrese sueldo    "))
	while(diml<300):
		diml=diml+1
		sueldo=diml
		return(sueldo)

def s_aum(salario,x):
	salario=float(input("ingrese salario   "))
	x=1,15
	return(salario*1,15)

def recorrer(vector,diml):
	for i in range(diml):
		vector[i]=f(vector[i])

def prom(diml,salario):
	diml=1
	salario=float(input("ingrese salario"))
	suma_salario=0
	while(salario in diml):
		diml=diml+1
		suma_salario=salario+diml
		prom=suma_salario*diml//100
		return(prom)
