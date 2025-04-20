import random
from suma_encadenada import suma_encadenada_minima

n = random.randint(500, 1500)
solucion = suma_encadenada_minima(n)

print(f"Número n:{n}\nSolución:\n{solucion}\n")