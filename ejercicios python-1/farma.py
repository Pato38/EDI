#Carga medicamentos con su código y características

def leer_medicam():
	medicam = {}
	medicam={
		'codigo':int(input("ingrese código del medicamento:  ")),
		'medicam':input("ingrese nombre del medicamento:   "),
		'comp_ppal':input("ingrese componente principal:   "),
		'stock':int(input("ingrese stock del medicamento:   ")),
		'prec_unit': float(input("ingrese precio unitario:  "))}
	return medicam

#Carga los medicamento y devuelve un arreglo con los medicamentos cargados
def cargar_medicam():
	farma = []
	seguir = 's'
	i = 0
	while(seguir!='n' and i<1000):
		medicamento = leer_medicam()
		farma.append(medicamento)
		seguir = input("¿Desea cargar un nuevo medicamento? [s/n]  ")
		i = i + 1
	
	return farma


farma = cargar_medicam()
print(farma)

#Ingresa el código del medicamento, la cantidad que se vende e imprime el precio total. Finaliza al colocar -1 

def ventas(farma):
	
	precio_total=0
	i=0
	codigo=int(input("Ingrese el codigo del medicamento que desea vender: "))
	cantidad=int(input("Ingrese la cantidad de medicamentos :  "))
	for i in range(len(farma)):
		if (codigo == farma[i]['codigo']):
			precio_total = farma[i]['prec_unit'] * cantidad 
		else:
			i=i+1    
	print("El precio de total  es:   ",(precio_total))	
			
	return	precio_total

precio_total=ventas(farma)


#elimina los medicamentos con stock 0

def remove_stock_cero(farma):
	i=0
	n = len(farma)
	for i in range (n):
		if farma[i]['stock'] != 0:
			i = i + 1
		else:
			farma.remove(farma[i])
			return farma

		


remover = input("Desea remover los medicamentos con stock agotado?[s/n] ")
if remover == 's':
	remove_stock_cero(farma)
print(farma)

#modificar el precio unitario del medicamento código 30 en $10
def aumento(farma):
	i=0
	code=input("ingrese código del medicamento cuyo valor desea modificar:  ")
	aumento=int(input("ingrese el valor del aumento:  "))
	for farma[i]['codigo'] in range (len(farma)):
		if farma[i]['codigo']==code:
			farma[i]['prec_unit']=farma[i]['prec_unit']+aumento
			
			
	return 

valor=aumento(farma)
	
print(valor)











