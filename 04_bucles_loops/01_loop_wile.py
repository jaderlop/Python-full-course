# Los bucles son importantes ya que estos
# ejecutan una sentencia de codigo por un
# Tiempo definido o hasta que una condicion se 
# deje de cumplir

#CICLO WILE
print("ciclo wile")

contador = 0

while contador < 5:
    print(contador)
    contador += 1

import os

os.system('clear')

condicion = True

# el codigo de abajo me ejecuta un codigo infinito
# ya que la condicion siempre va a ser true
# para detener esto en la consola poner
# ctrl + c
#while condicion:
#    print(f'la condicion es {condicion}')
   

# BREAKE
# ya el contador trae un valor que se encontro
# lo verificamo y lo reasignamos para seguir practicando

print(contador)
contador = 0

# El break sirve para romper la condicion de busqueda de while
# ya que si no conocemos el valor de busqueda o si no sabemos si esta 
# en donde lo estamos buscand el breake nos ayudara a romper la busqueda
while contador < 1000:    
    contador += 1
    print(contador)
    
    if contador * 10 == 900:
        print(f'se encontor el contador; {contador}')
        break

os.system('clear')

# CONTINUE encuentra la iteracion la separa y continua con el ciclo
contador = 0 
objetivo = 27 # Lo que estamos buscando   

while contador < 30:    
    contador += 1
    
    if contador % 2 == 0:  # salta los numeros pares
        continue

    print(f'los numeros impares son {contador}')    
    if contador == objetivo:
        print(f'se encontro el objetivo {objetivo}')
        continue


# ELSE EN bucles while 
os.system('clear')

contador = 0 
objetivo = [7,15,23] # Lo que estamos buscando   

while contador < 30:    
    contador += 1
    
    if contador % 2 == 0:  # salta los numeros pares
        continue
        
    print(f'los numeros impares son {contador}')    
    if contador in objetivo:
        print(f'se encontro el objetivo {objetivo}')
        continue

else:
    print('el bucle termino')
    print(contador)

os.system('clear')

numero = int(input('ingresa un numero par: '))
print(numero)

while numero % 2 != 0:
    numero = int(input('usuario el numero no es par: '))
    print(numero)
else:
    print(f'si ese numero {numero} es par')


os.system('clear')
# TRY


        

