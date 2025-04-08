import numpy as np
import matplotlib.pyplot as plt
import time
import random

tiempos = []

def generar_carrera(n_postas):
    carrera = []
    kilometro = 0  # Comenzamos en el kilómetro 0

    for i in range(n_postas):
        incremento = random.randint(1, 7)  # Genera un número aleatorio entre 1 y 10
        kilometro += incremento  # Suma el incremento al total de kilómetros
        carrera.append((f"Posta {i + 1}", kilometro))  # Añade la tupla a la lista

    return carrera

def postas_hitratacion(mapa_carrera):

    mapa_carrera.sort(key=lambda posta: posta[1])
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


valores_n = [100000, 200000, 300000, 400000, 500000]

for valor in valores_n:
    carrera = generar_carrera(valor)
    t1 = time.time()
    postas_hitratacion(carrera)
    t2 = time.time()
    tiempos.append(t2-t1)
    
# Graficar
plt.figure(figsize=(8,6))
plt.plot(valores_n[:len(tiempos)], tiempos, label="Tiempos", color="blue")
plt.xlabel("n")
plt.ylabel("Tiempo (s)")
plt.title("Comparación del tiempos: de 100.000, 200.000, 300.000, 400.000 y 500.000")
plt.legend()
plt.grid(True)
plt.show()