class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            res = min(res, nums[mid])

            # find current partition where mid is

            # we are in left partition - need to move right 
            if nums[mid] > nums[right]:
                left = mid + 1

            # we are in right partition - need to move left
            else:
                right = mid - 1

        return res