import time
import random

tiempos = [[0,0,0,0,0] for _ in range(0,5)]
promedios = []
valores_n = [100, 200, 300, 400, 500]

def generar_carrera(n_postas):
    carrera = []
    kilometro = 0  # Comenzamos en el kilómetro 0

    for i in range(n_postas):
        incremento = random.randint(1, 7)  # Genera un número aleatorio entre 1 y 10
        kilometro += incremento  # Suma el incremento al total de kilómetros
        carrera.append((f"Posta {i + 1}", kilometro))  # Añade la tupla a la lista

    return carrera

def postas_hitratacion(mapa_carrera):

    mapa_carrera.sort(key=lambda postas: postas[1])
    postas_hitratacion = []
    ultima_posta = 0
    cantidad_postas = len(mapa_carrera)

    for i in range(1, cantidad_postas):
        distancia_actual = mapa_carrera[i][1] - mapa_carrera[ultima_posta][1]
        
        if distancia_actual > 7:
            if ultima_posta == 0 and mapa_carrera[i - 1][1] > 7:
                postas_hitratacion.append(mapa_carrera[ultima_posta])
            postas_hitratacion.append(mapa_carrera[i - 1])
            ultima_posta = i - 1
    if mapa_carrera[cantidad_postas - 1][1] - mapa_carrera[ultima_posta][1] > 7:
        postas_hitratacion.append(mapa_carrera[-1])
             
    return postas_hitratacion

i = 0
for valor in valores_n:

    for j in range(0,5):
        carrera = generar_carrera(valor)
        t1 = time.time()
        resultado = (postas_hitratacion(carrera))
        print(resultado)
        t2 = time.time()
        tiempos[i][j]= t2 - t1
    promedios.append((sum(tiempos[i]))/5)
    i += 1

for i in range(0,5):
    print(f"tiempos de los valores {i+1}:")
    print(tiempos[i])
    print(f"promedio de los valores {i+1}:")
    print(promedios[i])
