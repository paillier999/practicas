#Programación orientada a objetos
class Coche(): # para especificar el estado inicial, se hace un constructor con el comando __init__(self).

    def __init__(self):

        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False #si queremos que estos atributos no cambien, entonces tenemos que "encapsularlos.

    def arrancar(self, arrancamos):
        self.enmarcha=arrancamos

        if(self.__enmarcha):
            return "El cohe está en marcha"
        else:
            return "El coche está detenido"

    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ",
              self.__anchoChasis, " y una largo de ", self.__largoChasis)

miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("-----A continuación creamos el segundo objeto-----")

miCoche2 = Coche()
print(miCoche2.arrancar(False))
miCoche2.ruedas=2
miCoche2.estado()