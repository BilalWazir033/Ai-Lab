graph={
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
def dfs(graph,start):
    visited=set()
    stack=[start]
    while stack:
        node=stack.pop()
        if node not in visited:
            print(node,end=" ")
            visited.add(node)
            for neighber in reversed(graph[node]):
                if neighber not in visited:
                    stack.append(neighber)
dfs(graph,'A')