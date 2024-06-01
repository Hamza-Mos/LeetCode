class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        for i in range(len(s1)):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1

        matches = 0

        for i in range(26):
            matches += freq1[i] == freq2[i]

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                print([left, right])
                return True

            # remove left character

            leftChar = ord(s2[left]) - ord('a')

            if freq1[leftChar] == freq2[leftChar]:
                matches -= 1

            if freq1[leftChar] == freq2[leftChar] - 1:
                matches += 1

            freq2[leftChar] -= 1
            left += 1

            rightChar = ord(s2[right]) - ord('a')

            if freq1[rightChar] == freq2[rightChar]:
                matches -= 1

            if freq1[rightChar] == freq2[rightChar] + 1:
                matches += 1

            freq2[rightChar] += 1

        return matches == 26
        