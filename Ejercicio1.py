class Estudiante:
    def _init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

nombre = input("Digame su nombre: ")
edad = input("Ahora su edad: ")
grado = input("Por ultimo su grado: ")

estudiante = Estudiante(nombre,edad,grado)

print(f"""
      DATOS DEL ESTUDIANTE: \n\nonlocal
      Nombre: {estudiante.nombre} \n
      Edad: {estudiante.edad} \n
      Grado: {estudiante.edad} \n

      """)

while True:
    estudiar = input()
    if (estudiar,lower() == "estudiar"):
        estudiante.estudiar()

