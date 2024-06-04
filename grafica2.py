import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Función que representa la ecuación diferencial
def modelo(v, t, g, k, m):
    """
    Ecuación diferencial que modela el movimiento de un objeto bajo la influencia de la gravedad y la resistencia del aire.

    Parámetros:
    v: Velocidad
    t: Tiempo
    g: Gravedad (m/s^2)
    k: Constante de resistencia del aire (Ns/m)
    m: Masa (kg)
    """
    dvdt = g - (k/m) * v
    return dvdt

# Pedir al usuario los valores de los parámetros
try:
    v0 = float(input("Ingresa la velocidad inicial (m/s): "))
    g = float(input("Ingresa el valor de la gravedad (m/s^2): "))
    m = float(input("Ingresa el valor de la masa (kg): "))
    k = float(input("Ingresa el valor de la constante de resistencia del aire (Ns/m): "))

except ValueError:
    print("Error: Ingresa valores númericos")
    exit()

# Resolver la ecuación diferencial
t = np.linspace(0, 50, 200)  # Rango de tiempo
sol = odeint(modelo, v0, t, args=(g, k, m))

# Graficar
fig, ax1 = plt.subplots()

color = 'tab:blue'
ax1.set_xlabel('Tiempo (s)')
ax1.set_ylabel('Velocidad (m/s)', color=color)
ax1.plot(t, sol, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Resistencia del aire (N)', color=color)
resistencia = k * sol.flatten()  # Calcula la resistencia del aire
ax2.plot(t, resistencia, color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Solución de la ecuación diferencial mdv/dt = mg - kv')
plt.grid(True)
ax1.grid(True)  # Activa la cuadrícula en los ejes ax1
ax2.grid(True)  # Activa la cuadrícula en los ejes ax2
plt.show()
