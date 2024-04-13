class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = defaultdict(int)
        left = 0
        res = 0
        maxFreq = 0

        for right in range(len(s)):
            char = s[right]
            freqMap[char] += 1
            maxFreq = max(freqMap[char], maxFreq)

            while (right - left + 1) - maxFreq > k:
                freqMap[s[left]] -= 1
                left += 1

            res = max(right - left + 1, res)

        return res