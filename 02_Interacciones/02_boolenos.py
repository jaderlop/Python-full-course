import os

print("Valores booleanos basicos ")

print(True)
print(False)

# Operadores de comparacion
print("5>3",5>3) #True
print("5<3",5<3) #False
print("5==5",5==5) #True igualdad
print("5!=3",5!=3) #True Desigualdad
print("5>=3",5>=3) #True mayor igual que
print("5<=3",5<=3) #True menor igual que

print("comparacion de cadenas")

os.system("clear")
###Python es un lenguaje de programacion lexicografico
### Locual hace que el interprete identifique los
### Elementos lexicos que componen el codigo fuente
#### osea qye la A va primero que la B

###
print("operacion de cadenas")
print("'mamzana < pera':","manzana"<"pera")
print("'Hola == hola':","Hola" == "hola")#Falso

os.system("clear")
print("AND")
print("Tabla de la verdad")
print("A     B     A and B")
print("True  True",True and True) # True
print("True  False",True and False) # False
print("False  True",False and True) # False
print("False  False",False and False) # False

print("or")
print("Tabla de la verdad")
print("A     B     A or B")
print("True  True",True or True) # True
print("True  False",True or False) # True
print("False  True",False or True) # True
print("False  False",False or False) # False

numero = 4
if numero:
    print("Elnumero es mayor que 0")

## Esta linea de codigo no se ejecuta
## ya que el 0 es un valor falso
numero = 0
if numero:
    print("Esto no sucedera")

# Recordar que si la variable de caracteres esta vacia
# Esto tomara el valor de falso
nombre = ""
if nombre:
    print(f'el nombre es {nombre}')
else:
    print(f'No hay nombre')    