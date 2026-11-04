
# Graph Coloring using Backtracking
# Fixed Input

def is_safe(graph, color, vertex, c, n):
    for i in range(n):
        if graph[vertex][i] == 1 and color[i] == c:
            return False
    return True


def graph_coloring(graph, m, color, vertex, n):

    # All vertices are colored
    if vertex == n:
        return True

    # Try different colors
    for c in range(1, m + 1):

        if is_safe(graph, color, vertex, c, n):

            color[vertex] = c

            if graph_coloring(graph, m, color, vertex + 1, n):
                return True

            # Backtracking
            color[vertex] = 0

    return False


# Fixed graph (Adjacency Matrix)
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

n = 4
m = 3

color = [0] * n

if graph_coloring(graph, m, color, 0, n):
    print("Graph Coloring is possible")
    for i in range(n):
        print("Vertex", i + 1, ":", "Color", color[i])
else:
    print("Graph Coloring is not possible")
