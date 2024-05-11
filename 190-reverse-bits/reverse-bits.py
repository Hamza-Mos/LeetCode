class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            # move res 1 bit left
            res = res << 1

            # get rightmost bit for n
            bit = n & 1

            # add bit to end of res
            res = res | bit

            # bitshift n to the right
            n = n >> 1

        return res