#edad=aact-anac
# #Declarar variables
anac=0
aact=0
#datos de salida 
edad=0
#solicitar los datos
aact=int(input("Dame el año actual:"))
anac=int(input("Dame el año de nacimiento:"))
#Calcular la edad 
edad = aact-anac
#Mostrar los resultados
print(f"si naciste en el año {anac} en el año {aact} tendras {edad} años")
#Datos de salida sin If
print(f"Tu edad es:{edad},")