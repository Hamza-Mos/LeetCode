class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(num, power):
            if power < 0:
                return 1 / pow(num, -power)

            if power == 0:
                return 1

            res = pow(num, power // 2)
            res = res * res

            if power % 2 == 1:
                res *= num

            return res

        return pow(x, n)
        