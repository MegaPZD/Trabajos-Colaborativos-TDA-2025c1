def postas_hitratacion(mapa_carrera):

    mapa_carrera.sort(key=lambda ciudad: ciudad[1])
    postas_hitratacion = []
    ultima_posta = 0
    cantidad_postas = len(mapa_carrera)

    for i in range(1, cantidad_postas):
        distancia_actual = mapa_carrera[i][1] - mapa_carrera[ultima_posta][1]
        
        if distancia_actual > 7:
            postas_hitratacion.append(mapa_carrera[i - 1])
            ultima_posta = i - 1
    if ultima_posta != cantidad_postas - 1:
        postas_hitratacion.append(mapa_carrera[-1])
             
    return postas_hitratacion