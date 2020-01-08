from collections import defaultdict

class Graph(object):

    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def insertNode(self, value):
        self.nodes.add(value)

    def insertEdge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[from_node, to_node] = distance
        self.edges[to_node].append(from_node)
        self.distances[to_node, from_node] = distance
