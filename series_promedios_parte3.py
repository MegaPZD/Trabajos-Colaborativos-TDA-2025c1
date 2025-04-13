from suma_encadenada import backtracking

import time
import random

tiempos = [[0,0,0,0,0] for _ in range(0,5)]
promedios = []
valores_n = [100, 200, 300, 400, 500]
i = 0
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

for valor in valores_n:

    for j in range(0,5):
        t1 = time.perf_counter()
        resultado = suma_encadenada_minima(valor)
        t2 = time.perf_counter()
        tiempos[i][j]= t2 - t1
    promedios.append((sum(tiempos[i]))/5)
    i += 1

for i in range(0,5):
    print(f"tiempos de los valores {valores_n[i]}:")
    print(tiempos[i])
    print(f"promedio de los valores {valores_n[i]}:")
    print(promedios[i])