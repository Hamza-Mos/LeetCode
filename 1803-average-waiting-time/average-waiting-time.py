class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        currTime = 0
        res = 0

        for time, wait in customers:
            if time > currTime:
                currTime = time

            else:
                res += currTime - time

            res += wait
            currTime += wait

        return res / len(customers)
        