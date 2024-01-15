class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f'Persona(nombre={self.nombre}, edad= {self.edad})' 
    
    def __repr__(self) -> str:
        return f'Persoba("{self.nombre},{self.edad})'
    
    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+ otro.nombre,nuevo_valor)
    
            
dalto = Persona("Lucas",21)
maria = Persona("Maria",18)

nueva_persona = dalto + maria

print(nueva_persona.nombre)
