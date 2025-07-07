import random
import sys
import time

MAX_VAL = 10000

def subconjuntoOptimoDP(A: list[int], B: int) -> list[int]:
    n = len(A)

    dp = [[False] * (B + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(B + 1):
            if j >= A[i - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - A[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    for suma in range(B, -1, -1):
        if dp[n][suma]:
            suma_max = suma
            break
    else:
        return []

    S_opt = []
    i, j = n, suma_max
    while i > 0 and j > 0:
        if not dp[i - 1][j]:
            S_opt.append(A[i - 1])
            j -= A[i - 1]
        i -= 1

    return S_opt

def subconjuntoFactible(A: list[int], B: int):
    A_ordenado = sorted(A, reverse=True)
    S = []
    suma = 0

    for a in A_ordenado:
        if suma + a <= B:
            S.append(a)
            suma += a

    return S

def setDatos(usando_seed=False, seed=(-1)):
    if not usando_seed:
        seed = random.randint(0, 999999)
    random.seed(seed)

    B = random.randint(15, MAX_VAL)
    A = [random.randint(1, MAX_VAL) for _ in range(MAX_VAL//3)]

    print(f"A = {A}\nB = {B}")

    inicio_opt = time.perf_counter()
    S_opt = subconjuntoOptimoDP(A, B)
    final_opt = time.perf_counter()

    print(f"Tiempo que tomo resolverlo optimamente: {final_opt-inicio_opt}\nS optimo: {S_opt}")

    inicio = time.perf_counter()
    S = subconjuntoFactible(A, B)
    final = time.perf_counter()

    print(f"Tiempo que tomo resolverlo con aproximacion: {final-inicio}\nS: {S}")

    print(f"Usando seed: {seed}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        resultado = setDatos()
    else:
        seed = int(sys.argv[1])
        resultado = setDatos(True, seed)

if resultado:
    for clave, valor in resultado.items():
        print(f"{clave}: {valor}")