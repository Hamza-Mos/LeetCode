class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26

        for t in tasks:
            freq[ord(t) - ord('A')] += 1

        freq.sort()

        maxFreq = freq[-1] - 1
        idleSlots = maxFreq * n

        for i in range(0, 25):
            idleSlots -= min(maxFreq, freq[i])

        return len(tasks) + max(idleSlots, 0)

        