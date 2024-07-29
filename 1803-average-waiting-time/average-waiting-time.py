class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        currTime = 0
        res = 0

        for time, wait in customers:
            if time > currTime: # customer order time is later than the time that the prev order finished
                currTime = time

            else: # time of previous order and current order overlaps
                res += currTime - time # add the additional wait time

            res += wait
            currTime += wait # update currTime to the time that the order time will be finished

        return res / len(customers)
        