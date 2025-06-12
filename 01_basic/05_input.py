## El input es una forma de que el programa pida informacion al usuario
## y operar con estos datos 


#nombre = input("Hola cual es tu nombre?")

#print(f'Hola {nombre}')


## ESTA ES UNA MALA PRACTICA (INVESTIGAR BIEN LA FUNCION. SPLIT())
country, city =input("En que paise vives").split()

print(f"Vives en {country} y la ciudad {city}")
