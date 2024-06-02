class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            # find out which partition we are in

            # left sorted partition
            if nums[mid] > nums[high]:
                # target is to our left
                if nums[low] <= target < nums[mid]:
                    high = mid - 1

                else:
                    low = mid + 1

            # right sorted partition
            else:
                # target is to our right
                if nums[mid] < target <= nums[high]:
                    low = mid + 1

                else:
                    high = mid - 1

        return -1
        