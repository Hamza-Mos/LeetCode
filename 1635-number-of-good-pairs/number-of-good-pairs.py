class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
        approach:

            - use hashmap to count frequency of numbers
            - iterate through each number in the array
                - add the count of the number in the hashmap to the result
                - increment the frequency of the number by 1

            - return result

        """
        numCount = defaultdict(int)
        res = 0

        for n in nums:
            res += numCount[n]
            numCount[n] += 1

        return res

        