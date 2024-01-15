from abc import ABC, abstractmethod

class Trabajdor(ABC):
    
    @abstractmethod
    def comer(self):
        pass

class Comedor(ABC):    
    @abstractmethod
    def trabajar(self):
        pass
    
class Durmiente(ABC):
    
    @abstractmethod
    def dormir(self):
        pass
    
class Humano(Trabajdor, Durmiente, Comedor):
    def comer(self):
        print("El Humano esta comiendo")
        
    def trabajar(self):
        print("El Humano esta trabjando")
        
    def dormir(self):
        print("El Humano esta durmiendo")
        
class Robot(Trabajdor):
    def trabajar(self):
        print("El robot esta trabajando")      
        
robot = Robot()
humano = Humano()

robot.trabajar()
humano.trabjar()
humano.comer()