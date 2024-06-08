class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        # output: [a, b]
        # sumAlice - a + b = sumBob + a - b
        # b = a + (sumBob - sumAlice)/2

        sumAlice, sumBob = sum(aliceSizes), sum(bobSizes)

        setBob = set(bobSizes)

        for a in aliceSizes:
            if a + (sumBob - sumAlice)/2 in setBob:
                return [a, a + (sumBob - sumAlice)/2]