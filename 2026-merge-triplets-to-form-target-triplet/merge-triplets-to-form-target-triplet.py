class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # ignore triplets that have any value that is greater than the greatest value in the target array

        # set of all positions in triplets that match positions/values in the target list
        goodPositions = set()

        for t in triplets:
            # ignore triplets that have a value greater than the greatest value in target
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for index, val in enumerate(t):
                # found a good value
                if val == target[index]:
                    # we include index because it is possible that multiple triplets have 
                    # the same value at the same index so we should count them as 1 good position
                    goodPositions.add((index, val))

        return len(goodPositions) == 3 # found all 3 positions that match target
        