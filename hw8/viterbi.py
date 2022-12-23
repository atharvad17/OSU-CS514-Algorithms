from collections import defaultdict

def longest(n, edges):
    graph = [[] for _ in range(n)]
    in_degree = [0 for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    start_nodes = []
    for i, d in enumerate(in_degree):
        if d == 0:
            start_nodes.append(i)

    longestPath = []

    def pathSolve(node, path):
        if len(graph[node]) == 0:
            nonlocal longestPath
            if len(path) > len(longestPath):
                longestPath = list(path)

        for next_node in graph[node]:
            path.append(next_node)
            pathSolve(next_node, path)
            path.pop()

    for node in start_nodes:
        pathSolve(node, [node])

    return (len(longestPath) - 1, longestPath)
