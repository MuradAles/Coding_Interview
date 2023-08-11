class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def getVertices(self):
        return list(self.graph_dict.keys())

    def addVertex(self, vrtx):
        if vrtx not in self.graph_dict:
            self.graph_dict[vrtx] = []

    def getEdges(self):
        if not self.graph_dict:
            return []
        all_edges = []
        for vertex in self.graph_dict:
            for nextvertex in self.graph_dict[vertex]:
                if {nextvertex, vertex} not in all_edges:
                    all_edges.append({vertex, nextvertex})
        return all_edges

    def AddEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.graph_dict:
            self.graph_dict[vrtx1].append(vrtx2)
        else:
            self.graph_dict[vrtx1] = [vrtx2]


def main():
    graph_elements = {
        "a": ["b", "c"],
        "b": ["a", "d"],
        "c": ["a", "d"],
        "d": ["e"],
        "e": ["d"],
    }
    g = Graph(graph_elements)
    g.addVertex("f")
    print(g.getVertices())
    print(g.getEdges())


main()
