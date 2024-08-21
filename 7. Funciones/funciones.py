#funcion simple
def saludar ():
    print("Hola soy funciones")

    saludar() # Llamamos a la función

#funcion con parametros
def saludar2 (nombre):
    print("Hola soy", nombre)

    saludar2("funciones con parametros") # Llamamos a la función

#funcion con parametros y retorno
def suma (a,b):
    return a + b

resultado = suma(5,3)
print(resultado) # Imprime resultado