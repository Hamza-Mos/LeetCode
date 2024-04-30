class Solution:
    # solution explanation: https://leetcode.com/problems/find-k-th-smallest-pair-distance/solutions/4668403/c-python-java-using-binary-search-and-sorting/
    """
    Intuition:

    -   The problem requires us to find the k-th smallest distance among all pair distances in a given array.
    -   The distance between any two pairs is defined by the absolute difference between those two elements.
    -   Sorting the array initially helps in efficiently finding pair distances using a two-pointer or binary 
        search technique.

    """
    
    def position(self, nums, m):
        ans = 0
        for i in range(len(nums) - 1):
            index = bisect.bisect_right(nums, nums[i] + m)
            ans += (index - 1 - i)
        return ans


    """
    Approach

    -   Sort the Array: Begin by sorting the array to ensure that all pairs can be considered in non-decreasing 
        order of distances.

    -   Binary Search on Distance: Use binary search on the range of possible distances (from 0 to the maximum 
        distance possible, which is max(nums) - min(nums)).

        -   Determining Midpoint Distance (m): For each midpoint m during the binary search, calculate how many 
            pairs have a distance less than or equal to m.

        -   Counting Pairs: Iterate through the sorted array, using upper_bound to find the first element that is 
            greater than nums[i] + m. This allows calculation of the number of elements within the desired 
            distance m from nums[i].

        -   Adjusting Search Range: If the number of such pairs is greater than or equal to k, narrow the search 
            to the left (lower distances). Otherwise, narrow it to the right (higher distances).

    -   Finding the Exact Distance: The loop exits when the search range is minimized, and the smallest distance 
        that meets the condition is found.

    """

    def smallestDistancePair(self, nums, k):
        # Sort the Array
        nums.sort()

        # range of values for possible differences: 0 to (max - min)
        left, right = 0, nums[-1] - nums[0]

        # binary search
        while left < right:
            mid = (left + right) // 2

            numDifferences = self.position(nums, mid)

            # print(mid)
            # if numDifferences == k:
            #     return mid

            # make difference lower since we want to find the upper bound where numDifferences == k
            if numDifferences >= k:
                right = mid

            else:
                left = mid + 1

        return left

"""
Complexity:
-   Time complexity: O(log⁡(max−min) × n + nlog⁡n)
    - for each iteration of binary search (min - max), we loop through array [ O(log⁡(max−min) × n) ]
    - sorting: O(nlog⁡n)
-   Space complexity: O(1)

"""