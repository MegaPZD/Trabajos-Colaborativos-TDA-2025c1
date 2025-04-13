import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter
from suma_encadenada import backtracking
tiempos = []

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

valores_n = [100, 200, 300, 400, 500, 1000]

for valor in valores_n:
    t1 = perf_counter()
    resultado = suma_encadenada_minima(valor)
    t2 = perf_counter()
    tiempos.append(t2-t1)
    
# Graficar
plt.figure(figsize=(8,6))
plt.plot(valores_n[:len(tiempos)], tiempos, label="Tiempos", color="blue")
plt.xlabel("n")
plt.ylabel("Tiempo (s)")
plt.title("Comparación del tiempos: de 100, 200, 300, 400, 500 y 1.000")
plt.legend()
plt.grid(True)
plt.show()