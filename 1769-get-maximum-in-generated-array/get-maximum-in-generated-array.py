class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0]
        n += 1

        if n == 1:
            return 0

        nums.append(1)

        for i in range(2, n):
            if i % 2 == 1:
                nums.append(nums[i // 2] + nums[(i // 2) + 1])

            else:
                nums.append(nums[i // 2])

        print(nums)

        return max(nums)
        