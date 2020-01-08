from Graph import Graph
from heapq import heappop, heappush
#import time

def printEdges(path):
    for k, v in path.items():
      print('Arresta:', k, '--->', v)


def dijkstra(graph, initial_node):
    visited = {initial_node: 0}
    path = {}
    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node
    return path


def dijkstraWithHeap(graph, initial_node):
    visited = {initial_node: 0}
    path = {}
    nodes = set(graph.nodes)
    heap = [(0, initial_node)]

    while nodes and heap:
        current_weight, min_node = heappop(heap)
        try:
            while min_node not in nodes:
                current_weight, min_node = heappop(heap)
        except IndexError:
            break

        nodes.remove(min_node)

        for v in graph.edges[min_node]:
            weight = current_weight + graph.distances[min_node, v]
            if v not in visited or weight < visited[v]:
                visited[v] = weight
                heappush(heap, (weight, v))
                path[v] = min_node

    return path


if __name__ == '__main__':

    myGraph = Graph()

    with open('grafos/1') as file:
        for line in file:
            lst = line.split(',')
            vertexFrom = int(lst[0])
            vertexTo = int(lst[1])
            myGraph.insertNode(vertexTo)
            myGraph.insertNode(vertexFrom)
            weightEdge = float(lst[2])
            myGraph.insertEdge(vertexFrom, vertexTo, weightEdge)


    # Testes de Tempo

    #lista = []
    #for i in range(30):
        #print(i)
        #inicio = time.time()
        #result = dijkstra(myGraph, 0)
        #fim = time.time()
        #lista.append(fim-inicio)
        # para printar as arrestar do dijkstra: (printEdges(dijkstra(myGraph, 0)))
    #tempo_medio_sem_heap = sum(lista) / 30
    #print('Tempo: %f' % tempo_medio_sem_heap)

    #lista = []
    #for i in range(30):
        #inicio = time.time()
        #result = dijkstraWithHeap(myGraph, 0)
        #fim = time.time()
        #lista.append(fim - inicio)
        # para printar as arrestar do dijkstra com Heap:
        # print(printEdges(dijkstraWithHeap(myGraph, 0)))
    #tempo_medio_heap = sum(lista) / 30
    #print('Tempo: %f' % tempo_medio_heap)
