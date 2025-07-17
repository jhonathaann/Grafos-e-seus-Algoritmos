import heapq

# funcao recebe o grafo G, os pesos associados as areas e um vertice de origem s
def dijkstra(G, pesos, s):
    # iniciando as dist associadas a cada vertice ao vertice de origem (s) como infinito
    d = {}
    pi = {}
    for u in G.keys():
        d[u] = float('infinity')
        pi[u] = None
    
    # a distancia de s para o vertice de origem (s) é 0
    d[s] = 0

    '''como a fila de prioridade (min-heap) Q funciona: cada elemento é uma
    tupla (distancia, vertice). o heap é ordenando pelo primeiro elemento da tupla
    (distancia)'''
    Q = [(0, s)]
    heapq.heapify(Q) # transformando a lista Q em um heap

    S = set() # conjunto ({}) que ira armazenar os vertices cujas distancias ja foram encontradas

    # enquanto o heap nao estiver vazio
    while Q:
        # extraindo o vertice com a menor dist, e a dist associado a ele
        current_dist, u = heapq.heappop(Q)

        # se esse vertice ja foi processado, va para o proximo
        if u in S:
            continue

        # add u ao conjunto de vertices processados
        S.add(u)

        # para cada vertice v vizinho ao vertice u
        for v in G[u]:
            # se v ainda nao foi processado
            if v not in S:
                # obtem o peso da aresta de liga u com v (verifica ambas as direcoes)
                if (u,v) in pesos:
                    peso = pesos[(u,v)]
                else:
                    peso = pesos[(v,u)]

                # calcula a nova estimativa de distancia para v somando a dist de v com u
                new_dist = d[u] + peso


            # relaxando as arestas
            # a nova dist para v for menor, atualize ela
            if new_dist < d[v]:
                d[v] = new_dist
                pi[v] = u # predecessor do v é o u
                heapq.heappush(Q, (new_dist, v)) # add a nova distancia associada ao vertice v

    return d, pi

# grafo G
G = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# pesos associados as arestas
pesos = {
    ('A', 'B'): 4,
    ('A', 'C'): 2,
    ('B', 'D'): 5,
    ('B', 'E'): 3,
    ('C', 'F'): 4,
    ('E', 'F'): 1
}

s = 'A'  # vertice de origem
distancias, predecessores = dijkstra(G, pesos, s)
    
print("Distâncias mínimas a partir de", s)
for vertice, distancia in distancias.items():
    print(f"{vertice}: {distancia}")
    