class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = 0
        maxJump = 0

        index = 0

        while index < len(nums) - 1:
            maxJump = max(maxJump, nums[index] + index)
            
            if index == goal:
                if index == maxJump:
                    return False

                goal = maxJump

            index += 1

        return True

        