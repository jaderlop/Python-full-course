### 01 sentencias condicionales if, elif, else
## Sirve para cumplir condiciones

# El modulo os es muy interesante
# opera el ordenador
import os
os.system("clear")

print("sentencias")

edad = int(input("Que edad tienes:  "))
permiso = str(input("Tienes Permiso:   "))
#esta es uan funcion que pide la eda d
# No funciona si no se llama aunque
# el dato de la edad igual se pide y almacena

def Porteria(edad):

## BIFURCACION Es cuando el codigo toma caminos
    
    if edad >= 18:
        print(f"eres mayor de edad tienes {edad}")
    elif edad > 13:
        print(f"sube al segundo piso")
    elif edad < 13:
        print(f"Vete a casa tienes {edad}")

    #En el caso anterior este else no se va a ejecutar
    ## Ya que la bifurcacion desdtina las convinaciones
    ## de la edad
            
    else:
        print(f"No pasas ")


# Funcion para limpiar la consola
        
os.system('cls' if os.name == 'nt' else 'clear')


## Hay que tratar de no hacer if infinitos por que 
# El codigo entrara en bucles entreses si y no provechoso

def Permiso(edad, permiso):
    if edad >=18 and permiso == "Si":
        print(f"tienes {edad} pero con permiso")
    elif edad < 18 and permiso == "No":
        print(f"No tienes edad pero si persmiso")
    else:
        print("ingresa el permiso")
        

x = edad
y = edad + 10
Porteria(x)
Permiso(y, permiso)

