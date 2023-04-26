class Coche():
    def __init__(self, largoChasis, anchoChasis, ruedas, enmarcha):
        self.largoChasis = largoChasis
        self.anchoChasis = anchoChasis
        self.ruedas = ruedas
        self.enmarcha = enmarcha

    def arrancar(self, arrancamos):
        self.enmarcha=arrancamos

        if(self.enmarcha):
            return "El coche está en marcha"

        else:

            return "El coche está detenido"

    def estado(self):
        print("El coche tiene: ", self.ruedas, "ruedas. Un ancho de ", self.anchoChasis, " y un largo de ",
              self.largoChasis)


miCoche = Coche(245,34,4,True)

miCoche.estado()

print("------------------A continuación creamos el segundo objeto----------------")

miCoche2=Coche(159,24,4, False)

miCoche2.estado()

miCoche3 =Coche(45,67,3,False)

miCoche3.estado()