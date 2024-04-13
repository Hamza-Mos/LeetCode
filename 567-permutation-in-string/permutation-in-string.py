class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        freq1, freq2 = [0] * 26, [0] * 26

        for i in range(len(s1)):
            char1 = ord(s1[i]) - ord('a')
            char2 = ord(s2[i]) - ord('a')

            freq1[char1] += 1
            freq2[char2] += 1

        matches = 0

        for i in range(26):
            if freq1[i] == freq2[i]:
                matches += 1

        left = 0

        for right in range(len(s1), len(s2)):
            if matches == 26:
                break

            newChar = ord(s2[right]) - ord('a')
            oldChar = ord(s2[left]) - ord('a')

            # case 1: we were at correct frequencies for newChar before but no longer the case
            if freq1[newChar] == freq2[newChar]:
                matches -= 1

            # case 2: we will now be at correct frequencies
            if freq1[newChar] == freq2[newChar] + 1:
                matches += 1

            freq2[newChar] += 1

            # case 3: we were at correct frequences for oldChar before but no longer the case
            if freq1[oldChar] == freq2[oldChar]:
                matches -= 1

            # case 4: we will now be at correct frequencies
            if freq1[oldChar] == freq2[oldChar] - 1:
                matches += 1

            freq2[oldChar] -= 1

            left += 1

        return matches == 26
        