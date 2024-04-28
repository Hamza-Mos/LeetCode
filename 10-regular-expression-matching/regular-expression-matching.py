class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # base cases:
        # if we have exceeded the bounds for both p and s, then we know we have a match - return True
        # if we have exceeded the bounds for s but not p then it is possible to have a match - no returns
            # ex: s = "a", p = "a*"
        # if we have exceeded the bounds for p but not s then it is impossible - return False

        # cache - takes indices for s and p and returns a boolean
        cache = {}

        def dfs(sIndex, pIndex):
            if sIndex >= len(s) and pIndex >= len(p):
                return True

            if pIndex >= len(p):
                return False

            if (sIndex, pIndex) in cache:
                return cache[(sIndex, pIndex)]

            # we got a character match or we have a "." wildcard for p (so we always have a guaranteed match)
            match = sIndex < len(s) and (s[sIndex] == p[pIndex] or p[pIndex] == ".")

            # if next character is a star ("*")
            if pIndex + 1 < len(p) and p[pIndex + 1] == "*":
                skipStar = dfs(sIndex, pIndex + 2)
                takeStar = match and dfs(sIndex + 1, pIndex)
                cache[(sIndex, pIndex)] = skipStar or takeStar
                return cache[(sIndex, pIndex)]

            elif match:
                cache[(sIndex, pIndex)] = dfs(sIndex + 1, pIndex + 1)
                return cache[(sIndex, pIndex)]

            cache[(sIndex, pIndex)] = False

            return cache[(sIndex, pIndex)]

        return dfs(0, 0)
        