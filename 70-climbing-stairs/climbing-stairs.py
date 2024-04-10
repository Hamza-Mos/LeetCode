class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        n1 = 1 # first step
        n2 = 2 # second step

        for i in range(3, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp

        return n2
        