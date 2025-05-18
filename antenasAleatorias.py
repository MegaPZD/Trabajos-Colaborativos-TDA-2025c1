"""resultado  = antenas_mediante_flujo(5, [ 
    [0, 3, 4, 4, 3],
    [3, 0, 3, 3, 7],
    [4, 3, 0, 4, 3],
    [4, 3, 4, 0, 3],
    [3, 7, 3, 3, 0]
], 2, 2, 4)"""

import antenas
import random
import sys

def generadorAntenasAleatorias(usando_seed=False, seed=(-1)):

    if not usando_seed:
        seed = random.randint(0, 999999)
    print(f"Usando seed: {seed}")
    random.seed(seed)

    n  = random.randint(5, 20)
    D = random.randint(20, 100)
    k = random.randint(2, max(2, n // 2))
    b = random.randint(2, max(2, (3 * n) // 2))
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i,n):
            if i == j:
                continue
            matriz[i][j] = matriz[j][i] = random.randint(1, 100)

    print(f"Se genero una situción aleatoria (resoluble o no) con los siguientes parametros:\nCantidad de antenas: {n}, k: {k}, b: {b} y D: {D}\ny la matriz:\n")
    for i in range(n):
        print(f"{matriz[i]}")
    return antenas.antenas_mediante_flujo(n,matriz,k,b,D)

     
resultado = dict()
if __name__ == "__main__":
    if len(sys.argv) != 2:
        resultado = generadorAntenasAleatorias()
    else:
        seed = int(sys.argv[1])
        resultado = generadorAntenasAleatorias(True, seed)
if resultado:
    for clave, valor in resultado.items():
        print(f"{clave}: {valor}")