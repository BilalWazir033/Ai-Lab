from collections import deque
graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}
def bfs(graph,start):
    visited=set()
    queue=deque([start])
    visited.add(start)
    while queue:
        node=queue.popleft()
        print(node,end=" ")
        for neighber in graph[node]:
            if neighber not in visited:
                visited.add(neighber)
                queue.append(neighber)
bfs(graph,'A')