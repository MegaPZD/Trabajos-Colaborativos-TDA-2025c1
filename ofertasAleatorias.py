import random
import math
import sys
import time

def elegir_mejor_oferta(ofertas):
    n = len(ofertas)
    r = int(n / math.e)
    mejor_hasta_ahora = max(ofertas[:r])

    for i in range(r, n):
        if ofertas[i] > mejor_hasta_ahora:
            return ofertas[i]

    return ofertas[-1]  # si no encontró mejor

def generar_ofertas(n, semilla):
    random.seed(semilla)
    ofertas = [random.randint(1, 1000) for _ in range(n)]
    random.shuffle(ofertas)
    return ofertas

def correr_experimento(n=100, semilla=None):
    if semilla is None:
        semilla = random.randint(0, 999999)

    ofertas = generar_ofertas(n, semilla)
    mejor_real = max(ofertas)

    start = time.perf_counter()
    seleccionada = elegir_mejor_oferta(ofertas)
    end = time.perf_counter()

    print(f"Semilla utilizada: {semilla}")
    print(f"Cantidad de ofertas: {n}")
    print(f"Oferta seleccionada por el algoritmo: {seleccionada}")
    print(f"Mejor oferta real: {mejor_real}")
    print(f"¿El algoritmo eligió la mejor oferta? {'SÍ' if seleccionada == mejor_real else 'NO'}")
    print(f"Tiempo de ejecución: {end - start:.8f} segundos")
    return {
        "semilla": semilla,
        "seleccionada": seleccionada,
        "mejor_real": mejor_real,
        "correcto": seleccionada == mejor_real,
        "tiempo": end - start
    }

if __name__ == "__main__":
    if len(sys.argv) == 2:
        semilla = int(sys.argv[1])
        correr_experimento(semilla=semilla)
    else:
        correr_experimento()
