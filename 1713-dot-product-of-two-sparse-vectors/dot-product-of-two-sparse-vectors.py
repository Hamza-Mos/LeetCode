class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = []

        for index, num in enumerate(nums):
            if num:
                self.nums.append((index, num))
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        nums1, nums2 = self.nums, vec.nums

        index1 = index2 = 0

        res = 0

        while index1 < len(nums1) and index2 < len(nums2):
            # check if indices are the same
            if nums1[index1][0] == nums2[index2][0]:
                res += nums1[index1][1] * nums2[index2][1]
                index1 += 1
                index2 += 1

            elif nums2[index2][0] < nums1[index1][0]:
                index2 += 1

            else:
                index1 += 1

        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)