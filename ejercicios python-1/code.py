
print("ingrese los codigos de las carreras")
code=int(input())
code_impares=1
while(code>1):
	digito=code%10
	code=code//10
	if(digito%2==1):
		code_impares=digito
		print("el código tiene numeros impares")