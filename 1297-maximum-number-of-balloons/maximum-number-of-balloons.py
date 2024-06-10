class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        inputFreq = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        for char in text:
            if char in inputFreq:
                inputFreq[char] += 1

        inputFreq["l"] = inputFreq["l"] // 2
        inputFreq["o"] = inputFreq["o"] // 2
        return min(inputFreq.values())
        