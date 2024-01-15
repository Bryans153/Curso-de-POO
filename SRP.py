class Auto():
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque
        
    def mover(self, distancia ):
        if self.tanque.obtener_combustible()>= distancia / 2:
            self. posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
        else:
            print("No hay suficiente combustible")
            
class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100
        
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad 
        
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad
        
tanque = TanqueDeCombustible()
autito = Auto(tanque)

print(autito)