class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sIdx = pIdx = 0
        starIdx = sTmpIdx = -1
        sLen, pLen = len(s), len(p)

        while sIdx < sLen:
            if pIdx < pLen and (p[pIdx] == s[sIdx] or p[pIdx] == "?"):
                sIdx += 1
                pIdx += 1
            elif pIdx < pLen and p[pIdx] == "*":
                starIdx = pIdx
                sTmpIdx = sIdx
                pIdx += 1
            elif starIdx != -1:
                pIdx = starIdx + 1
                sIdx = sTmpIdx + 1
                sTmpIdx = sIdx
            else:
                return False

        return all(x == "*" for x in p[pIdx:])
