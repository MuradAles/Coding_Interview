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
    graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}
    #       A --------> B --------> D
    #       |           |
    #       \           \
    #       |           |
    #       v           v
    #       C--->F<-----E
    print("bfs", bfs("A", graph))
    print("dfs", dfs("A", graph))


main()
