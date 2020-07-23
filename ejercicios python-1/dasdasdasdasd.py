clientes=[2,3,4,7,5]

def maximo(clientes,max,diml):
	i=0
	max=input("ingrese el máximo:  ")
	for i in range (diml):
		if i==max:
			print(i)
	return i

i=maximo(clientes,max,5)
print("la posición que ocupa el nro es:  ",(i))

def borrar(clientes,x,diml):
	x=input("ingrese elemento a eliminar:  ")
	clientes.remove(clientes[i])
	return diml-1

diml=borrar(clientes, 7,5)
print("la cant de posiciones que quedan ocupadas son:   ",(diml))

def alocar(clientes,x,diml,y):
	x=input("ingrese la posición en la desea ingresar elemento:  ")
	y=input("ingrese valor:  ")
	j=input()
	for i in range (diml):
		clientes[+1]=clientes[j]
		clientes[i]=y
		clientes.insert(clientes[i])
	return diml+1

diml=alocar(clientes,4,5,8)
print(clientes)

