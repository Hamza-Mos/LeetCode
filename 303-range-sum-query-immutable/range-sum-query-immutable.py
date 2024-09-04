class NumArray:

    # use prefix sum!!
    def __init__(self, nums: List[int]):
        self.sums = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            self.sums[i + 1] = self.sums[i] + nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        # basically returns sum of nums up to and including nums[right] - sum of nums up to and including nums[left]
        return self.sums[right + 1] - self.sums[left]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)