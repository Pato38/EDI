#Se desea saber si la suma de todas las posiciones de la matriz m_1
#es igual a la suma de todas las posiciones de la matriz m_2
#se sabe q ambas son de 8x10 y contiene nros reales en el intervalo 0-100
#considerando dos digitos decimales. Imprimir un msje apropiado e informe la
#situación.Analizar y contestar: 
#a)que entrada se requiere?(tipo y cantidad)
#b)cuál es la salida deseada?(tipo y cantidad)
#c)que métodos produce la salida deseada?
m_1=[None]*4
m_2=[None]*4

def carga(dim_f,dim_c):
	
	m=[]
	for c in range (dim_c):
		m.append([])
		for f in range (dim_f):
			m[c].append(float(input("ingrese el numero para la posición ["+str(c)+"]["+str(f)+"]:  ")))

	return m


m_1=carga(2,2)
m_2=carga(2,2)

print(m_1)
print(m_2)


def suma(matriz,dim_c,dim_f):
	
	suma=0
	for c in range (dim_c):
		for f in range (dim_f):
			suma=matriz[c][f]+suma
	return suma

suma_m_1=suma(m_1,2,2)
suma_m_2=suma(m_2,2,2)


if suma_m_1==suma_m_2:
	print("la suma de las matrices es igual")
else: 
	print("la suma de las matriz es diferente")



