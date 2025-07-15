'''Dado um Grafo G, o objetivo é contar quantas componentes
esse grafo possui.

Ideia: aplica a busca em largura (BFS) no gravo e, quando a função
retornar os vértices visitados, voce aplica uma subtração de conjunto
nos vértices do Grafo G com os vértices visitados, obtendo assim um novo 
conjunto de vértices. Passe esse novo conjunto de vértices para a função
de busca. repita o processo enquanto essa subtração não der o conjunto 
vazio. A quantidade de vezes que a função BFS for chamada representa o 
numero de componetes que o grafo possui

'''

from collections import deque

def BFS(G, s):
    cor = {}
    Q = deque()  
    ordem_visita = set()  # ordem_visita agora é um conjunto, e não uma lista

    for u in G.keys():
        cor[u] = 'branco'

    cor[s] = 'cinza'
    Q.append(s)
    ordem_visita.add(s)

    while Q:
        u = Q.popleft()

        for v in G[u]:
            if cor[v] == 'branco':
                cor[v] = 'cinza' 
                Q.append(v) 
                ordem_visita.add(v)

        cor[u] = 'preto'

    return ordem_visita

def contar_componentes(G):
    # se o grafo for vazio, ele tem apenas uma componente
    if len(G) == 0:
        return 0
    
    nao_visitados = set(G.keys()) # transformando a lista ([]) de vertices do grafo em um conjunto ({})
    componentes = 0

    # enquanto a lista de nao visitados nao estiver vazia
    while nao_visitados:
        v = nao_visitados.pop() # pegando o primeiro vertice da lista

        visitados = BFS(G,v)

        # realizando a subtração de conjunto
        nao_visitados -= visitados

        componentes += 1

    return componentes


# Exemplo de uso:
grafo_nao_conexo = {
    'A': ['B'],
    'B': ['A'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['E'],
    'G': []
}

print(contar_componentes(grafo_nao_conexo))  # Deve retornar 4