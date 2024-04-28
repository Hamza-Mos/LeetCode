class Solution:
    def jump(self, nums: List[int]) -> int:
        maxJump = 0
        numJumps = 0
        goal = 0

        for index in range(0, len(nums) - 1):
            currJump = nums[index] + index
            maxJump = max(maxJump, currJump)

            if index == goal:
                # not possible
                if maxJump == goal:
                    return -1

                numJumps += 1
                goal = maxJump

        return numJumps
        