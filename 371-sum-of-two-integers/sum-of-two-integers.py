class Solution:
    def getSum(self, a: int, b: int) -> int:
        # python's integers are not 32 bits long so we use a bitmask to ensure they're 32 bits
        bitMask = 0xffffffff

        # b will hold carry, and a will hold current sum
        while b:
            carry = (a & b) << 1

            a = (a ^ b) & bitMask

            b = carry & bitMask 
        
        if a > bitMask // 2:
            return ~(a ^ bitMask)

        return a