import matplotlib.pyplot as plt

intento = list(range(1, 11))
print(intento)

derecha = [10, 13, 18, 17, 20, 24, 23, 18, 12, 14]

izquierda = [13, 15, 15, 20, 16, 19, 16, 15, 24, 16]

plt.plot(intento, derecha, label="Mano derecha")
plt.plot(intento, izquierda, label="Mano izquierda")

plt.title("Distancia recorrida por la regla antes de atraparla entre dedo índice y pulgar.")
plt.xlabel("Intentos")
plt.ylabel("Distancia en cm")
plt.legend()
plt.show()
