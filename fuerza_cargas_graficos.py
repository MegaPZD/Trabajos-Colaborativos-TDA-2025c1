import random
import time
import matplotlib.pyplot as plt


def calcular_fuerza_parcial(cargas, particula, inicio, fin):
    if inicio > fin:
        return 0
    if inicio == fin:
        return cargas[inicio] * cargas[particula] / (particula - inicio) ** 2
    medio = (inicio + fin) // 2
    return calcular_fuerza_parcial(cargas, particula, inicio, medio) + \
           calcular_fuerza_parcial(cargas, particula, medio + 1, fin)

def calcular_fuerza(cargas, particula):
    fuerza_izquierda = calcular_fuerza_parcial(cargas, particula, 0, particula - 1)
    fuerza_derecha = calcular_fuerza_parcial(cargas, particula, particula + 1, len(cargas) - 1)
    return fuerza_izquierda - fuerza_derecha

# Punto 5 
def generar_sets(tamaños, semilla=123):
    random.seed(semilla)
    sets = []
    for n in tamaños:
        sets.append([random.uniform(-10, 10) for _ in range(n)])
    return sets

# Punto 6 
def medir_tiempos(sets):
    tiempos = []
    resultados = []
    for cargas in sets:
        j = len(cargas) // 2  
        t1 = time.time()
        resultado = calcular_fuerza(cargas, j)
        t2 = time.time()
        tiempos.append(t2 - t1)
        resultados.append(resultado)
    return tiempos, resultados


tamaños = [10, 100, 500, 1000, 2000, 3000, 5000]
sets = generar_sets(tamaños)
tiempos, resultados = medir_tiempos(sets)


for i in range(len(tamaños)):
    print(f"Tamaño: {tamaños[i]}")
    print(f"Cargas: {sets[i]}")
    print(f"Índice evaluado: {len(sets[i]) // 2}")
    print(f"Fuerza total: {resultados[i]}")
    print(f"Tiempo de ejecución: {tiempos[i]:.6f} segundos")
    print("")

plt.figure(figsize=(10, 6))
plt.plot(tamaños, tiempos, marker='o')
plt.xlabel("Tamaño del set de cargas (n)")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.title("Tiempo de ejecución vs Tamaño del input")
plt.grid(True)
plt.tight_layout()
plt.show()
