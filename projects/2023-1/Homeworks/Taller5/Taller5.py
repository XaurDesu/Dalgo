import math
class solution:
    # AdjList es un diccionario con la siguiente estructura
    # {1:[[2,-2],[3,30],[4,1]], 2:[[1,-2]], 3:[[1,30],[4,-1]], 4:[[3,-1],[1,1]]}
    # Donde la segunda coordenada representa el costo entre los dos nodos
    # Todos los grafos son grafos no dirigidos!
    # Los nombres de los nodos son numeros naturales!

    def __init__(self, AbjList: dict):
        self.AbjList = AbjList

    def FLoyd_Warshall_Negative_Cylcle_Detection(self, Node1: int, Node2: int) -> bool:
        """
        Dados dos nodos del grafo, Retorna:
            True: si el camino de menor costo (calculado usando Floy Warsall) no contiene 
                  ciclos negativos  
            False: si el camino de menor costo (calculado usando Floy Warsall) contiene 
                  ciclos negativos  
        """
        dist = []
        for i in len(self.AbjList)
        dist.append([0]*len(self.AbjList))

        for i in self.AbjList.keys():
            dist[i][i] = 0
            for j in self.AbjList[i]:
                dist[i][j[0]] = j[1]
        
        for k in range(1, len(dist)):
            for i in range(1, len(dist)):
                for j in range(1, len(dist)):
                    if dist[i][i] < 0:
                        return True
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        return False
        
    def MST_Connect_All_Points(self, points: List[List[int]]) -> int:
        """
        Dada una lista de puntos puntos que representa coordenadas enteras de algunos puntos en un plano 2D
        El coste de conectar dos puntos  es la distancia euclidean 
        Devuelve el coste mínimo para que todos los puntos estén conectados. 
        Todos los puntos están conectados si hay exactamente un camino simple entre dos puntos cualesquiera.

        Ejemplos:
            - MST_Connect_All_Point([[0,0],[2,2],[3,10],[5,2],[7,0]]) = 20
            - MST_Connect_All_Point([[3,12],[-2,5],[-4,1]]) = 18
        """
        pass