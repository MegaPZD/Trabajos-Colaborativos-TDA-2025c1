import networkx as nx

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

    return diccionario_resultante
