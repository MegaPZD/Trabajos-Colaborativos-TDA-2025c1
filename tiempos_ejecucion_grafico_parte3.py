import numpy as np
import matplotlib.pyplot as plt
import time
from suma_encadenada import backtracking

def suma_encadenada_minima(n):
    if n == 1:
        return [1]
    
    sol = []
    n_aux = n
    
    while n_aux % 2 == 0 and n_aux > 2:
        n_aux //= 2
    
    if n_aux >= 100 and n_aux % 2 > 0:
        sol = suma_encadenada_minima(n_aux - 1)
        sol.append(n_aux)

    backtracking(n_aux, [1, 2], sol)

    while sol[-1] < n:
        sol.append(sol[-1] + sol[-1])
    print("Solucion encontrada: ", sol, " para n = ", n)
    
    return sol

def medir_tiempo(n):
    """
    Genera un mapa de n ciudades y mide el tiempo de ejecución de postas_hitratacion.
    """
    inicio = time.perf_counter()
    suma_encadenada_minima(n)
    fin = time.perf_counter()
    return fin - inicio

# Parámetros del gráfico
n_max = 1000
salto = 20

n_values = list(range(3, n_max + 1, salto))
tiempos = [medir_tiempo(n) for n in n_values]

# Graficar
plt.figure(figsize=(10,6))
plt.plot(n_values[:len(tiempos)], tiempos, label="Tiempo (promedio móvil)", color="green", linewidth=2)
plt.xlabel("Cantidad de ciudades")
plt.ylabel("Tiempo de ejecución (s)")
plt.title("Tiempo de ejecución de postas_hitratacion vs. tamaño del mapa")
plt.legend()
plt.grid(True)
plt.show()
