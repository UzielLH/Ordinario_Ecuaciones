import numpy as np
import matplotlib.pyplot as plt

def v(t, m, g, k, Vo):
    return (m * g / k) + (Vo - (m * g / k)) * np.exp(-k * t / m)

def main():
    # Valores iniciales
    m = 72.41
    g = 9.8
    k1 = 0.5
    k2 = 10
    Vo = 0
    
    # Crear un array de valores de tiempo para la primera parte (0 a 15s)
    tiempo_1 = np.linspace(0, 15, 250)
    # Calcular los valores de v(t) para cada valor de tiempo con k1
    velocidad_1 = v(tiempo_1, m, g, k1, Vo)
    
    # Valor de velocidad al final de la primera parte
    v_final_1 = velocidad_1[-1]
    
    # Crear un array de valores de tiempo para la segunda parte (15 a 60s)
    tiempo_2 = np.linspace(15, 60, 750)
    # Calcular los valores de v(t) para cada valor de tiempo con k2, comenzando desde v_final_1
    velocidad_2 = v(tiempo_2 - 15, m, g, k2, v_final_1)
    
    # Unir las dos partes
    tiempo_total = np.concatenate((tiempo_1, tiempo_2))
    velocidad_total = np.concatenate((velocidad_1, velocidad_2))
    
    # Graficar v(t)
    plt.plot(tiempo_total, velocidad_total, label='v(t)')
    plt.title('Gráfico de v(t) del paracaidismo')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('v(t)')
    plt.grid(True)
    
    # Agregar una línea vertical y horizontal en t=15s para indicar el cambio en la constante k
    plt.axvline(x=15, color='r', linestyle='--', label=f'Tiempo: 15s, v: {v_final_1:.2f} m/s')
    plt.axhline(y=v_final_1, color='r', linestyle='--')
    # Agregar un punto en la intersección de t=15s
    plt.plot(15, v_final_1, 'ro')
    
    # Calcular la velocidad en t=20s
    tiempo_20 = 20
    v_20 = v(tiempo_20 - 15, m, g, k2, v_final_1)
    
    # Agregar una línea vertical y horizontal en t=20s
    plt.axvline(x=tiempo_20, color='b', linestyle='--', label=f'Tiempo: 20s, v: {v_20:.2f} m/s')
    plt.axhline(y=v_20, color='b', linestyle='--')
    # Agregar un punto en la intersección de t=20s
    plt.plot(tiempo_20, v_20, 'bo')
    
    # Calcular la velocidad en t=57.35s
    tiempo_57_35 = 57.35
    if tiempo_57_35 <= 15:
        v_57_35 = v(tiempo_57_35, m, g, k1, Vo)
    else:
        v_57_35 = v(tiempo_57_35 - 15, m, g, k2, v_final_1)
    
    # Agregar una línea vertical y horizontal en t=57.355s
    plt.axvline(x=tiempo_57_35, color='g', linestyle='--', label=f'Tiempo: {tiempo_57_35}s, v: {v_57_35:.2f} m/s')
    plt.axhline(y=v_57_35, color='g', linestyle='--')
    # Agregar un punto en la intersección de t=57.355s
    plt.plot(tiempo_57_35, v_57_35, 'go')
    
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
