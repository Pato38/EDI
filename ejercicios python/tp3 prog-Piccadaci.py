#1. Implementaremos una clase llamada Persona que tendrá como atributo (variable) el nombre de la persona y dos métodos (funciones).
# El primero de los métodos inicializará el atributo nombre y el segundo mostrará por pantalla el contenido del mismo.
# Definir dos instancias (objetos) de la clase Persona.
class Persona():
	def __init__(self):
		self.nombre=input("ingrese nombre del empleado:  ")
		

	def mostrar(self):
		print(" El Nombre de la persona es :  ",self.nombre)
		

	def setNombre(self,nombre):
		self.nombre=nom??

	def getNombre(self):
		return self.nombre




#2. Declarar una segunda clase llama Empleado que hereda de la clase Persona y agrega el atributo sueldo.
# Debe mostrar si tiene que pagar impuestos o no (sueldo superior a 3000). Crear un objeto de cada clase. 

class Empleado(Persona):
	def __init__ (self):
		super().__init__()
		self.sueldo=float(input("ingrese sueldo:   "))


	def mostrar(self):
		super().mostrar()
		print("Sueldo:    ",self.sueldo)

	def paga_imp(self):
		if self.sueldo > 3000:
			print(" Debe pagar impuesto")
		else:
			print("No paga impuesto")


Persona1= Persona()
Persona1.mostrar()
Empleado1=Empleado()
Empleado1.mostrar()
Empleado1.paga_imp()




	


#3. Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno.
# Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota
# y si ha aprobado o no.´

class Alumno():
	
	def __init__(self):
		print("alumno-nota")
		self.nom = input("ingrese nombre del alumno:  ")
		self.nota = int(input("ingrese nota obtenida:  "))

	def setNota(self,nota):
		self.nota = nota

	def getNota(self):
		return self.nota

	def mostrar(self):
		print(" Nombre:   ",self.nom,"Nota:  ",self.nota)

	def aprobados(self):
		if self.nota >= 7:
			print( self.nom, "ha aprobado ")
		else:
			print( self.nom, "ha desaprobado")
		


alumno1=Alumno()
alumno1.mostrar()
alumno1.aprobados()

#4. Realizar un programa que tenga una clase Persona con las siguientes características. 
#Implementar los métodos necesarios para inicializar los atributos, mostrar los datos e 
#indicar si la persona es mayor de edad o no. 


class Persona():
	def __init__(self):
		print("mayores de edad")
		self.nom=input("ingrese nombre de la persona:  ")
		self.edad=int(input("ingrese edad:   "))

		
	def mostrar(self):
		print("                      ")
		print("Nombre: ",self.nom)
		print ( "edad: ",self.edad)

	def setNombre(self,nom):
		self.nom

	def getNombre(self):
		return self.nom

	def __str__(self):
		print(self.nom)

	def mayoredad(self):	
		if self.edad >= 18:
			print(" la persona es mayor de edad")
		else:
			
			print("la persona es menor de edad")

persona1=Persona()
persona1.mostrar()
persona1.mayoredad()




	
#5. Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre,
# el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones 
# Añadir contacto.  Lista de contactos  Buscar contacto  Editar contacto  Cerrar agenda 

class Agenda():

	def __init__(self):
		
		self.contactos=[]
		
		


		
	def menu(self):
		print()
		menu=[["1.agenda"],
		["2.añadir contacto"],
		["3.lista de contactos"],
		["4.buscar contactos"],
		["5.editar contacto"],
		["6.cerrar agenda"]]

		for i in range (6):
			print("          ")
			print (menu[i][0])

		seleccion=input("Seleccione la opción deseada: ")
		if seleccion == 1:
			self.agenda()
		elif seleccion == 2:
			self.añadir()
		elif seleccion == 3:	
			self.lista()
		elif seleccion == 4:
			self.buscar()
		elif seleccion == 5:
			self.editar()
		elif seleccion == 6:
			print("usted está saliendo de la agenda") 

	
	def añadir(self):
		print("                               ")
		print("añadir nuevo contacto:    ")
		
		super().__init__()
		seguir = 's'
		while(seguir!='n'):
			datos_contacto={}
			datos_contacto={
			'nom':input("ingrese nombre de contacto:     "),
			'tel':int(input("ingrese el teléfono del contacto:     ")),
			'email':input("ingrese el mail del contacto:        ")}
			self.contactos.append(datos_contacto)
			seguir = input("¿Desea cargar un nuevo contacto? [s/n]  ")
		print(self.contactos)	
		return self.contactos

	

	def lista(self):
		print("                ")
		print("	Lista de contactos")
		
		if len(self.contactos) == 0:
			print("no hay contactos en la lista")
		else:
			for i in range (len(self.contactos)):
				print(self.contactos[i]['nom'])

		


	


	def busqueda(self):
		print("               ")
		print("buscar contactos")
	
		nom=input("introduzca el nombre de su contacto:   ")
		for i in range (len(self.contactos)):
			if nom == self.contactos[i]['nom']:
				print("Nombre:    ",self.contactos[i]['nom'])
				print("teléfono:   ",self.contactos[i]['tel'])
				print("mail:    ",self.contactos[i]['email'])
				return i
		



	def editar(self):
		print("               ")
		print("editar contacto")
		
		nom=input("introduzca el nombre de su contacto:   ")
		for i in range (len(self.contactos)):
			if nom == self.contactos[i]['nom']:
				finalizar=False
				while finalizar == False:
			
					print("1. nombre")
					print("2.teléfono")
					print("3.mail")
					print("4.exit")
					opcion=int(input("Seleccione el número  de la opción que desea modificar:  "))
					if opcion == 1:
						nom=input("introduzca el nuevo nombre:    ")
						self.contactos[i]['nom']=nom
					elif opcion == 2:
						tel=int(input("ingrese el nuevo número: "))
						self.contactos[i][tel]=tel
					elif opcion == 3:
						email=input("ingrese nuevo mail:  ")
						self.contactos[i][email]=mail
					elif opcion == 4:
						exit()
					finalizar=True	
					print(self.contactos)

					



