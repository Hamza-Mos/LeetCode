class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        freqDiff = defaultdict(int)

        # word1 - add freq
        # word2 - subtract freq
        for c1, c2 in zip(word1, word2):
            freqDiff[c1] += 1
            freqDiff[c2] -= 1

        for freq in freqDiff.values():
            if abs(freq) > 3:
                return False

        return True
        