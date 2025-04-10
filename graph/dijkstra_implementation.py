import heapq


def dijkstra(graph, start):
    """Algoritmo de Dijkstra
    Calcula os caminhos mais curtos para se chegar a um vértice A, partindo de qualquer vértice de um grafo.

    Funciona da seguinte forma:
    1. Visita apenas uma vez cada um dos vértices do grafo;
    2. Calcula a distância que os vizinhos de um vértice X precisam percorrer para chegar ao vértice A;
    3. Verifica se a distância entre um vértice Y e A, passando pelo atual vértice X, é menor que outra distância calculada entre Y e A;
    4. Se sim, substitui a distância entre Y e A pela nova distância calculada passando pelo vértice X, e considera o caminho oficial de Y para A como sendo através de X.
    """
    min_heap = [(0, start)]  # dá o primeiro comando à heap, para inicializar em A, com distância 0
    distances = {node: float("inf") for node in graph}  # inicializa todas as distâncias com valor infinito
    distances[start] = 0  # A até A é zero

    while min_heap:  # itera enquanto houverem comandos na heap
        current_distance, current_node = heapq.heappop(min_heap)  # pega o comando de menor distância da heap

        # se um comando a ser executado for de distância maior que um já encontrado, ignora
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():  # itera sobre os vizinhos de um nó do grafo
            distance = current_distance + weight  # calcula a distância do nó neighbor até o nó A
            if distance < distances[neighbor]:
                # se a nova distância é menor do que uma anteriormente calculada, atualiza na resposta
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))  # adiciona um novo comando à heap

    return distances


graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1},
}

start_node = "A"
distances = dijkstra(graph, start_node)
print(f"Distances from {start_node}: {distances}")
