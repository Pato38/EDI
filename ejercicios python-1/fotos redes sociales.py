fotos=dict

fotos={'dim':input(),'titulo':input(),'autor':input(),'cant_mg':int(input()),'cant_clics':int(input()),'cant_coment':int(input())}

fotos['cant_clics']=int(input("ingrese cantidad de clics     "))
pmax=1
i=0
for i in range (dim):
	if(fotos['cant_clics']>pmax):
		
		pmax=fotos['cant_clics']
		fotos['cant_clics']=fotos['titulo']
		print("la foto con más clics es:    ", fotos['titulo'])


fotos['cant_mg']=int(input("ingrese cantidad de mg:   "))
max_mg=0
for fotos['cant_mg'] in range(dim):
	if(fotos['autor']==fotos[mart_vinderlays]):
		max_mg=fotos['cant_mg']+1
		max_mg =fotos['titulo']
		print("la foto con más mg es:    " , fotos['titulo'])


def cant_coment(cant_coment,titulo):
	cant_coment=0
	for cant_coment in range (fotos['titulo']):
		cant_coment=cant_coment+1
		return(cant_coment)
