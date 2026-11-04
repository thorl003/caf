
# Maximum Flow using Ford-Fulkerson Algorithm
# Fixed Input

from collections import deque

def bfs(graph, source, sink, parent):
    n = len(graph)

    visited = [False] * n
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()

        for v in range(n):
            if not visited[v] and graph[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u

                if v == sink:
                    return True

    return False


def max_flow(graph, source, sink):
    n = len(graph)
    parent = [-1] * n
    flow = 0

    while bfs(graph, source, sink, parent):

        path_flow = float('inf')
        v = sink

        while v != source:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v])
            v = u

        v = sink

        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u

        flow += path_flow

    return flow


# Fixed Input Graph (Capacity Matrix)
graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]

source = 0
sink = 5

result = max_flow(graph, source, sink)

print("Maximum Flow:", result)
