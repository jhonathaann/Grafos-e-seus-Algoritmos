from collections import deque

# busca em profundidade
def DFS(G):
    cor = {}
    pi = {} # armazena o predecessor
    ordem_visita = []

    # pinta todos os vertices do grafo de branco. branco = não visitado
    for u in G.keys():
        cor[u] = 'branco'
        pi[u] = None # predecessor de cada vertice ainda é vazio, pois ninguem foi explorado ainda

    # para todo vertice u do grafo
    for u in G.keys():
        # se o vertice u ainda nao foi visitado
        if cor[u] == 'branco':
            DFS_visita(G, u, cor, pi, ordem_visita)
    
    return pi, ordem_visita

    

def DFS_visita(G, u, cor, pi, ordem_visita):
    cor[u] = 'cinza' # marca o vertice corrente como cinza
    ordem_visita.append(u) # add ele na ordem de visita

    # para cada vertice v adj ao vertice u
    for v in G[u]:
        # se o vertice v nao foi visitado
        if cor[v] == 'branco':
            pi[v] = u
            DFS_visita(G, v, cor, pi, ordem_visita) # visita o vertice v
    
    cor[u] = 'preto'


G = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B']
}

predecessores, vertices_visitados = DFS(G)

print(f'Ordem dos vertices visitados: {vertices_visitados}')