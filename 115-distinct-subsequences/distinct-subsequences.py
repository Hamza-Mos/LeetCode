class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        def findSubsequences(indexForS, indexForT):
            # found a valid subsequence (reached end of t)
            if indexForT == len(t):
                return 1
            
            # not a valid subsequence (reached end of s)
            if indexForS == len(s):
                return 0

            # check cache
            if (indexForS, indexForT) in cache:
                return cache[(indexForS, indexForT)]

            if s[indexForS] == t[indexForT]:
                cache[(indexForS, indexForT)] = findSubsequences(indexForS + 1, indexForT + 1) + findSubsequences(indexForS + 1, indexForT)

            else:
                cache[(indexForS, indexForT)] = findSubsequences(indexForS + 1, indexForT)

            return cache[(indexForS, indexForT)]

        return findSubsequences(0, 0)

        