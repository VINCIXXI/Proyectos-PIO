'''Escribe una función llamada es_par que reciba número
y devuelva el mayor de los dos'''

def es_par(numero):
    return numero % 2 == 0
num= int(input("Introduce un número: "))
print(es_par(num))
if es_par(num):
    print("Es par")
else:
    print("No es par")
    