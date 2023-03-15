class solution:
    # Salvo el ultimo metodo AdjList es un diccionario con la siguiente estructura
    # {1:[2,3,4], 2:[1], 3:[1,4], 4:[3,1]}
    # Todos los grafos son grafos no dirigidos!
    # Los nombres de los nodos son numeros naturales!
    def BFS_connect(AdjList: dict, Node1: int, Node2: int) -> bool:
        """
        Dados dos nodos del grafo, retorne True si están conectados, False en otro caso  
        """
        pass
    def BFS_shortest_path(AdjList: dict, Node1: int, Node2: int) -> List[int]:
        """
        Dados dos nodos del grafo, retorne el camino de menor longitud.
        El camino de menor longitud debe ser un lista de los nodos por los cuales
        se debe pasar para llegar del Nodo1 al Nodo2, incluyéndolos. Si los nodos
        no están conectados se debe devolver una lista vacía.  
        """
        pass
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        An image is represented by an m x n integer grid image where image[i][j] 
        represents the pixel value of the image.

        You are also given three integers sr, sc, and color. You should perform 
        a flood fill on the image starting from the pixel image[sr][sc].

        To perform a flood fill, consider the starting pixel, plus any pixels 
        connected 4-directionally to the starting pixel of the same color as 
        the starting pixel, plus any pixels connected 4-directionally 
        to those pixels (also with the same color), and so on. 
        Replace the color of all of the aforementioned pixels with color.

        https://leetcode.com/problems/flood-fill/
        """
    def DFS_isTree(AdjList:dict) -> bool:
        """
        Escriba un algoritmos basados en DFS tal que dado un grafo retorne 
        True sii el grafo es un arbol, en otro caso False.
        """
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
        ...
        """