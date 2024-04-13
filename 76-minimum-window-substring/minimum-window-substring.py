class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        window = ""

        freqForT = defaultdict(int)
        freqForS = defaultdict(int)

        for c in t:
            freqForT[c] += 1

        left = 0
        need = len(freqForT)
        for right in range(len(s)):
            if s[right] in freqForT:
                freqForS[s[right]] += 1

                if freqForS[s[right]] == freqForT[s[right]]:
                    need -= 1

            while need == 0:
                if window == "" or len(window) > right - left + 1:
                    window = s[left:right + 1]

                charToRemove = s[left]
                left += 1

                if charToRemove in freqForT:
                    freqForS[charToRemove] -= 1

                    if freqForS[charToRemove] < freqForT[charToRemove]:
                        need += 1
            
        return window