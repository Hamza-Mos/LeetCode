class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # take max jump each time
        goal = 0
        currIndex = 0
        maxJump = 0

        while currIndex < len(nums) - 1:
            currJump = currIndex + nums[currIndex]
            maxJump = max(maxJump, currJump)

            if currIndex == goal:
                if maxJump == goal:
                    return False

                goal = maxJump

            currIndex += 1

        return True
        