class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                return res

            # prevent duplicates for nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                currSum = nums[i] + nums[left] + nums[right]

                if currSum > 0:
                    right -= 1

                elif currSum < 0:
                    left += 1

                # found a triplet
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1

                    # prevent duplicates for nums[left]
                    while left < len(nums) and nums[left] == nums[left - 1]:
                        left += 1

        return res