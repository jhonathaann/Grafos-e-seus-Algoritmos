from collections import deque

# busca em largura
def BFS(G, s):
    cor = {}
    pi = {} # armazena o predecessor
    Q = deque()  # Q é uma fila. ela vai armazenar os vertices que foram visitados
    ordem_visita = []

    # para cada vertice do grafo, vou "pintar" ele de branco
    for u in G.keys():
        cor[u] = 'branco'
        pi[u] = None

    # começando pelo vertice s. "pinto" ele de cinza e o add na fila
    cor[s] = 'cinza'
    Q.append(s)  # add o vertice de inicio na fila
    ordem_visita.append(s)

    # enquanto houver vertices na fila
    while Q:
        u = Q.popleft() # pega o primeiro vertice da fila

        # para cada vertice adj ao vertice corrente u
        for v in G[u]:
            # se ele ainda não foi visitado
            if cor[v] == 'branco':
                cor[v] = 'cinza' # pinta esse vertices de cinza
                pi[v] = u  # amarzena que o predecessor do v é o u
                Q.append(v) # add o v na fila
                ordem_visita.append(v)  # add o v na ordem de visita

        cor[u] = 'preto' # marca o vertice u como visitado

    return pi, ordem_visita


grafo = {
    'A': ['B', 'C'],  # vertice A é vizinho do vertice B e C
    'B': ['A', 'D', 'E'], # vertice B é vizinho do vertice A, D, e E
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
    }

s = 'A'
print(grafo.keys())
predecessores, vertices_visitados = BFS(grafo, s)

print(f'Ordem dos vertices visitados: {vertices_visitados}')

