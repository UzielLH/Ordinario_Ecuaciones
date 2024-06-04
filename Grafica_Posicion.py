import numpy as np
import matplotlib.pyplot as plt

def s(t, m, g, k, Vo):
    return ((m*g*t)/k) - (m/k) * np.exp(-(k*t)/m) * (Vo - (m*g)/k) + (m/k) * (Vo - (m*g)/k)

def calcular_tiempo_90_porciento(m, g, k, Vo):
    return -(m * np.log((-0.1 * m * g) / (k * Vo - g * m))) / k

def main():
    try:
        # Solicitar al usuario que ingrese los valores
        m = float(input("Ingresa la masa (kg): "))
        g = float(input("Ingresa el valor de la gravedad (m/s^2): "))
        k = float(input("Ingresa el valor de la constante de resistencia del aire (Ns/m): "))
        Vo = float(input("Ingresa la velocidad inicial (m/s): "))
    except ValueError:
        print("Error: Ingrese valores numéricos para la masa, la gravedad, la constante y la velocidad inicial.")
        return
    
    if m <= 0 or k <= 0:
        print("Error: La masa y la constante deben ser valores positivos.")
        return

    # Crear un array de valores de tiempo
    t_evaluar = np.linspace(0, 500, 1000)  # Se graficará desde t=0 hasta t=30
    
    # Calcular los valores de s(t) para cada valor de tiempo
    s_evaluar = s(t_evaluar, m, g, k, Vo)
    
    # Graficar s(t)
    plt.plot(t_evaluar, s_evaluar)
    plt.title('Gráfico de s(t)')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('s(t)')
    plt.grid(True)
    
    # Encontrar el tiempo cuando la posición alcanza el 90% del valor máximo
    t_90_porciento = calcular_tiempo_90_porciento(m, g, k, Vo)
    
    # Calcular el valor de s(t) en t_90_porciento
    s_90_porciento = s(t_90_porciento, m, g, k, Vo)
    
    # Agregar una línea vertical en el tiempo t_90_percent
    plt.axvline(x=t_90_porciento, color='r', linestyle='--', label=f'Tiempo al 90% de s_max: {t_90_porciento:.2f} s')
    
    # Agregar una línea horizontal en el valor de s_max * 0.9
    plt.axhline(y=s_90_porciento, color='g', linestyle='--', label=f'90% de s_max: {s_90_porciento:.2f} m')
    
    # Agregar un punto en el gráfico en (t_90_percent, 0.9 * s_max)
    plt.plot(t_90_porciento, s_90_porciento, 'bo', label=f'Punto en 90% de s_max')
    
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
