class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")


class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")


class Camion():

    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")

def desplazamientoVehiculo(Vehiculo):
    Vehiculo.desplazamiento()


miVehiculo= Coche()

desplazamientoVehiculo(miVehiculo)