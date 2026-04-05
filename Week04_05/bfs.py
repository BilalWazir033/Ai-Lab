from collections import deque

graph = {
    'A': ['B','C'],   # A connects to B and C
    'B': ['D','E'],   # B connects to D and E
    'C': ['F'],       # C connects to F
    'D': [],          # D has no neighbors
    'E': ['F'],       # E connects to F
    'F': []           # F has no neighbors
}

def bfs(graph, start):

    visited = set()           
    queue = deque([start])
    visited.add(start)

    while queue:

        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:

            if neighbor not in visited:

                visited.add(neighbor)
                queue.append(neighbor)

bfs(graph, 'A')
