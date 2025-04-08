import numpy as np
import matplotlib.pyplot as plt
import random
import time

def postas_hitratacion(mapa_carrera):
    mapa_carrera.sort(key=lambda postas: postas[1])
    postas_hitratacion = []
    ultima_posta = 0
    cantidad_postas = len(mapa_carrera)

    for i in range(1, cantidad_postas):
        distancia_actual = mapa_carrera[i][1] - mapa_carrera[ultima_posta][1]
        
        if distancia_actual > 7:
            if ultima_posta == 0 and mapa_carrera[i - 1][1] > 7:
                postas_hitratacion.append(mapa_carrera[ultima_posta])
            postas_hitratacion.append(mapa_carrera[i - 1])
            ultima_posta = i - 1

    if mapa_carrera[cantidad_postas - 1][1] - mapa_carrera[ultima_posta][1] > 7:
        postas_hitratacion.append(mapa_carrera[-1])
             
    return postas_hitratacion

def generar_carrera(n_postas):
    carrera = []
    kilometro = 0  # Comenzamos en el kilómetro 0

    for i in range(n_postas):
        incremento = random.randint(1, 7)  # Genera un número aleatorio entre 1 y 10
        kilometro += incremento  # Suma el incremento al total de kilómetros
        carrera.append((f"Posta {i + 1}", kilometro))  # Añade la tupla a la lista

    return carrera

def medir_tiempo(n):
    """
    Genera un mapa de n ciudades y mide el tiempo de ejecución de postas_hitratacion.
    """
    mapa = generar_carrera(n)
    inicio = time.perf_counter()
    postas_hitratacion(mapa)
    fin = time.perf_counter()
    return fin - inicio

# Parámetros del gráfico
n_max = 500000
salto = 2000

n_values = list(range(100, n_max + 1, salto))
tiempos = [medir_tiempo(n) for n in n_values]

# Suavizado con promedio móvil
ventana = 5
tiempos_suavizados = np.convolve(tiempos, np.ones(ventana)/ventana, mode='valid')

# Graficar
plt.figure(figsize=(10,6))
plt.plot(n_values[:len(tiempos_suavizados)], tiempos_suavizados, label="Tiempo (promedio móvil)", color="green", linewidth=2)
plt.xlabel("Cantidad de ciudades")
plt.ylabel("Tiempo de ejecución (s)")
plt.title("Tiempo de ejecución de postas_hitratacion vs. tamaño del mapa")
plt.legend()
plt.grid(True)
plt.show()
