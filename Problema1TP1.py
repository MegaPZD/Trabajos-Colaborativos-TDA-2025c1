def postas_hitratacion(mapa_carrera):

    mapa_carrera.sort(key=lambda posta: posta[1])
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