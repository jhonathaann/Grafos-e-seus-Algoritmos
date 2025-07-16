'''Dado um Grafo G, verificar se ele é conexo.

Um grafo G é conexo se, para quaisquer pares de vértices u e v que
você pegar, existe pelo menos um caminho que liga esses vértices

Ideia de solução: utilar a busca em largura (BFS) e, caso a lista de
vertices visitados for menos do que a lista de vertices, existe 
pelo menos um vértice que não foi visitado. Não importa quel vértice 
de origem você passa para a função, se ele não for conexo, sempre vai haver
pelo menos um vértice que não vai ser visitado quando você aplica a busca

'''

from collections import deque

# busca em largura
def conexo(G):

    # Grafo vazio é coniderado Conexo
    if len(G) == 0:
        return True
    
    s = next(iter(G)) # pega a primeira chave. não precisa saber de ante mão como esta organizado esse dicionário
    cor = {}
   # pi = {} # armazena o predecessor
    Q = deque()  # Q é uma fila. ela vai armazenar os vertices que foram visitados
    ordem_visita = []

    # para cada vertice do grafo, vou "pintar" ele de branco
    for u in G.keys():
        cor[u] = 'branco'
        #pi[u] = None

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
                #pi[v] = u  # amarzena que o predecessor do v é o u
                Q.append(v) # add o v na fila
                ordem_visita.append(v)  # add o v na ordem de visita

        cor[u] = 'preto' # marca o vertice u como visitado


    if len(ordem_visita) < len(G):
        return False
    
    return True


grafo_conexo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

grafo_nao_conexo = {
    'A': ['B'],
    'B': ['A'],
    'C': ['D'],
    'D': ['C']
}

print("Grafo conexo é conexo?", conexo(grafo_conexo))  # True
print("Grafo não conexo é conexo?", conexo(grafo_nao_conexo))  # False