"""funciones anidadas para validar y filtrar los datos"""
def procesar_numeros(numeros:list):
     def es_positivo(n):
            return n>0
     def filtros (lista):
        totalPositivos=0
        totalNegativos=0

        for numero in lista:
            if es_positivo(numero):
                totalPositivos+=numero
            else:
                totalNegativos+=numero
        return {
            "Positivos": totalPositivos, 
            "Negativos": totalNegativos
            }
 
     return filtros(numeros)

numeros=[-6,5,-4,5,4]
resultado=procesar_numeros(numeros)
#print(type(numeros))
print(f"La suma de los numeros positivos es: {resultado["Positivos"]}")
print(f"La suma de los numeros negativos es: {resultado["Negativos"]}")