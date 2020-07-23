#Suma
def suma(n):
	if n == 1:
		return 1
	else: 
		return n+suma(n-1)

#Factorial		
def fac(n):
	if n==1:
		return (1)
	else:
		return n*fac(n-1)

#Busqueda Recursiva
def busqueda_recursiva(x,i,arreglo):
	if x==arreglo[i]:
		return(i)
	else:
		return (busqueda_recursiva(x,i+1,arreglo))

#
def reverse_word(palabra):
	if len (palabra)==1:
		return (palabra)
	else:
		return (palabra[-1]+reverse_word(palabra[0:-1]))

#suma de digitos
def suma_digitos (n):
	if n//10==0:
		return(n)
	else:
		return (n%10) + suma_digitos (n//10)
		
#suma de valores de matriz
def suma_arreglo(a,i):
	if (len(a)==i):
		return(a[i])
	else:
		return (a[i] + suma_arreglo[a,i+1])

def suma_matriz(m,c,f,dim_c,dim_f):
	if f==dim_f:
		return suma_matriz(m,[f],0)
	else:
		return suma_matriz(m,[f],0) + suma_matriz(m,c,f+1,dim_c,dim_f)
		
#busqueda dicotomica recursiva
def bdr(x,a,pri,ult):
	medio=(pri+ult)/2
	if a[medio]==x:
		return(medio)
	else:
		if a[medio]<x:
			return bdr(x,a,pri,medio-1)
		else:
			return bdr(x,a,medio+1,ult)
