class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # calculate difference for how much more it would cost to send person to cityB instead of cityA
        diff = sorted([ [cityA - cityB, cityA, cityB] for cityA, cityB in costs ])
        N = len(costs) // 2
        res = 0

        # cityA
        for i in range(N):
            res += diff[i][1]

        # cityB
        for i in range(N, len(diff)):
            res += diff[i][2]

        return res

