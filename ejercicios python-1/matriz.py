#reservar espacio para matriz
matriz=[None]*4
dim_c=2
dim_f=2


def carga(dim_f,dim_c):
	
	matriz=[]
	for c in range (dim_c):
		matriz.append([])
		for f in range (dim_f):
			matriz[c].append(float(input("ingrese el numero para la posición ["+str(c)+"]["+str(f)+"]:  ")))

	return matriz


matriz=carga(2,2)


print(matriz)

#recorrer columnas pares e imprimir



def col_par(matriz,dim_c):
	
	for c in range (dim_c):
		
		if (c % 2 == 0):
			print(matriz[c])
	return col_par

col_par=col_par(matriz,2)


#recorrer fila impar e imprimir

def fil_impar(matriz,dim_f):
	
	for f in range (dim_f):
		
		if (f % 2 != 0):
			print(matriz[f])
			
	return fil_impar

fil_impar=fil_impar(matriz,2)


#recorrer diagonal e imprimir

def diag(matriz,dim_f,dim_c):
	
	for f in range (dim_f):
		for c in range (dim_c):
			if f==c:
				print(matriz[f][c])
		
		

diagonal=diag(matriz,dim_f,dim_c)
