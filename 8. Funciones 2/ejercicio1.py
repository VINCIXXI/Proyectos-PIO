"""calculadora con funciones anidadas"""
def calculadora (operador,x,y) :
    def suma (a,b) :
        return a + b
    def resta (a,b) :
        return a - b
    def multiplicar (a,b) :
        return a * b
    def division (a,b) :
        if b!=0:
            return a / b
        else:
            return "No se puede dividir por cero"
    if operador == "sumar":
        return suma(x,y)
    elif operador == "restar":
        return resta(x,y)
    elif operador == "multiplicar":
        return multiplicar(x,y)
    elif operador == "dividir":
        return division(x,y)
    else:
        return "Operador no valido"
    
#ejemplo de uso 
resultado = calculadora("sumar",5,3)
print("Resultado: ",resultado)