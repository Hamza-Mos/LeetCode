class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # impossible
        if sum(gas) < sum(cost):
            return -1

        total = 0
        start = 0

        for index in range(len(gas)):
            total += gas[index] - cost[index]

            if total < 0:
                total = 0
                start = index + 1

        return start