def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la funcion")
        
        funcion()
        print("Despues de llamar a la funcion")
        
def saludo():
    print("Hola dalto como andas")
    
saludo_modificado = decorador(saludo)
saludo_modificado()

@decorador
def salduo():
    print("HOla dalto como andas")
    
saludo()
