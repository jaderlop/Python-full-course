def hola():

    from Registro_Apellido_01 import Apellido
    from Registro_Nombre_01 import Nombre

    # Aqui llamo a unas funciones previamente creadas y les paso el dato que se pide
    #nombre = Nombre()
    #apellido = Apellido()
    #print(f'Hola {nombre}, {apellido} vamos a hackear tu mente, la realidad y el mundo')

    # Normal
    print("hola mundo")
    # Con comillas simples
    print('tambien con comillas simples')
    # Separado por comas
    print("tambien","esto","Sirve","Separado por comas")
    # Definiendo el separado
    print("tambien","esto","Sirve","Separado por comas", sep="_")
    # Definiendo el final
    print("hola muchacho", end="/")
    print("que tal")

if __name__=="__main__":
    hola()
     