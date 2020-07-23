#informar sitios turisticos, provincia y cantidad de visitantes.
#ordenada por sitios, provincia, y cant de visitantes



ZZZ=input()
sitio_anterior=input()
cant_vis=0
sitio=0
while(sitio!=ZZZ):
	lugar=input("ingrese nombre del sitio:  ")
	sitio_anterior=sitio
	while (sitio!=ZZZ) and (sitio_anterior==sitio):
		provincia=input("ingrese provincia:  ")
		visitantes=int(input("ingrese cantidad de visitantes:  "))
		cant_vis=cant_vis+visitantes
		
		
		sitio=sitio+1
		print (sitio_anterior,cant_vis)











