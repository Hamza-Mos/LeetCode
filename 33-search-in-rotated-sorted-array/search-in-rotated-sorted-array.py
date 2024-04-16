class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # found target
            if nums[mid] == target:
                return mid

            # find current partition

            # left partition
            if nums[mid] > nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1

                else:
                    left = mid + 1

            # right partition
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1

                else:
                    right = mid - 1

        return -1
        