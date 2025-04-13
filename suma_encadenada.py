from time import time

def calcular_posibles_pasos(n, ult_elem):
    pasos = 0
    i = ult_elem
    while i < n:
        pasos += 1
        i += i
    return pasos

def backtracking(n, par, opt):
    if len(opt) > 0 and calcular_posibles_pasos(n, par[-1]) + len(par) >= len(opt):
        return

    if len(opt) > 0 and len(par) >= len(opt):
        return
    
    if par[-1] == n:
        opt.clear()
        opt.extend(par)
        return
    
    nums_utilizados = set()
    
    for i in range((len(par) - 1) , -1, -1):
        if par[i] + par[i] <= par[-1]:
            continue

        for j in range(i, -1, -1):
            nuevo_valor = par[i] + par[j]
 
            if nuevo_valor > n or nuevo_valor <= par[-1] or nuevo_valor in nums_utilizados:
                continue

            par.append(nuevo_valor)
            backtracking(n, par, opt)
            par.pop()

            nums_utilizados.add(nuevo_valor)

            
def suma_encadenada_minima(n):
    if n == 1:
        return [1]
    
    t1 = time()
    sol = []
    n_aux = n
    
    while n_aux % 2 == 0 and n_aux > 2:
        n_aux //= 2
    
    if n_aux >= 100 and n_aux % 2 > 0:
        sol = suma_encadenada_minima(n_aux - 1)
        sol.append(n_aux)
        print("Aproximacion de la solucion: ", sol)

    print("Buscando una solucion:")
    backtracking(n_aux, [1, 2], sol)

    while sol[-1] < n:
        sol.append(sol[-1] + sol[-1])
    print("Solucion encontrada: ", sol, " para n = ", n)
            
    t2 = time()
    print(f"Execution time: {t2 - t1} seconds")
    
    return sol

print(suma_encadenada_minima(20000))