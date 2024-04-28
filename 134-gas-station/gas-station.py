class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # not possible
        if sum(gas) < sum(cost):
            return -1

        diff = 0
        start = 0

        for index in range(len(gas)):
            if diff < 0:
                diff = 0
                start = index

            diff += gas[index] - cost[index]

        return start
        