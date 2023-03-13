# Primera solucion, muere en memoria.
class Solution:
    def bfs(self, image, sr, sc, prev_color, new_color):
        image[sr][sc] == new_color
        adj = [ 
                [sr+1,sc],
        [sr,sc-1],   [sr,sc+1],
                [sr-1,sc]
        ]
        for i in adj:
            if i[0] < len(image) and i[1] < len(image[0]) and image[i[0]][i[1]] == prev_color:
                image = self.bfs(image, i[0],i[1], prev_color, new_color)
        return image

    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        image = self.bfs(image, sr, sc, image[sr][sc], color)
