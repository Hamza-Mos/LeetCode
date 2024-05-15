class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        MIN = -2 ** 31
        MAX = 2 ** 31 - 1

        while x:
            # get last digit
            digit = int(math.fmod(x, 10)) # fmod will return digit with the correct sign (regular % returns positive sign always)
            x = int(x / 10)

            # reversed integer will exceed max limit
            if (res > MAX // 10 or (res == MAX // 10 and digit >= MAX % 10)):
                return 0

            # reversed integer will exceed min limit
            if (res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10)):
                return 0

            res = res * 10 + digit

        return res
        