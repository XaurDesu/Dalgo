class Solution:
    solved = {}
    def climbStairs(self, n: int) -> int:
        if n == 1: 
            return 1
        if n == 2: 
            return 2
        if n == 0:
            return 0
        else:
            if n in self.solved.keys():
                return self.solved[n]
            m = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.solved[n] = m
            return m