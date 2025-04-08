import numpy as np
import matplotlib.pyplot as plt
import time
import random

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

def generar_mapa(n):
    return [(f"Ciudad_{i}", random.uniform(0, 1000)) for i in range(n)]

def medir_tiempos(n_vals):
    tiempos = []
    
    for n in n_vals:
        mapa = generar_mapa(n)
        inicio = time.perf_counter()
        postas_hitratacion(mapa)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    
    return np.array(tiempos)

# Valores de n para probar
n_vals = np.linspace(100, 10000, 30, dtype=int)  # 30 valores desde 100 hasta 10.000
tiempos_reales = medir_tiempos(n_vals)

# Complejidad teórica O(n log n)
complejidad_teorica = n_vals * np.log(n_vals)
complejidad_teorica = complejidad_teorica / max(complejidad_teorica) * max(tiempos_reales)

# Gráfico
plt.figure(figsize=(8,6))
plt.plot(n_vals, tiempos_reales, label="Tiempo real", color="blue")
plt.plot(n_vals, complejidad_teorica, label=r"$O(n \log n)$", color="green")
plt.xlabel("Cantidad de ciudades (n)")
plt.ylabel("Tiempo (s)")
plt.title("Comparación del tiempo real vs. complejidad teórica - postas_hitratacion")
plt.legend()
plt.grid(True)
plt.show()
