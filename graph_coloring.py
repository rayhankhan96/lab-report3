def is_safe(node, graph, color, c):
    for neighbor in graph[node]:
        if color[neighbor] == c:
            return False
    return True

def solve(node, graph, color, k, n):
    if node == n:
        return True
    for c in range(1, k + 1):
        if is_safe(node, graph, color, c):
            color[node] = c
            if solve(node + 1, graph, color, k, n):
                return True
            color[node] = 0
    return False

def graph_coloring(filename):
    with open(filename, 'r') as f:
        data = list(map(int, f.read().split()))
    n, m, k = data[0], data[1], data[2]
    graph = [[] for _ in range(n)]
    index = 3
    for _ in range(m):
        u = data[index]
        v = data[index + 1]
        graph[u].append(v)
        graph[v].append(u)
        index += 2
    color = [0] * n
    if solve(0, graph, color, k, n):
        print(f"Coloring Possible with {k} Colors")
        print("Color Assignment:", color)
    else:
        print(f"Coloring Not Possible with {k} Colors")

graph_coloring("input.txt")