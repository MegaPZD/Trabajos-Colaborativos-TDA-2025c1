from palindromo import palindromo

def prueba_palindromos(set_path):
    with open(set_path, 'r') as f:
        for linea in f:
            partes = linea.strip().split()

            if len(partes) != 2:
                continue

            palabra, solucion_esperada = partes
            resultado = palindromo(palabra)
            if len(resultado) == int(solucion_esperada):
                print(f"{palabra}: OK ({resultado})")
            else:
                print(f"{palabra}: ERROR (esperado {solucion_esperada}, obtenido {resultado})")

prueba_palindromos('set_palindromos.txt')