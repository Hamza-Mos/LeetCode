class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        indexS = 0

        for char in t:
            if indexS == len(s):
                return True

            if char == s[indexS]:
                indexS += 1

        return indexS == len(s)
        