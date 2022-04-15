edad= int(input("ingresa tu edad:  "))
maculino= False 

sexo= int(input(""" 
ingresa tu edad: 
[1]para masculino
[2]para femenino 
>>>"""))

if sexo== 1:
    masculino= True 
elif sexo==2:
    masculino= False 

else:
    print("esa opcion no es valida")
    exit()

if edad>= 18 and edad<=70:
    if masculino:
        print(f"hola caballero de {edad} años de edad")
    else:
        print(f"hola dama de{edad} años de edad")

else:
    print("hola para poder usar el programa debes ser mayor de de 18 y menor de 70 años  ") 

    exit()           