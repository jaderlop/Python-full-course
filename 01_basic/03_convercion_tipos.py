# Cambio de tipos a otros de un strink a un numero

print("Conversion de tipos")
print("100")
print(type("100"))
print(int("100")+1)
print(type(int("100")+1))

print(type("100"+str(1)))

#El unico valor numerico que es false es el 0
print(bool(2))
print(bool(0))
print(bool(-2))

#El unico valor de texto que es falsa es el vacio
print(bool("hola"))
print(bool(" "))
print(bool(""))