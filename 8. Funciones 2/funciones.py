def funciones_externa (mensaje) :
    print (f"Mensaje desde la función externa: {mensaje}")
    
    def funciones_interna () :
        print (f"Mensaje desde la función interna: {mensaje}")

    funciones_interna()
    
funciones_externa("Hola mundo") 
