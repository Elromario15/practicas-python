
tabla_a_multiplicar=int(input("ingresa el numero para multipicar: "))
hasta_donde=int(input(f"hasta donde desea calcular el numero {tabla_a_multiplicar} :"))

#print(f"{tabla_a_multiplicar} x 1={tabla_a_multiplicar *1}")
#print(f"{tabla_a_multiplicar} x 2={tabla_a_multiplicar *2}")
#print(f"{tabla_a_multiplicar} x 3={tabla_a_multiplicar *3}")
#print(f"{tabla_a_multiplicar} x 4={tabla_a_multiplicar *4}")

#num= 1

for i in range(hasta_donde):
    print(f"{tabla_a_multiplicar} x {i+1}= {tabla_a_multiplicar *(i+1)} ")
    #num=num+2