class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            res = res << 1
            bit = n & 1
            res = res | bit
            n = n >> 1

        return res