import random
from fuerza_cargas import fuerza_cargas

def generar_particulas(n):
    particulas = []

    for i in range(n):
        paricula = random.randint(-500, 1500)
        particulas.append(paricula)

    return particulas

n = random.randint(50, 200)
particula_particular = random.randint(0, n)
particulas = generar_particulas(n)

print(f"Particula: {particula_particular}\nSolucion: {fuerza_cargas(particulas, particula_particular)}\n")