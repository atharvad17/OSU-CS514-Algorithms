from collections import defaultdict

def order(n, edges):

    def visit(v):
        if v in visited:
            return
        visited.add(v)
        for u in prereqs[v]:
            visit(u)
        output.append(v)

    graph = defaultdict(list)
    prereqs = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        prereqs[v].append(u)

    nodes = range(n)
    visited = set()
    output = []
    for v in nodes:
        visit(v)
    return output