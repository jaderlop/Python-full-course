# Variables 
# las variables sirven para guardar datos en memoria, python es un lenguaje de tipo dinamico y de tipado fuerte

my_name = "manolo"
print(my_name)

# Las variables se puden reasignar

my_name = "manuel"
print(my_name)

# el tipo de dato se determina en tiempo de ejecucion no hay que declarlo explicitamente:
#No es necesario decir si es strink o int

print(type(my_name))
my_name = 10
print(type(my_name))
my_name = "manolo"
edad = 10 
años = 0 #int(input("ingresa una edad"))
print(f'Hola mi nombre es {my_name} y tengo {edad} y si sumo {años} a mi edad es {edad + años}')

# Forma de asignar variables

mi_nombre_es = "ok" #snake_case
nombre = "ok"

MiNombreEs = "ko" # pascalcase no recomendable
minombrees = "ko" # no recomendable

mi_nombre_es_123 = "ok" #Los numeros se agregan al final

# forma de crear constantes pero en python no existen solo se simulan
MI_NOMBRE = "ok" # forma de crear constante

# Al crear variables no se pueden usar: palabras reservadas, numeros iniciales, solo numero,
# con espacios

# Python es un lenguaje dinamico y fuerte


# Esto es una forma de hacer que la variable solo hacebte valores booleano que son falsos
## Son anotaciones

### De igual manera al ejecutarse el codigo esta variable se puede reasignar con otros valores
### Esto no afecta la ejecucion del programa

logger: bool = False
print(logger)

logger = 20
print(logger)
print(type(logger))

