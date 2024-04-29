class Solution:
    def isHappy(self, n: int) -> bool:
        def getSquaredSumOfDigits(num):
            sum = 0

            while num:
                sum += (num % 10) ** 2
                num = num // 10

            return sum

        slow, fast = n, getSquaredSumOfDigits(n)

        while slow != fast and fast != 1:
            fast = getSquaredSumOfDigits(getSquaredSumOfDigits(fast))
            slow = getSquaredSumOfDigits(slow)

        return fast == 1
        