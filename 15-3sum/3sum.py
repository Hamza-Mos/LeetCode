class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            # skip duplicates of first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] > 0:
                return res

            left, right = i + 1, len(nums) - 1

            while left < right:
                currSum = nums[i] + nums[left] + nums[right]

                if currSum > 0:
                    right -= 1

                elif currSum < 0:
                    left += 1

                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1

                    while left < len(nums) and nums[left] == nums[left - 1]:
                        left += 1

        return res
        