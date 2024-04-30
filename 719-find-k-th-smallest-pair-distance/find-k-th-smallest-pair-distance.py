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

            # If `mid` produced `k` or more results we know it's the upper bound
            if numDifferences >= k:
                # We don't set to `mid - 1` because we found a number of distances
                # bigger than *or equal* to `k`. If this `mid` ends up being
                # actually equal to `k` then it's a correct guess, so let's leave it within
                # the guess space.
                right = mid

            # If `mid` did not produce enouh results, let's increase the guess
            # space and try a higher number.
            else:
                left = mid + 1

        # `left` ends up being an actual distance in the input, because
        # the binary search mechanism waits until the exact left/right combo where
        # 2nd to last `mid` did not produce enough results (k or more), but
        # the last `mid` did.
        return left

"""
Complexity:
-   Time complexity: O(log⁡(max−min) × n + nlog⁡n)
    - for each iteration of binary search (min - max), we loop through array [ O(log⁡(max−min) × n) ]
    - sorting: O(nlog⁡n)
-   Space complexity: O(1)

"""