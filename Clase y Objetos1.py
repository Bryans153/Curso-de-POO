class Celular:
    def _init__(self, marca, modelo, camara):
        self.marca = marca 
        self.modelo = modelo
        self.camara = camara 

    def llamar(self):
        print(f'Estas haciendo un llamado desde un: {self.modelo}')

    def cortar(self):
        print(f'Cortaste la llamada desde tu: {self.modelo}')

celular1 = Celular("Samsung","S23","48MP")
celular2 = Celular("Apple","Iphone 15", "96Mp")

celular2.llamar()