agenda=Agenda()
agenda.menu()
agenda.añadir()
agenda.lista()
agenda.busqueda()
agenda.editar()

#6. En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero.
# El banco requiere también al final del día calcular la cantidad de dinero que se ha depositado.  deberán crear dos clases, 
#la clase cliente y la clase banco. La clase cliente tendrá los atributos nombre y cantidad y los métodos __init__, depositar, extraer, mostrar_total. 
#La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos __init__, operar y deposito_total.

class  cliente():
	
	def __init__(self,nom):
		self.nom=nom
		self.cant=0
		

	def depositar(self,cant):
		
		self.cant=self.cant + cant 


	def extraer(self,cant):
		
		self.cant=self.cant - cant 


	def mostrar_total(self):
		return self.cant

	def imprimir(self):
		print("                        ")
		print ("nombre del cliente:   ",self.nom, " total de la cuenta:    ",self.cant)




class banco():

	def __init__(self):
		
		self.depositos=0
		self.extracciones=0
		

		
	def operar(self,depositos,extracciones):
		self.depositos = self.depositos + depositos
		self.extracciones=self.extracciones + extracciones

		
		

	def deposito_total(self):
		total=0
		total=self.depositos + total
		print("                       ")
		print("el total de dinero depositado es:  ", total)


cliente1=cliente("Marcos")
cliente1.depositar(322)
cliente1.extraer(22)
cliente1.mostrar_total()
cliente1.imprimir()
banco=banco()
banco.operar(300,22)
banco.deposito_total()


#7. Desarrollar un programa que conste de una clase padre Cuenta y dos subclases PlazoFijo y CajaAhorro. 
#Definir los atributos titular y cantidad y un método para imprimir los datos en la clase Cuenta. 
#La clase CajaAhorro tendrá un método para heredar los datos y uno para mostrar la información. 
#La clase PlazoFijo tendrá dos atributos propios, plazo e interés. 
#Tendrá un método para obtener el importe del interés (cantidad*interés/100) y otro método para mostrar la información, 
#datos del titular plazo, interés y total de interés. 
#Crear al menos un objeto de cada subclase.




class cuenta():
	def __init__(self,nom,cant):
		self.nom=nom
		self.cant=cant
	

	def imprimir(self):
		print("                  ")
		print("nombre:   ",self.nom)
		print("cuenta en pesos:   ",self.cant)



class cajaAhorro(cuenta):
	def __init__(self,nom,cant):
		super().__init__(nom,cant)


	def mostrar(self):
		print("                    ")
		print("nombre:  ",self.nom)
		print ("cantidad en su cuenta Caja de Ahorro:   ",self.cant)




class PlazoFijo(cuenta):
	def __init__(self,nom,cant,plazo,interes):
		super().__init__(nom,cant)
		self.plazo=plazo
		self.interes=interes

	def importe_interes(self):
		
		self.total=self.cant*self.interes/100
		 

	def mostrar(self):
		print("                      ")
		print("titular:   ",  self.nom)
		print("porcentaje de interés:    ",  self.interes,)
		print("                         ")
		print("el interes total en los plazos fijos es de:      ",  self.total)



cuenta=cuenta("Maria",3200)
cuenta.imprimir()
caja_de_ahorro= cajaAhorro("Juan",4000)
caja_de_ahorro.mostrar()
PlazoFijo=PlazoFijo("Maria",3200,30,10)
PlazoFijo.importe_interes()
PlazoFijo.mostrar()

