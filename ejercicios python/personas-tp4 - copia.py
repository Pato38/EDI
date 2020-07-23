from io import open
#abre, lee y cierra el fichero
fichero=open('personas.txt','r',encoding="utf8")
lineas=fichero.readlines()
fichero.close()
#arma una lista y lo agrega
personas=[]

for linea in lineas:
	campos=linea.replace("\n","").split(";")#las comillas q cierran indica q se termino la fila y va hacia abajo y el ; divide
	persona={"id":campos[0], "nombre":campos[1],
			"apellido":campos[2],"nacimiento":campos[3]}
	personas.append(persona)


for p in personas:
	print("(id-{}) {} {} : {}".format(p['id'], p['nombre'],
										p['apellido'],p['nacimiento']))