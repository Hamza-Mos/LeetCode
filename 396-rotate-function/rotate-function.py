class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # array = [a, b, c]
        # F(0) = 0*a + 1*b + 2*c
        # F(1) = 0*c + 1*a + 2*b
        # F(1) - F(0) = (a + 2b) - (b + 2c) = a + b - 2c 
        # F(1) = F(0) + (a + b - 2c)
        # F(1) = F(0) + (a + b + c) - 3c
        # sooo???
        # F(k) = F(k - 1) + SUM - N * nums[N - k] ??

        currResult = 0
        sumNums = 0

        for i in range(len(nums)):
            currResult += i * nums[i]
            sumNums += nums[i]

        answer = currResult
        prevResult = currResult
        currResult = 0
        N = len(nums)

        for k in range(1, len(nums)):
            currResult = prevResult + sumNums - (N * nums[N - k])
            answer = max(currResult, answer)
            prevResult = currResult

        return answer
        