print("ingrese numero")
num=int(input())
suma_digito_par=0
while(num>1):
	digito=int(num%10)
	num=num//10
	if(digito%2==0):
		suma_digito_par=suma_digito_par+digito
		print(suma_digito_par)