import numpy as np
import matplotlib.pyplot as plt

def v(t, m, g, k, Vo):
    return (m*g/k) + (Vo - (m*g/k)) * np.exp(-k*t/m)

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
        print("Error: Ingresa valores numéricos para la masa, la gravedad, la constante de resistencia y la velocidad inicial.")
        return
    
    if m <= 0 or k <= 0:
        print("Error: La masa y la constante de resistencia deben ser valores positivos.")
        return

    # Crear un array de valores de tiempo
    valores_tiempo = np.linspace(0, 500, 1000)  # Se graficará desde t=0 hasta t=30
    
    # Calcular los valores de v(t) para cada valor de tiempo
    valores_v = v(valores_tiempo, m, g, k, Vo)
    
    # Graficar v(t)
    plt.plot(valores_tiempo, valores_v)
    plt.title('Gráfico de v(t)')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('v(t)')
    plt.grid(True)
    
    # Encontrar el tiempo cuando la velocidad alcanza el 90% del valor máximo
    t_90_porciento = calcular_tiempo_90_porciento(m, g, k, Vo)
    
    # Calcular el valor de v(t) en t_90_porciento
    v_90_porciento = v(t_90_porciento, m, g, k, Vo)
    
    # Agregar una línea vertical en el tiempo
    plt.axvline(x=t_90_porciento, color='r', linestyle='--', label=f'Tiempo al 90% de v_max: {t_90_porciento:.2f} s')
    
    # Agregar una línea horizontal en velocidad
    plt.axhline(y=v_90_porciento, color='g', linestyle='--', label=f'90% de v_max: {v_90_porciento:.2f} m/s')
    
    # Agregar un punto en el gráfico
    plt.plot(t_90_porciento, v_90_porciento, 'bo', label=f'Punto en 90% de v_max')
    
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
