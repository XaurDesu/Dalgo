#Flood Fill: Solución que fuerza al input a ser una lista de adyacencia.
class Solution:
    def make_visited(self, l_adj):
        ret = {}
        for v in l_adj.keys():
            ret[v] = False
        return ret

    def create_l_adj(self, image, prev_color):
        l_adj = {}

        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == prev_color:
                    l_adj[(i, j)] = [
                            (i+1, j),
                    (i, j-1),       (i,j+1),
                            (i-1, j)
                    ]
        return l_adj
    
    def bfs(self, image, l_adj, sr, sc, color, prev_color):
        visited = self.make_visited(l_adj)
        queue = [(sr, sc)]
        while 0 < len(queue):
            current_node = queue.pop(0)
            if current_node[0] >= len(image) and current_node[1] >= len(image[0]):
                visited[current_node] = True
            if not visited[current_node]:
                visited[current_node] = True
                image[current_node[0]][current_node[1]] = color
                for n in l_adj[current_node]:
                    if n in visited and not visited[n]:
                        queue.append(n)
        return image

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        prev_color = image[sr][sc]
        l_adj = self.create_l_adj(image, prev_color)
        image = self.bfs(image, l_adj, sr, sc, color, prev_color)
        return image