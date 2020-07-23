#carga de matrices
m_1=2*2
m_2=[None]*4
def carga(dim_c,dim_f):
	m=[]
	for c in range (dim_c):
		m.append([])
		for f in range (dim_f):
			m[c].append(int(input("ingrese valor para la posición ["+str(c)+"]["+str(f)+"]:  ")))
	return m

m_1=carga(2,2)
m_2=carga(2,2)
print (m_1)
print (m_2)

#se suman las columnas de m_1
def suma_de_columnas(m_1,dim_c):
	sumacolumna=0
	f=0
	for c in range(dim_c):
		sumacolumna=sumacolumna+m_1[c][f]
	return sumacolumna

sumacolumna=suma_de_columnas(m_1,2)
print(sumacolumna)
	
#se suman las filas de m_2

def suma_de_filas(m_2,dim_f):
	sumafila=0
	c=0
	for f in range(dim_f):
		sumafila=m_2[f][c]+sumafila
	return sumafila

sumafila=suma_de_filas(m_2,2)

print(sumafila)


#promedio de valores de ambas matrices


def promedio_valores(m,dim_c,dim_f):
	suma_m=0
	promedio_m=0
	for c in range (dim_c):
		for f in range (dim_f):
			suma_m=m[c][f]+suma_m
			promedio_m=suma_m//(dim_c+dim_f)
	return promedio_m

m=m_1
promedio_m=promedio_valores(m,2,2)
print("el promedio de la matriz es:    ",(promedio_m))

#multiplicación de matrices
def multiplicación(m_1,m_2,dim_c,dim_f):
	m_3=[0,0],[0,0]
	for c in range(dim_c):
		for f in range (dim_f):
			for z in range (2):
				m_3[c][z]+=m_1[c][z]*m_2[z][f]
	print (m_3)
	return multiplicación

multiplicación=multiplicación(m_1,m_2,2,2)

