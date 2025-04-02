import random
from Problema1TP1 import postas_hitratacion

# carrera = [(Posta i+1, kilometro), ...] n aleatorio

def generar_carrera(n_postas):
    carrera = []
    kilometro = 0  # Comenzamos en el kilómetro 0

    for i in range(n_postas):
        incremento = random.randint(1, 7)  # Genera un número aleatorio entre 1 y 10
        kilometro += incremento  # Suma el incremento al total de kilómetros
        carrera.append((f"Posta {i + 1}", kilometro))  # Añade la tupla a la lista

    return carrera

n = random.randint(10, 50) # numero de postas

carrera = generar_carrera(n)
print(f"{n} Postas:\n{carrera}\nPostas Resultantes:\n{postas_hitratacion(carrera)}")
