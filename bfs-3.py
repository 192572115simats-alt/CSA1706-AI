from collections import deque

graph = {
    1: [2, 3],
    2: [5, 6],
    3: [7, 4],
    4: [3, 8],
    5: [2],
    6: [2],
    7: [3, 8],
    8: [7, 4]
}

def bfs(start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

bfs(1)
