import numpy as np
import matplotlib.pyplot as plt

def v(t, m, g, k, Vo):
    return (m*g/k) + (Vo - (m*g/k)) * np.exp(-k*t/m)

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
    t_evaluar = np.linspace(0, 400, 1000)  # Se graficará desde t=0 hasta t=20
    
    # Calcular los valores de v(t) para cada valor de tiempo
    v_evaluar = v(t_evaluar, m, g, k, Vo)
    
    # Calcular los valores de s(t) para cada valor de tiempo
    s_evaluar = s(t_evaluar, m, g, k, Vo)
    
    # Encontrar el tiempo cuando la posición alcanza el 90% del valor máximo
    t_90_porciento = calcular_tiempo_90_porciento(m, g, k, Vo)
    
    # Calcular el valor de v(t) en t_90_porciento
    v_90_porciento = v(t_90_porciento, m, g, k, Vo)
    
    # Calcular el valor de s(t) en t_90_porciento
    s_90_porciento = s(t_90_porciento, m, g, k, Vo)
    
    # Crear la figura y los ejes
    fig, ax1 = plt.subplots()
    
    # Graficar v(t) en el primer eje y configurar su color
    color = 'tab:blue'
    ax1.set_xlabel('Tiempo (s)')
    ax1.set_ylabel('v(t)', color=color)
    ax1.plot(t_evaluar, v_evaluar, color=color, label='v(t)')
    ax1.tick_params(axis='y', labelcolor=color)
    
    # Agregar una línea vertical en el tiempo t_90_percent para v(t)
    ax1.axvline(x=t_90_porciento, color='r', linestyle='--', label=f'Tiempo al 90% de v_max: {t_90_porciento:.2f} s')
    
    # Agregar una línea horizontal en el valor de v_max * 0.9
    ax1.axhline(y=v_90_porciento, color='g', linestyle='--', label=f'90% de v_max: {v_90_porciento:.2f} m/s')
    
    # Agregar un punto en el gráfico en (t_90_percent, 0.9 * v_max)
    ax1.plot(t_90_porciento, v_90_porciento, 'bo', label=f'Punto en 90% de v_max')
    
    # Configurar la leyenda para el primer eje
    ax1.legend(loc='upper left')
    
    # Crear el segundo eje compartiendo el eje x con el primer eje
    ax2 = ax1.twinx()
    
    # Graficar s(t) en el segundo eje y configurar su color 
    color = 'tab:red'
    ax2.set_ylabel('s(t)', color=color)
    ax2.plot(t_evaluar, s_evaluar, color=color, label='s(t)')
    ax2.tick_params(axis='y', labelcolor=color)
    
    
    # Agregar una línea vertical en el tiempo t_90_porciento para s(t)
    ax2.axvline(x=t_90_porciento, color='r', linestyle='--', label=f'Tiempo al 90% de s_max: {t_90_porciento:.2f} s')
    
    # Agregar una línea horizontal en el s_90_porciento
    ax2.axhline(y=s_90_porciento, color='g', linestyle='--', label=f'90% de s_max: {s_90_porciento:.2f} m')
    
    # Agregar un punto en el gráfico
    ax2.plot(t_90_porciento, s_90_porciento, 'bo', label=f'Punto en 90% de s_max')
    
    # Configurar la leyenda para el segundo eje
    ax2.legend(loc='upper right')
    
    # Agregar una cuadrícula al gráfico
    plt.grid(True)
    
    # Agregar un título explicativo al gráfico
    plt.title('Gráfico de velocidad y posición respecto a la resistencia del aire')
    
    # Mover las etiquetas de las líneas fuera del gráfico
    ax1.legend(loc='upper left', bbox_to_anchor=(0.0, 1.2), shadow=True, ncol=1)
    ax2.legend(loc='upper right', bbox_to_anchor=(1.0, 1.2), shadow=True, ncol=1)
    
    # Mostrar la figura
    fig.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
