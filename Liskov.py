#Principio de sustitución de Liskov
class Rectangulo:
    def __init__(self, altura, ancho):
        self.altura, self.ancho = altura, ancho

    def area(self):
        return self.altura * self.ancho


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

    def set_lado(self, lado):
        self.altura = lado
        self.ancho = lado



Mirectan = Rectangulo(5,20)

print(Mirectan.area())

Micuadra = Cuadrado(5)

print(Micuadra.area())