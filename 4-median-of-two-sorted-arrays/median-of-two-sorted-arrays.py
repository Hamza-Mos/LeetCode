class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        M, N = len(nums1), len(nums2)

        # smaller array should be nums1

        # low, high represent the number of elements in nums1 that will be in the left partition
        low, high = 0, M

        while low <= high:
            """
            I was initially confused about why it is (m + n + 1) // 2 instead of just (m + n) // 2 and I think the 
            following is the reason.

            Given that m+n is the total count of elements:

            For the odd number total count of elements, this tips the scale of the number of elements to be 
            1 extra in the left side of the partitions, allowing you to know the median is one of the elements 
            just to the left of the partition on either nums1 or nums2. (As in the code 
            return max(maxLeftA, maxLeftB)).

            For the case of even number total count of elements, the +1 does not affect the quotient due to the 
            truncation of the 0.5 part.
            """

            partitionA = (low + high) // 2
            partitionB = (M + N + 1) // 2 - partitionA

            # partitionA and partitionB represent the number of elements in the left parition for both arrays
            # so that's why we subtract 1 to get the index of the max element in the left partition
            maxLeftA = float('-inf') if partitionA - 1 < 0 else nums1[partitionA - 1]
            maxLeftB = float('-inf') if partitionB - 1 < 0 else nums2[partitionB - 1]

            minRightA = float('inf') if partitionA >= M else nums1[partitionA]
            minRightB = float('inf') if partitionB >= N else nums2[partitionB]

            # correct partitions
            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                # odd length
                if (M + N) % 2 == 1:
                    return max(maxLeftA, maxLeftB)

                else:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2

            # go left
            elif maxLeftA > minRightB:
                high = partitionA - 1

            # go right
            else:
                low = partitionA + 1

        