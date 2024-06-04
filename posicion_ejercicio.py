import numpy as np
import matplotlib.pyplot as plt

def s(t, m, g, k, Vo):
    return ((m*g*t)/k) - (m/k) * np.exp(-(k*t)/m) * (Vo - (m*g)/k) + (m/k) * (Vo - (m*g)/k)


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
    t_evaluar = np.linspace(0, 60, 400)  # Se graficará desde t=0 hasta t=30
    
    # Calcular los valores de s(t) para cada valor de tiempo
    s_evaluar = s(t_evaluar, m, g, k, Vo)
    
    # Graficar s(t)
    plt.plot(t_evaluar, s_evaluar)
    plt.title('Gráfico de s(t) de acuerdo al ejercicio')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('s(t)')
    plt.grid(True)
    
    
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
