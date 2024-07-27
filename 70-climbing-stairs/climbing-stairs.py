class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        n1 = 1
        n2 = 2

        for i in range(3, n + 1):
            currStep = n1 + n2
            n1 = n2
            n2 = currStep

        return n2

        