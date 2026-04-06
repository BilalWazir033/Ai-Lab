from collections import deque
graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':['F'],
    'F':[],
    'G':[]
}
def bfs(graph,start):
    visited=set()
    queue=deque([start])
    visited.add(start)
    while queue:
        node=queue.popleft()
        print(node,end=" ")
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
bfs(graph,'A')                                                                                                                                                                                                                                                                                                                                                                                                                                                          
