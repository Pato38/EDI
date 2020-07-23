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



