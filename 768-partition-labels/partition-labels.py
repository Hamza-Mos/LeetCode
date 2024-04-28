class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charLastIndex = { char : index for index, char in enumerate(s) }

        res = []
        start = 0
        end = 0

        for index in range(len(s)):
            char = s[index]
            end = max(end, charLastIndex[char])

            if index == end:
                res.append(end - start + 1)
                start = end + 1

        return res