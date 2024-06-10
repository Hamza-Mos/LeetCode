class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        inputFreq = defaultdict(int)
        for char in text:
            inputFreq[char] += 1

        res = 0

        while inputFreq["b"] and inputFreq["a"] and inputFreq["n"] and inputFreq["l"] >= 2 and inputFreq["o"] >= 2:
            res += 1
            inputFreq["b"] -= 1
            inputFreq["a"] -= 1
            inputFreq["l"] -= 2
            inputFreq["o"] -= 2
            inputFreq["n"] -= 1

        return res
        