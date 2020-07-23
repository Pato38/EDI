
from io import open
import sys

fichero=open("contador.txt", "a+") #lo abre
fichero.seek(0) #establece la posición actual
contenido = fichero.readline() #lo lee

#lee el contenido y si es igual a 0 lo iguala a la variable y comienza a escribirlo
if len(contenido)==0:
	contenido = "0"
	fichero.write(contenido)

fichero.close() #cierra el fichero

#transforma el texto a número
try:
	contador=int(contenido)
#contamos el nro de argumentos con el sys.argv inc incrementa dec decrece
	if len (sys.argv)==2:
		if sys.argv[1]=="inc":
			contador+= 1
		elif sys.argv[1] == "dec":
			if contador > 0:
				contador-= 1
			else:
				contador=0

	print (contador)
	

	fichero = open("contador.txt","w")
	fichero.write (str(contador))		
	fichero.close()

except:
	print("Error. Fichero corrupto")