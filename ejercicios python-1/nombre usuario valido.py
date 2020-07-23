print("ingrese nombre de usuario")
usuario=(input())
while len(usuario)>6 and len(usuario)<12:
	print("true")
if(len(usuario)<6):
	print("el nombre de usuario debe tener al menos 6 caracteres")
if(len(usuario)>12):
	print("el nombre de usuario no puede contener mas de 12 caracteres")
if(usuario)!=(str):
	print("el nombre de usuario debe contener solo letras y numeros")



