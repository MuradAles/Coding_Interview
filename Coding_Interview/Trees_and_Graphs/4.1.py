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

    def check_Route_Between_Nodes_bfs(self, vertex_1, vertex_2) -> bool:
        # first we can check if vertices exists in graph
        if vertex_1 not in self.graph_dict or vertex_2 not in self.graph_dict:
            return False
        # now we can use bfs to check if path exists
        # bfs
        bfs_list = bfs(vertex_1, self.graph_dict)
        if vertex_2 in bfs_list:
            return True
        return False

    def check_Route_Between_Nodes_dfs(self, vertex_1, vertex_2) -> bool:
        # first we can check if vertices exists in graph
        if vertex_1 not in self.graph_dict or vertex_2 not in self.graph_dict:
            return False
        # now we can use dfs to check if path exists
        dfs_list = bfs(vertex_1, self.graph_dict)
        if vertex_2 in dfs_list:
            return True
        return False


def bfs(vertex, graph, visited=None, queue=None):
    if visited is None:
        visited = list()
    if queue is None:
        queue = list()
    visited.append(vertex)
    queue.append(vertex)

    while queue:
        s = queue.pop(0)
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return visited


def dfs(vertex, graph, visited=None):
    if visited is None:
        visited = list()
    if vertex not in visited:
        visited.append(vertex)
        for neighbour in graph[vertex]:
            dfs(neighbour, graph, visited)
    return visited


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
        "z": ["g"],
    }
    g = Graph(graph_elements)
    g.getVertices()
    g.getEdges()
    print("bfs check")
    print(g.check_Route_Between_Nodes_bfs("a", "g"))
    print(g.check_Route_Between_Nodes_bfs("a", "z"))
    print("dfs check")
    print(g.check_Route_Between_Nodes_dfs("a", "g"))
    print(g.check_Route_Between_Nodes_dfs("a", "z"))


main()
