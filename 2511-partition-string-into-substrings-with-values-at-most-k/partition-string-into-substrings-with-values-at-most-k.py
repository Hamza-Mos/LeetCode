class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        # we want to be greedy and make each substring as big as possible
        currSubstr = ""
        res = 0

        for i in range(len(s)):
            if int(currSubstr + s[i]) > k:
                if int(s[i]) > k:
                    return -1

                else:
                    res += 1
                    currSubstr = s[i]

            else:
                currSubstr += s[i]

        res += 1

        return res
        