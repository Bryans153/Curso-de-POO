class Persona:
    def _init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre 
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola, estoy hablando un poco")


class Artista:
    def  _init__(self,habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return f"Mi habilidad es; {self.habilidad}"


class EmpleadoArtista(Persona,Artista):
    def  _init__(self,nombre,edad,nacionalidad,habilidad,empresa,salario):
        Persona().__init__(nombre,edad,nacionalidad)
        Artista().__init__(habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        print(f'Hola, soy : {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}')
    
roberto = EmpleadoArtista("Roberto",43,"argentino", "Cantar","Google",10000)

roberto.presentarse()
