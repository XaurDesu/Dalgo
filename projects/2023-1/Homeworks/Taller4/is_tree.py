graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E'],
         'G': []}

graph2 = {'A': ['B', 'C'],
         'B': [],
         'C': [],}

graph3 = {'A': ['B', 'C'],
         'B': [],
         'C': [],
         'D':[]}

def make_visited(Adj):
    ret = {}
    for v in Adj.keys():
        ret[v] = False
    return ret

def dfs_algo(s, visited, AdjList):
    if visited[s] == True:
        return False
    visited[s] = True	
    for n in AdjList[s]:
        if not visited[n]:
            if dfs_algo(n, visited, AdjList) == False:
                return False
            continue
        else:
            return False
    return True

def DFS_isTree(AdjList:dict) -> bool:
    """
    Escriba un algoritmos basados en DFS tal que dado un grafo retorne 
    True si el grafo es un arbol, en otro caso False.
    """
    visited = make_visited(AdjList)
    has_cycle = dfs_algo(next(iter(AdjList)),visited, AdjList)
    if False not in set(visited.values()) and has_cycle:
        return True
    else:
        return False

if __name__ == "__main__":
    print(DFS_isTree(graph))
    print(DFS_isTree(graph2))
    print(DFS_isTree(graph3))