class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProd = maxProd = 1
        res = float('-inf')

        for n in nums:
            temp = minProd
            minProd = min(n, minProd * n, maxProd * n)
            maxProd = max(n, temp * n, maxProd * n)

            res = max(maxProd, res)

        return res
        