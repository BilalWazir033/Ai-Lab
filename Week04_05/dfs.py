graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

def dfs(graph, start):    
    visited = set()    
    stack = [start]    
        
    while stack:    
        node = stack.pop()    
        if node not in visited:    
            print(node, end=" ")    
            visited.add(node)    
            # Add neighbors in reverse order to maintain expected order    
            for neighbor in reversed(graph[node]):    
                if neighbor not in visited:    
                    stack.append(neighbor)    
     
print("\nDFS Traversal from A:")    
dfs(graph, 'A')  
