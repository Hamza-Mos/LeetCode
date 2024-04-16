class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        totalLen = len(nums1) + len(nums2)
        half = totalLen // 2

        low, high = 0, len(nums1) - 1

        while True:
            mid = (low + high) // 2

            # nums1 pivot elements
            left1 = nums1[mid] if mid >= 0 else float('-inf')
            right1 = nums1[mid + 1] if mid + 1 < len(nums1) else float('inf')

            nums2Pivot = half - (mid + 1) - 1

            # nums2 pivot elements
            left2 = nums2[nums2Pivot] if nums2Pivot >= 0 else float('-inf')
            right2 = nums2[nums2Pivot + 1] if nums2Pivot + 1 < len(nums2) else float('inf')

            # we found correct partition
            if left1 <= right2 and left2 <= right1:
                # even
                if totalLen % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2

                # odd
                else:
                    return min(right1, right2)

            elif left1 > right2:
                high = mid - 1

            else:
                low = mid + 1
        