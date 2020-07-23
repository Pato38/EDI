from io import open
import pickle
#inicializamos la clase personajes con sus atributos
class Personaje:
	def __init__(self, nombre={},vida=0, ataque=0, defensa=0, alcance=0):
		self.nombre = nombre
		self.vida = vida
		self.ataque = ataque
		self.defensa= defensa
		self.alcance = alcance

#esta función imprime 
	def __str__(self):
		return "{} -> {} vida, {} ataque, {} defensa, {} alcance".format(
			self.nombre, self.vida, self.ataque, self.defensa, self.alcance)


#inicializamos clase gestor
class Gestor:

	personajes = []
	def __init__(self):
		self.cargar()
#el bucle for recorre los personajes temporales dentro de la clase personajes y si coincide con el nombre del personaje lo agrega y guarda
	def agregar(self,p):
		for pTemp in self.personajes:
			if pTemp.nombre == p.nombre:
				return

		self.personajes.append(p)
		self.guardar()

#el bucle for recorre nuevamente los personajes y si el personaje temporal es igual a nombre lo remueve y guarda los cambios
	def borrar(self, nombre):
		for pTemp in self.personajes:
			if pTemp.nombre == nombre:
				self.personajes.remove(pTemp)
				self.guardar()
				print("\nPersonaje {} borrado".format(nombre))
				return

#muestra los personajes
	def mostrar(self):
		if len(self.personajes)==0:
			print("El gestor esta vacio")
			return
		for p in self.personajes:
			print(p)

#pckl almacena cualq objeto en un archivo o  cadena

	def cargar(self):
		fichero= open("personajes.pckl", "ab+") #abrimos el fichero en serie (pickl)
		fichero.seek(0)#inicializa en 0
		try:
			self.personajes = pickle.load(fichero)	#lo carga
		except:
			print("El fichero está vacío")
			pass
		finally:
			fichero.close()
			print ("Se han cargado {} personajes".format(
				len(self.personajes)))



	def  guardar(self):
		fichero = open("personajes.pckl","wb")
		pickle.dump(self.personajes,fichero) #con dump muestra lo q pedimos
		fichero.close

	

G=Gestor()
G.agregar(Personaje("Caballero",4,2,4,2))
G.agregar(Personaje("Guerrero",2,4,2,4))
G.agregar(Personaje("Arquero",2,4,1,8))
G.mostrar()
G.borrar("Arquero")
G.mostrar()