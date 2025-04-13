def calcular_fuerza_parcial(cargas, particula, inicio, fin):
  if inicio > fin:
    return 0
  if inicio == fin:
    return cargas[inicio] * cargas[particula] / (particula - inicio)**2
  medio = (inicio + fin) // 2
  return calcular_fuerza_parcial(cargas, particula, inicio, medio) + calcular_fuerza_parcial(cargas, particula, medio + 1, fin)

def calcular_fuerza(cargas, particula):
  fuerza_izquierda = calcular_fuerza_parcial(cargas, particula, 0, particula - 1)
  fuerza_derecha = calcular_fuerza_parcial(cargas, particula, particula + 1, len(cargas) - 1) 
  return fuerza_izquierda - fuerza_derecha

q = [3,-4,2,5,1]
calcular_fuerza(q,2)
