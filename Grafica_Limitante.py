import numpy as np
import matplotlib.pyplot as plt

def V(m, g, k):
    return m*g/k

def main():
    try:
        # Solicitar al usuario que ingrese los valores
        m = float(input("Ingresa la masa (kg): "))
        g = float(input("Ingresa el valor de la gravedad (m/s^2): "))
        k = float(input("Ingresa el valor de la constante de resistencia del aire  (Ns/m): "))
    except ValueError:
        print("Error: Ingresa valores numéricos para la masa, la gravedad y la constante de resistencia del aire.")
        return
    
    if m <= 0 or k <= 0:
        print("Error: La masa y la constante de resistencia deben ser valores positivos.")
        return

    # Calcular el valor constante de V(t)
    V_constant = V(m, g, k)
    
    # Graficar V(t)
    plt.axhline(y=V_constant, color='r', linestyle='-', label='V(t) = mg/k')
    plt.title('Gráfico de Velocidad Limitante')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('V(t)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
