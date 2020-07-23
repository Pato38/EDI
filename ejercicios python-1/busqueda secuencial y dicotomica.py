
m_2=[[1,2,3],
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

#busqueda dicotómica de un número medio en una matriz

def busqueda_dicotomica(m_2,num):
	num=0
	
	primero=0
	ultimo=len(m)-1
	medio=(primero+ultimo)//2
	while medio!=num and primero < ultimo:
		if i > num: #aca el puso m_2[i]
			ultimo=medio - 1
		else:
			primero=medio + 1
			medio=(primero + ultimo)//2
			if(primero < ultimo):
				return posicion

m_2=[[1,2,3],
	[4,5]]
m=m_2
posicion=busqueda_dicotomica(m,3)#esto no lo puso, no se si va la posicion de  prim y seg o el valor
print(posicion)