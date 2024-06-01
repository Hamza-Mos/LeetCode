class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        resLen = float('inf')
        res = ""

        tFreq = Counter(t)

        left = 0
        need = len(tFreq)

        sFreq = defaultdict(int)

        for right in range(len(s)):
            currChar = s[right]

            if currChar in tFreq:
                sFreq[currChar] += 1

                if sFreq[currChar] == tFreq[currChar]:
                    need -= 1

            while need == 0:
                if right - left + 1 < resLen:
                    res = s[left:right + 1]
                    resLen = right - left + 1

                if s[left] in tFreq:
                    sFreq[s[left]] -= 1

                    if sFreq[s[left]] < tFreq[s[left]]:
                        need += 1

                left += 1

        return res

            

            
        