carreras=dict

carreras={"carrera_1":"sistemas","code1":222,"durac1":3,"cantalum1":5,"durac1":3,
"carrera_2":"politica","durac2":4,"cantalum2":24,"durac2":4,
"carrera_3":"agropecuario","durac3":3,"cantalum3":12,"durac3":3}
print(carreras)

dict=carreras
code_impares=1
if(carreras["code1"]>1):
	digito=carreras["code1"]%10
	digito=digito//10
	if(digito%2==1):
		code_impares=digito
		print("el código tiene numeros impares")