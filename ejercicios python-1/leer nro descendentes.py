print("ingrese tres números enteros: ")

a=int(input())
b=int(input())
c=int(input())

if(a>b and b>c):
	print(a,b,c)
if(c>b and b>a):
	print(c,b,a)
if(b>c and c>a):
	print(b,c,a)
if(a>c and c>b):
	print(a,c,b)
if(c>a and a>b):
	print(c,a,b)
else:
	print(b,a,c)
                	

	


