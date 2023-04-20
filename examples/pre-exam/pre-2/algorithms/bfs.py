def bfs(Adj, s): 
 visited = [False for v in Adj] 
 queue = [s]
 while 0 < len(queue): 
   current_node = queue.pop(0)
   if not visited[current_node]:
    # Usually here you do something 
    # with the current node
    visited[current_node] = True
    for n in Adj[current_node]:
      if not visited[n]:
        queue.append(n)