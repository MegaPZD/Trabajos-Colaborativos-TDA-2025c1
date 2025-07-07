def subconjuntoFactible(A: list[int], B: int):
    A_ordenado = sorted(A, reverse=True)
    S = []
    suma = 0

    for a in A_ordenado:
        if suma + a <= B:
            S.append(a)
            suma += a

    return S



A = [4,5,9,7,80,100,12,10]
B = 16

print(subconjuntoFactible(A, B))