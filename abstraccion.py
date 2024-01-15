class Auto():
    def __init__(self):
        self.estado = "apagado"
        
    def encender(self):
        self.estado = "encendido"
        print("El auto esta encendido")
        
    def conducir(self):
        self.__estado == "apagado"
        self.encender()
        print("Conduciendo el auto")
        
mi_auto = Auto()
mi_auto.conducir()