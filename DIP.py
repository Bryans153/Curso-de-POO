#class Diccionario:
#    def verificar_palabra(self, palabra):
#    #logica ara verificar palabras 
#    pass

#class CorrectorOrtogradico:
#    def __init__(self):
#        self.diccionario = Diccionario()
        
#    def corregir_texto(self, texto):
#        #usamos el diccionario para corregir el texto
#        pass
    
    
from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verficar_palabra(self, palabra):
        pass
    
    
class Dicionario(VerificadorOrtografico):
    def verficar_palabra(self, palabra):
        #logica para verificar palabras si esta en el diccionario
        pass
    
class CorrectorOrtografico:
    def __init__(self,verificador):
        self.verificador = verificador
        
    def corregir_texto(self, texto):
        # usamos para corregir el texto
        pass
        
        
corrector = CorrectorOrtografico(servicioWeb())