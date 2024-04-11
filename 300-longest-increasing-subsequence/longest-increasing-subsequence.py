class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # patient sort
        sequence = [nums[0]]

        for n in nums[1:]:

            if n > sequence[-1]:
                sequence.append(n)

            else:
                index = bisect_left(sequence, n)
                sequence[index] = n

        return len(sequence)
        