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


class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar
        if self.cargado:
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"


class Moto(Vehiculos):
    hcaballito = ""
    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
              self.enmarca, "\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena, "\n", self.hcaballito)


class VElectricos():
    def __init__(self):
        self.autonomia=100

    def cargarEnergia(self):

        self.cargando = True


miMoto = Moto("honda", "CRB")

miMoto.caballito()

miMoto.estado()

miFurgoneta=Furgoneta("Renault", "Kangoo")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True))

class BicicletaEñlectrica(VElectricos, Vehiculos):

    pass

miBici= BicicletaElectrica()