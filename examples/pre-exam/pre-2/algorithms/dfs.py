def dfs(Adj, s, visited): 
	
  # Usually here you do something 	
  # with the current node 
  visited[s] = True
  for n in Adj[s]:
    if not visited[n]:
      dfs(Adj,n,visited)