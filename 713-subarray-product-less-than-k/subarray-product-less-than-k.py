class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        left = 0
        product = 1

        for right in range(len(nums)):
            currNum = nums[right]
            product *= currNum

            # shrink window from left until product is valid again
            while product >= k and left <= right:
                product = product // nums[left]
                left += 1

            res += (right - left + 1)

        return res

        