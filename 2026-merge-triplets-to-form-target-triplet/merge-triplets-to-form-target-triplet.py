class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # get rid of triplets that have any element greater than the corresponding element in target
        # keep track of good elements that match up with elements in target in a set
        # if size of set is 3 then we have all elements needed to get to target

        goodElements = set()

        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue

            for index, num in enumerate(triplet):
                if num == target[index]:
                    goodElements.add((index, num))

        return len(goodElements) == 3