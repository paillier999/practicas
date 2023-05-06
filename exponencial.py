# Código para representar el crecimiento bacteriano

import math

import matplotlib.pyplot as plt

euler = math.e

x = list(range(1,10))

y = [round(math.exp(v),2) for v in x]

plt.plot(x,y)
plt.xlabel('Eje X (Tiempo en horas)')
plt.ylabel('Eje Y (colonias de bacterias)')
plt.title('Crecimiento bacteriano representado mediante la función exponencial')

# Mostrar el gráfico
plt.show()