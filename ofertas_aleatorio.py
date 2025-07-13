import random
import math
import time
import matplotlib.pyplot as plt

def elegir_mejor_oferta(ofertas):
    n = len(ofertas)
    r = int(n / math.e)
    mejor_hasta_ahora = max(ofertas[:r])

    for i in range(r, n):
        if ofertas[i] > mejor_hasta_ahora:
            return ofertas[i]

    return ofertas[-1]  # si no encontró mejor

def medir_tiempos():
    tiempos = []
    sizes = list(range(100, 10000, 500))
    
    for n in sizes:
        data = list(range(1, n + 1))
        random.shuffle(data)
        
        inicio = time.perf_counter()
        elegir_mejor_oferta(data)
        fin = time.perf_counter()

        tiempos.append(fin - inicio)

    return sizes, tiempos

def graficar(sizes, tiempos):
    plt.plot(sizes, tiempos)
    plt.xlabel("Cantidad de ofertas")
    plt.ylabel("Tiempo (s)")
    plt.title("Tiempo de ejecución vs tamaño de input")
    plt.show()

if __name__ == "__main__":
    random.seed(42)
    sizes, tiempos = medir_tiempos()
    graficar(sizes, tiempos)
