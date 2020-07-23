
m_2=[[1,2],
	[4,5]]
     
m_1=[[1,2],
	[3,4]]

#busqueda secuencial del numero mayor en una matriz
objetivo=0
maximo=4
i=0
def busqueda_secuencial(m_1,diml,i):
	while maximo!=objetivo and i<diml:
		i=i+1
		return maximo

maximo=busqueda_secuencial(m_1,2,i)
print(maximo)
