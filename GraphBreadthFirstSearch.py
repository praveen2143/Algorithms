def bfs(graph, start):
    visited = set()
    q = []
    q.append(start)
    visited.add(start)
    while len(q) > 0:
        curnode = q.pop(0)
        print(curnode, end=" ")
        for node in graph[curnode]:
            if node not in visited:
                q.append(node)
                visited.add(node)


if __name__ == '__main__':
    g = {
        "0": ["1", "3"],
        "1": ["0", "3"],
        "2": ["0", "1", "3"],
        "3": ["0", "2"]
    }
    bfs(g, "0")
