class Solution:
    def getSum(self, a: int, b: int) -> int:
        # python's integers are not 32 bits long so we use a bitmask to ensure they're 32 bits
        bitMask = 0xffffffff

        # b will hold carry, and a will hold current sum
        while b:
            carry = (a & b) << 1

            a = (a ^ b) & bitMask

            b = carry & bitMask 
        
        # check if a is negative (python uses infinite leading 1's for negative numbers)
        # bitMask // 2 is 0b0111111111111111111111111111111
        # a number is only negative if the 32nd bit is a 1
        if a > bitMask // 2:
            return ~(a ^ bitMask)

        return a