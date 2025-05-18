import networkx as nx
import string

def antenas_mediante_flujo(antenas : int, matriz_distancias, k, b, D):


    # grafo dirigido
    grafo = nx.DiGraph()

    for i in range(antenas):
        antena_inicio = f"inicio_antena{i+1}"
        grafo.add_edge('Origen', antena_inicio, capacity=k)

    for j in range(antenas):
        antena_destino = f"destino_antena{j+1}"
        grafo.add_edge(antena_destino, "Sumidero", capacity=b)

    # matriz cuadrada antenas * antenas
    for i in range(antenas):
        antena_inicio = f"inicio_antena{i+1}"
        conexiones_validas = 0
        for j in range(antenas):
            if i == j:
                continue
            if matriz_distancias[i][j] < D:
                antena_destino = f"destino_antena{j+1}"
                grafo.add_edge(antena_inicio, antena_destino, capacity=1)
                conexiones_validas += 1
        
        if conexiones_validas < k:
            print(f"Antena {i+1} no puede conectarse a {k} backups válidos.")
            return dict()

    flujo_maximo, resultado = nx.maximum_flow(grafo, 'Origen', 'Sumidero', flow_func=nx.algorithms.flow.edmonds_karp)

    print(f"El flujo maximo es: {flujo_maximo}")

    if(flujo_maximo < (antenas * k)):
        print(f"El flujo maximo {flujo_maximo} no es suficiente para abastecer n*k {antenas*k}\nSignificando que hay 1 o mas antenas que aparecen mas de b veces en los k backups")
        return dict()
    

    diccionario_resultante = dict()
    for u in resultado:
        if not u.startswith("inicio_"):
            continue
        clave = u.removeprefix("inicio_")
        vecinos = resultado[u]
        usados = {
            v.removeprefix("destino_") for v, flujo in vecinos.items() if flujo == 1
        }
        diccionario_resultante[clave] = usados

    #print(flujo_maximo)
    return diccionario_resultante

"""resultado  = antenas_mediante_flujo(5, [ 
    [0, 3, 4, 4, 3],
    [3, 0, 3, 3, 7],
    [4, 3, 0, 4, 3],
    [4, 3, 4, 0, 3],
    [3, 7, 3, 3, 0]
], 2, 2, 4)"""

"""resultado  = antenas_mediante_flujo(10, [
    [0, 3, 4, 4, 8,8,10,8,15,8],
    [3, 0, 3, 3, 7,7,9,7,14,5],
    [4, 3, 0, 4, 4, 8,6,4,11,4],
    [4, 3, 4, 0, 4, 4, 8, 8, 11, 8],
    [8, 7, 4, 4, 0, 4, 4, 8, 7, 8],
    [8,7,8,4,4,0,8,12,9,12],
    [10,9,6,6,4,8,0,4,5,6],
    [8,7,4,8,8,12,4,0,7,4],
    [15,14,11,11,7,9,5,7,0,11],
    [8,5,4,8,8,12,6,4,1,0]
], 3, 3, 9)"""

#for clave, valor in resultado.items():
#    print(f"{clave}: {valor}")