from time import time

def es_primo(n):
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    
    return True

def backtracking(n, par, opt):
    if len(opt) > 0 and len(par) >= len(opt):
        return
    
    if par[-1] == n:
        opt.clear()
        opt.extend(par)
        return
    
    for i in range((len(par) - 1) , -1, -1):
        for j in range(i, -1, -1):
            nuevo_valor = par[i] + par[j]

            if nuevo_valor > n or nuevo_valor <= par[-1]:
                continue

            par.append(nuevo_valor)
            backtracking(n, par, opt)
            par.pop()

            
def suma_encadenada_minima(n):
    if n == 1:
        return [1]
    
    n_aux = n
    while n_aux % 2 == 0 and n_aux > 2:
        n_aux //= 2
    
    t1 = time()
    sol = []

# Esto todavia hay que checkear si es cierto
    if es_primo(n_aux):
        sol = suma_encadenada_minima(n_aux - 1)
        sol.append(n_aux)
    else:
        backtracking(n_aux, [1,2], sol)

    while sol[-1] < n:
        sol.append(sol[-1] + sol[-1])
    
    t2 = time()
    print(f"Execution time: {t2 - t1} seconds")
    
    return sol

print(suma_encadenada_minima(188))