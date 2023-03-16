from ast import List
import math
class solution:
    # Salvo el ultimo metodo AdjList es un diccionario con la siguiente estructura
    # {1:[2,3,4], 2:[1], 3:[1,4], 4:[3,1]}
    # Todos los grafos son grafos no dirigidos!
    # Los nombres de los nodos son numeros naturales!
    def BFS_connect(self, Adj: dict, s: int, j: int) -> bool:
        visited = self.make_visited(Adj)
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

    def get_that_list(self,parent, Node2):
        ret = []
        var = Node2
        while var != None:
            ret.append(var)
            var = parent[var]
        ret = ret[::-1]
        return ret

    def BFS_shortest_path(self, AdjList: dict, Node1: int, Node2: int) -> List[int]:
        """
        Dados dos nodos del grafo, retorne el camino de menor longitud.
        El camino de menor longitud debe ser un lista de los nodos por los cuales
        se debe pasar para llegar del Nodo1 al Nodo2, incluyéndolos. Si los nodos
        no están conectados se debe devolver una lista vacía.  
        """ 
        visited = self.make_visited(AdjList)
        parent = {}
        for v in AdjList.keys():
            parent[v] = None
        
        previous_node = None
        queue = [Node1]
        while 0 < len(queue):
            previous_node = current_node
            current_node = queue.pop(0)
            if not visited[current_node]:
                parent[current_node] = previous_node
                if current_node == Node2:
                    return self.get_that_list(parent, Node2)
                visited[current_node] = True
                
                for n in AdjList[current_node]:
                    if not visited[n]:
                        queue.append(n)
        return []


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
    
    def bfs_flood_fill(self, image, l_adj, sr, sc, color, prev_color):
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
        image = self.bfs_flood_fill(image, l_adj, sr, sc, color, prev_color)
        return image
    

    def dfs_algo(self, s, visited, AdjList):
        if visited[s] == True:
            return False
        visited[s] = True	
        for n in AdjList[s]:
            if not visited[n]:
                if self.dfs_algo(n, visited, AdjList) == False:
                    return False
                continue
            else:
                return False
        return True

    def DFS_isTree(self, AdjList:dict) -> bool:
        """
        Escriba un algoritmos basados en DFS tal que dado un grafo retorne 
        True si el grafo es un arbol, en otro caso False.
        """
        visited = self.make_visited(AdjList)
        has_cycle = self.dfs_algo(next(iter(AdjList)),visited, AdjList)
        if False not in set(visited.values()) and has_cycle:
            return True
        else:
            return False

    def Diskjstra_shortest_path(AdjListWeigted, Node1:int, Node2:int) -> List[int]:
        """
        Escriba un algoritmo que implemente el algoritmo de Dikjstra para calcular
        el camino de MENOR costo entre dos nodos del grafo. El camino de debe ser 
        un lista de los nodos por los cuales se debe pasar para llegar del 
        Nodo1 al Nodo2, incluyéndolos. Si los nodos no están conectados 
        se debe devolver una lista vacía.
        

        Args:
            AdjListWeigted (?): En este caso son libres de escoger la implementación que deseen
            en cualquier caso incluyan comentarios que permitan hacer pruebas del metodo.
            
        -- IMPLEMENTACIÓN ADJ_LIST WEIGHTED --

        La lista Adyacente pesada se implementa de la siguiente forma

        list = {"Ejemplo": [["a", 14], ["b",21]]}
        es un diccionario donde la llave es una matriz 2xn, donde el valor "0" es el nodo al que lleva y 
        el valor "1" es el peso de la conexión. se asume que el valor "1" siempre será un número.
        ...
        """
        dist = []
        for i in len():
            pass

        