class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]

        while slow != fast:
            fast = nums[nums[fast]]
            slow = nums[slow]

        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
        