#suma
n=10
def suma(n):
	if n ==0:
		return 0
	else:
		return n+suma(n-1)

suma(10)
print(suma(10))

#maximo recursivo
diml=4
max=0
i=0
arreglo=[]
def encontrar_maximo_recursivo(arreglo,i,diml,max):
	
	if i == (diml):
		return max
	else:
		 if arreglo[i]> max:
		 	return encontrar_maximo_recursivo(arreglo,i+1,diml,arreglo[i])
		 else:
		 	return encontrar_maximo_recursivo(arreglo,i+1,diml,max)
arreglo=[1,2,8,3]
encontrar_maximo_recursivo(arreglo,i,4,max)
print(encontrar_maximo_recursivo(arreglo,i,4,max))