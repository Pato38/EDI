#a)Esta Funcion lee un cliente desde teclado, y devuelve un cliente
def leer_cliente():
	cliente={
		'cta':int(input("ingrese nro de cuenta:  ")),
		'sucursal':input("ingrese sucursal:   "),
		'apellido_nombre':input("ingrese apellido y nombre:   "),
		'fecha_ap_cta':int(input("ingrese fecha de apertura de la cuenta:   ")),
		'saldo': float(input("ingrese el saldo:  "))}
	return cliente

#Carga los clientes y devuelve un arreglo con los clientes cargados
def cargar_clientes():
	seguir = 's'
	i = 0
	while(seguir!='n' and i<10000):
		cliente = leer_cliente()
		clientes.append(cliente)
		seguir = input("¿Desea cargar un nuevo cliente? [s/n]  ")
		i = i + 1
	
	return clientes



cliente = {}
clientes = []
clientes = cargar_clientes()
print(clientes)



#Devuelve nombre de clientes q tengan saldo superior al promedio
def clientes_vip(clientes):	
	suma_saldo = 0
	i = 0
	for i in range(len(clientes)):
		suma_saldo = suma_saldo + clientes[i]['saldo']
	prom = suma_saldo/(len(clientes))    #Sacamos el promedio  entre el saldo total y el total de clientes
	print("El saldo promedio es:  " ,prom)

	# reccorremos la lista y buscamos que clientes superan el promedio y almacenamos en una nueva lista que retornara al final de la funcion
	i = 0
	clientes_vip = []
	for i in range(len(clientes)):
		if clientes[i]['saldo'] > prom:
			clientes_vip.append(clientes[i]['apellido_nombre'])
	return clientes_vip





clientes_vip = clientes_vip(clientes)
print("Los clientes cuyo saldo supera el promedio son:   ",clientes_vip)



#b)Esta Funcion lee un cliente desde teclado, y devuelve un cliente pero no pide el numero de cuenta.
# El programa lo determina segun el cliente anterior.
def leer_cliente():

	return cliente


def add_nuevo_cliente(clientes):
	seguir = 's'
	i = len(clientes)
	while(seguir!='n' and i<10000):
		cliente={
		'cta':(clientes[len(clientes)-1]['cta']+1),
		'sucursal':input("ingresará una cuenta consecutiva a la última ingresada;ingrese sucursal:   "),
		'apellido_nombre':input("ingrese apellido y nombre:   "),
		'fecha_ap_cta':int(input("ingrese fecha de apertura de la cuenta:   ")),
		'saldo': float(input("ingrese el saldo:  "))}
		clientes.append(cliente)
		seguir = input("¿Desea ingresar un nuevo cliente? [s/n]  ")
		i = i + 1
	return clientes

add_nuevo_cliente(clientes)
print(clientes)


#c)informa el nombre del cliente nro de cuenta 4500
def inform_cliente():
	i = 0
	busqueda = []
	num=int(input("ingrese el número de cta que desea buscar:  "))
	for i in range(len(clientes)):
		if clientes[i]['cta'] == num:
			busqueda=(clientes[i]['apellido_nombre'])
	return busqueda

busqueda=inform_cliente()

print("el cliente que busca es:   ", busqueda)

#d)informa nombre y apellido de los clientes de la sucursal Gonnet

def sucursal():
	i = 0
	sucursal.gonnet = []
	
	for i in range(len(clientes)):
		if clientes[i]['sucursal'] == 'gonnet':
			sucursal.gonnet.append(clientes[i]['apellido_nombre'])
	return sucursal.gonnet

sucursal.gonnet=sucursal()

print("los clientes de la sucursal Gonnet son:   ", sucursal.gonnet)


#e)define un nuevo cliente en un número de cta nuevo
def leer_cliente():

	return cliente

def add_nuevo_cliente1(clientes):
	seguir = 's'
	i = len(clientes)
	while(seguir!='n' and i<10000):
		cliente={
		'cta':(input("ingrese número de cta, si desea agregar un nuevo cliente:  ")),
		'sucursal':input("ingrese sucursal:   "),
		'apellido_nombre':input("ingrese apellido y nombre:   "),
		'fecha_ap_cta':int(input("ingrese fecha de apertura de la cuenta:   ")),
		'saldo': float(input("ingrese el saldo:  "))}
		clientes.append(cliente)
		seguir = input("¿Desea ingresar un nuevo cliente? [s/n]  ")
		i = i + 1
	return clientes



clientes = add_nuevo_cliente1(clientes)
print(clientes)








#f)Esta funcion remueve la cuenta especificada

def remover_cliente_cuenta(clientes):
	cuenta_remov = int(input("Ingrese el numero de cuenta a remover: "))
	seguir = True
	i = 0
	while(seguir!= False):
		if(clientes[i]['cta'] == cuenta_remov):
			clientes.remove(clientes[i])
			seguir = False
		else:
			i = i + 1
	return clientes


remover_cliente_cuenta(clientes)
print(clientes)





#Esta funcion remueve la cuenta especificada pero por nombre

def remover_cliente_cuenta(clientes):
	cuenta_remov = input("Ingrese el apellido y nombre del usuario que desea remover: ")
	seguir = True
	i = 0
	while(seguir!= False):
		if(clientes[i]['apellido_nombre'] == cuenta_remov):
			clientes.remove(clientes[i])
			seguir = False
		else:
			i = i + 1
	return clientes


remover_cliente_cuenta(clientes)
print(clientes)
