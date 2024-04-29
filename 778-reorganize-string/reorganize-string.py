class Solution:
    def reorganizeString(self, s: str) -> str:
        output = ""
        
        charCounter = defaultdict(int)

        for char in s:
            # subtract 1 for count because we need negative counts to implement max heap properly later
            charCounter[char] -= 1

        maxHeap = [ [freq, char] for char, freq in charCounter.items() ]
        heapq.heapify(maxHeap)

        # we want to be as greedy as possible - get the max count character at all times first then fill
        # in the gaps with other characters
        while maxHeap:
            count, char = heapq.heappop(maxHeap)

            output += char
            foundSecondChar = False

            # still more characters in maxHeap
            if maxHeap:
                secondCount, secondChar = heapq.heappop(maxHeap)
                foundSecondChar = True

                output += secondChar

                secondCount += 1

                if secondCount:
                    heapq.heappush(maxHeap, [secondCount, secondChar])

            # add back the most frequent character if there are more of it leftover
            count += 1

            if count and not foundSecondChar:
                return ""

            if count:
                heapq.heappush(maxHeap, [count, char])

        return output

        

        