#definir carga de clientes 
clientes=[]

def carga():
	clientes=[]
	cant_cliente=0
	mes=0
	gast0_total=0
	cliente=input()
	while (cant_cliente<2):
		cliente_ant=cliente
		
		while (cant_cliente<=2) and (cliente_ant==cliente):
			code=int(input("ingrese código de cliente:   "))
			gasto=float(input("ingrese gasto mensual:   "))
			gast0_total=gast0_total+gasto
			cant_cliente=cant_cliente+1
			mes=mes+1
			cliente=cliente_ant

			print(cliente_ant,gast0_total,cant_cliente,mes)
			clientes.append(cliente_ant)

		return clientes

clientes=carga()
print(clientes)

#informa gasto tota y gasto promedio
def leer_cliente():
	cliente={'code':input("ingrese codigo: "),'gasto':float(input("ingrese gasto: "))}
	return cliente

cliente=leer_cliente()
clientes=[None]*2

def carga(cliente,dimf):
	i=0
	while (i<dimf):
		cliente=leer_cliente()
		clientes.append(cliente)
		i=i+1
	return clientes

clientes=carga(cliente,2)
print(clientes)


def gasto_total(clientes,diml):
	gasto_total_cliente=0
	i=0
	for i in range(diml):
		gasto_total_cliente=gasto_total_cliente+cliente['gasto']
		prom=gasto_total_cliente//12
		print(gasto_total_cliente,prom)
		return prom


prom=gasto_total(clientes,2) 
print(prom)

def maximo(clientes,max,diml):
	i=0
	for i in range (diml):
		if i==max:
			print(i)
	return i

i=maximo(clientes,max,2)
print(i)


#busqueda, borrado y alocación

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

def alocar(clientes,x,diml):
	x=input("ingrese la posición en la desea ingresar elemento:  ")
	for i in range (diml):
		clientes[+1]=clientes[j]
		clientes[i]=x
	return diml+1

diml=alocar(clientes,4,5)
print("la nueva cantidad de clientes es:     ",(diml))
