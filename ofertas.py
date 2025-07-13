import math 

def elegir_mejor_oferta(ofertas):
    n = len(ofertas)
    r = int(n / math.e)  
    mejor_hasta_ahora = max(ofertas[:r])

    for i in range(r, n):
        if ofertas[i] > mejor_hasta_ahora:
            return ofertas[i]   

    return ofertas[-1]
