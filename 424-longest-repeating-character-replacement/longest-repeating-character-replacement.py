class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        maxFreq = 0
        res = 0
        left = 0

        for right in range(len(s)):
            char = s[right]
            freq[s[right]] += 1
            maxFreq = max(maxFreq, freq[s[right]])

            while (right - left + 1) - maxFreq > k:
                freq[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res