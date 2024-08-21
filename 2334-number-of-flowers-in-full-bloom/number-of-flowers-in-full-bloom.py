class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        """
        approach: 

        - like other interval problems, we want to sort flowers by start time, and people by arrival time
        - we will have 2 different indices:
            - one index for tracking the people list
            - one index for tracking the flowers list

        - since flowers will be sorted by start time, we will use a heap for end times
            - basically we will keep iterating over the flowers list until we reach a flower
              that has not bloomed yet before the current people[i] arrival time
            - for each flower, we will add its end time to the heap

            - in a separate loop, we will pop flowers that have ended blooming from our heap

            - we can track the count of flowers that each person sees by the length of the heap
                - heap will always contain the flowers that are in full bloom

            - (alternative approach): instead of sorting the flowers array, we could have a heap for
              start times of flowers and another one for end times of flowers. time complexity
              is the same but space complexity is worse

        m - length of flowers
        n - length of people
        time: O(nlogn + mlogm)
        space: O(n + m)

        """

        # we want to track the index for each person for the result list
        peopleList = [(time, index) for index, time in enumerate(people)]
        # sort people by arrival times
        peopleList.sort()

        # sort flowers by start time
        flowers.sort()

        res = [0] * len(people)
        minHeap = [] # stores end times of flowers

        flowersIndex = 0

        for currTime, peopleIndex in peopleList:
            # add flowers to heap that have started being in full boom
            while flowersIndex < len(flowers) and flowers[flowersIndex][0] <= currTime:
                heapq.heappush(minHeap, flowers[flowersIndex][1])
                flowersIndex += 1

            # remove flowers from heap that are past their end time
            while minHeap and minHeap[0] < currTime:
                heapq.heappop(minHeap)

            # update res
            count = len(minHeap)
            res[peopleIndex] = count

        return res