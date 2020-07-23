#carga cerveza por tipo

def leer_barril():

	barril={
		'producto':input("ingrese producto:  "),
		'litros':int(input("ingrese los litros por barril:  ")),
		'proveedor':input("ingrese proveedor:  "),
		'porc_amarg':int(input("ingrese porcentaje de amargura:  ")),
		'porc_alcohol':int(input("ingrese porcentaje de alcohol:  ")),
		'precio':int(input("ingrese precio:  ")),
		'porc_lleno':int(input("ingrese porcentaje de cerveza en el barril:  "))}
	return barril

barril=leer_barril()

#carga los tipos de cerveza en una lista
def cargar_barril():
	seguir='s'
	productos=[]
	i=0
	while seguir!='n':
		barril=leer_barril()
		productos.append(barril)
		seguir=input("desea cargar otra variedad: s/n    ")
		i=i+1
		
		return productos


productos=cargar_barril()
print(productos)



def vendidas(litros_consumidos):
	litro=int(input("Ingrese litros iniciales del barril  "))
	return litro - litros_consumidos

litros_consumidos=int(input("ingrese los litros consumidos   "))
litro_final=ventas(litros_consumidos)
print (litro_final)


def ganancia(precio_vta):
	precio=int(input("ingrese precio de compra de la cerveza:  "))
	return precio - precio_vta

precio_vta=int(input("ingrese el precio de la venta: "))
gan_final=ganancia(precio_vta)
print(gan_final)






	
	
