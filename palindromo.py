def reconstruir_solucion(cadena, es_palindromo, opt):
    n = len(cadena)
    resultado = []
    
    partes = opt[-1]
    j = n
    while partes > 0:
        for i in range(j - 1, -1, -1):
            if es_palindromo[i][j - 1] and opt[i] == partes - 1:
                resultado.append(cadena[i:j])
                partes -= 1
                j = i
                break

    return resultado[::-1]

def palindromo(cadena):

    n = len(cadena)
    es_palindromo = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(i,n):
            if cadena[i:j+1] == cadena[i:j+1][::-1]:
                es_palindromo[i][j] = True

    opt = [0] * (n + 1)

    for l in range(1, n + 1):
        min_cortes = l

        for i in range(l - 1):
            if es_palindromo[i][l - 1]:
                min_cortes = min(min_cortes, opt[i] + 1)

        opt[l] = min(min_cortes, opt[l - 1] + 1)

    return reconstruir_solucion(cadena, es_palindromo, opt)