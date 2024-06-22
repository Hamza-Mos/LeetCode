class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Indices = { num: index for index, num in enumerate(nums1) }
        print(nums1Indices)

        stack = []
        res = [-1] * len(nums1)

        for i, num in enumerate(nums2):
            while stack and stack[-1] < num:
                lastNum = stack[-1]
                if lastNum in nums1Indices:
                    numIndex = nums1Indices[lastNum]
                    res[numIndex] = num
                stack.pop()

            stack.append(num)

        return res
        