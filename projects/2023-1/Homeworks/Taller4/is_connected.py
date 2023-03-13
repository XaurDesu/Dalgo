graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E'],
         'G': []}
	
def make_visited(Adj):
    ret = {}
    for v in Adj.keys():
        ret[v] = False
    return ret

def is_connected(Adj, s, j):
    visited = make_visited(Adj)
    queue = [s]
    while 0 < len(queue): 
        current_node = queue.pop(0)
        if not visited[current_node]:
            visited[current_node] = True
            for n in Adj[current_node]:
                if n == j:
                    return True
                if not visited[n]:
                    queue.append(n)
    return False

if __name__ == "__main__":
    print(is_connected(graph, 'A', 'B'))
    print(is_connected(graph, 'A', 'D'))
    print(is_connected(graph, 'A', 'G'))