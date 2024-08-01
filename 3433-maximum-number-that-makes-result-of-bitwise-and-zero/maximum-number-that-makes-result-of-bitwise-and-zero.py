class Solution:
    def maxNumber(self, n: int) -> int:
        # intuition number 2^x &ed with 2^(x - 1) will be 0
        # log2(n) will give us x
        
        return 2 ** floor(log2(n)) - 1

        