class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            res = min(nums[mid], res)

            # find out which partition we are in

            # left sorted partition
            if nums[mid] > nums[right]:
                # move left towards the start of the right sorted partition
                left = mid + 1

            # right sorted partition
            else:
                # move left towards the start of the left sorted partition
                right = mid - 1

        return res
        