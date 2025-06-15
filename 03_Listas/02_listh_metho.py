import os
os.system('clear')

lista = [1,2,3,4,5,6,7,8,9,10]

# Metodo append agrega un elemento al final
print(lista)
lista.append(11)
print(lista)

# Metodo insert agrega un elemento en la posicion que le 
# indiquemos como parametro

lista.insert(4,'j')
print(lista)

# Metodo len tamaño de una lista o caracter
print(len(lista))
# Tambien funciona con carecteres no funciona con numero


nombre = "aaabcdefg"
numero = 10
print(f'{nombre}: {len(nombre)}')
# print(f'{numero}: {len(numero)}')

# Puedo covertir texto en listas cambiando su tipo de objeto
# Recordar hacer copias para querer volver al nombre original
# Por si acaso

# Los metodos append y extend funcionan de forma diferente


nombre_lista = list(nombre)
nombre_lista.append("123456")
nombre_lista.extend("123456")
print(nombre_lista)

# Metodo Remove elimina la primera aparicion de un elemento en una lista
# aunque guarde la lista en una nueva una vez que elimine el elemnto este desaparece de la lista original
# Es importante hacer copias

nombre_eliminado = nombre_lista.remove("b")
print(nombre_eliminado)


# pop elimina el ultimo elemento de la lista  o el que definamos y lo podemos guardar en una variable
# 

ultimo_lita = nombre_lista.pop(0)
print(ultimo_lita)
print(nombre_lista)
print(ultimo_lita)

# del elimina la lista
#print(nombre_lista)
#del nombre_lista

# Metodo clear elimina todos los elementos de la lista
# peros se conserva la variable que contenia esos valores
nombre_lista.clear()
print(nombre_lista)

os.system('clear')
#Metodo sort
# ordenar los elementos de una lista modificando la lista original
# CUIDADO ALTERA LOS VALORES DE UNA LISTA 
lista_n = [1,0,2,26,7,3,4,3,7,2,3,16]
lista_ordenada = lista_n.sort()

print(lista_n)
print(lista_ordenada)

# si se quiere ordenar los valores de una lista y conservar la original
# se utiliza la funcion sorted y se le pasa como parametro la lista
lista_n = [1,0,2,26,7,3,4,3,7,2,3,16]
lista_ordenada = sorted(lista_n)
print(lista_ordenada)
print(lista_n)

# al ser un lenguaje lexicografico las palabras se ordenaran por la pirmera
# letra que las compone, tener cuidad con las mayusculas ya que las pone de primero
lista_l = ["manzan","pera","manzana","mandarina","alimon","pera","a"]
lista_letra_ordenada = sorted(lista_l)


print(lista_l)
print(lista_letra_ordenada)

lista_l = ["manzan","pera","Manzana","mandarina","alimon","pera","a"]
lista_letra_ordenada = sorted(lista_l)

print(lista_l)
print(lista_letra_ordenada)

# Existen metodos y parametros que se pueden completar en las funciones
# si queremos que se ordenen dependiendo de las mayusculas o minusculas 
# hay que difinirlo

lista_l_copia = lista_l
lista_l_copia.sort(key=str.lower)
print(lista_l_copia)
print(lista_l)

# count es un metodo que me permite saber cuantas veces aparece un elemento en una lista
buscar = "carro"
print(f'en la lista hay {lista_l.count(buscar)}, {buscar}')

if buscar in lista_l:
    print(f'en la lista hay {lista_l.count(buscar)}, {buscar}')
else:
    print(f'en la lista no esta {buscar}')
