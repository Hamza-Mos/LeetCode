class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freqMap = collections.defaultdict(int)

        for n in hand:
            freqMap[n] += 1

        minHeap = list(freqMap.keys())
        heapq.heapify(minHeap)

        while minHeap:
            currMin = minHeap[0]

            for num in range(currMin, currMin + groupSize):
                if num not in freqMap:
                    return False

                freqMap[num] -= 1

                if freqMap[num] == 0:
                    if num != minHeap[0]:
                        return False

                    heapq.heappop(minHeap)

        return True
        