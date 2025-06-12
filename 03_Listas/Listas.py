# Las listas son secuencias mutables
# De elementos de diferentes tip
print("Listas")

lista1 = [1,2,3,4,5,6]
lista2 = ["A","b","c","d"]
lista3 = [1,"hola",3.14, True]

lista_vacia = []
lista_de_lista =[[1,2],[3,4]]
matrix =[[1,2],[3,4],[4,5]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_lista)
print(matrix)

print("Acceso a los elementos de una lista")
print("SLICING")

print(f'la lista 1 tine {len(lista1)} valores')
print(lista1[0])
print(lista1[len(lista1)-1])
print(lista1[-1])

# el ultimo numero no esta agregado
print("lista1 por slicing del 2 al 5")
print(lista1[1:5])

print("estructura de la lista")
print("Desde : Hasta : pasos")
print(lista1[::2])

