class Persona:
    def _init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre 
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print(f"Hola, estoy hablando un poco")


class Empleado(Persona):
    def  _init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario


class Estudiante(Persona):
    def  _init__(self,nombre,edad,nacionalidad,notas,universidad):
        super().__init__(nombre,edad,nacionalidad)
        self.notas = notas
        self.universisadad = universidad


roberto = Empleado("Roberto",43,"Argentino")

print(roberto.nacionalidad)

    