class Vehiculos:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarca = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarca = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
              self.enmarca, "\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena)


class Moto(Vehiculos):
    pass


miMoto = Moto("honda", "CRB")


miMoto.frenar()

miMoto.estado()
