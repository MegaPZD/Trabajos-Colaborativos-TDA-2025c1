def postas_hitratacion(mapa_carrera):

    mapa_carrera.sort(key=lambda ciudad: ciudad[1])

    postas_hitratacion = []
    max_distancia = 0
    
    for i in range(1, len(mapa_carrera)):
        distancia_actual = mapa_carrera[i][1] - mapa_carrera[i-1][1]
        if distancia_actual + max_distancia <= 7:
            max_distancia += distancia_actual
        elif distancia_actual > 7 and i != len(mapa_carrera) - 1:
            max_distancia = 0
        else:
            postas_hitratacion.append(mapa_carrera[i-1])
            max_distancia = 0  

    if max_distancia > 0:
        postas_hitratacion.append(mapa_carrera[-1])
             
    return postas_hitratacion