class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def getVertices(self):
        print("Vertices", list(self.graph_dict.keys()))
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
        print("Edges", all_edges)
        return all_edges

    def AddEdge(self, edge_1, edge_2):
        if edge_1 in self.graph_dict:
            self.graph_dict[edge_1].append(edge_2)
        else:
            self.graph_dict[edge_1] = [edge_2]

    def bfs_check(self, vertex_1, vertex_2):
        pass

    def dfs_check(self, vertex_1, vertex_2):
        pass

    def check_Route_Between_Nodes(self, vertex_1, vertex_2) -> bool:
        # first we can check if vertices exists in graph
        if vertex_1 not in self.graph_dict or vertex_2 not in self.graph_dict:
            return False
        # now we can use dfs or bfs to check if path exists
        # dfs
        visited = list()
        dfs_check(self, vertex_1, vertex_2, visited)
        return True


def main():
    # populate graph
    graph_elements = {
        "a": ["b"],
        "b": ["c", "d"],
        "c": ["a", "f"],
        "d": ["e"],
        "e": ["c", "d"],
        "f": ["g", "e"],
        "g": ["e"],
    }
    g = Graph(graph_elements)
    print(g.getVertices())
    print(g.getEdges())
    print(g.check_Route_Between_Nodes("a", "e"))


main()
