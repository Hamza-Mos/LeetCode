class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        bold = [False] * len(s)

        for index in range(len(s)):
            for word in words:
                if index + len(word) <= len(s) and s[index: index + len(word)] == word:
                    for i in range(index, index + len(word)):
                        bold[i] = True

        res = ""

        index = 0

        while index < len(bold):
            if bold[index]:
                res += "<b>"
                while index < len(bold) and bold[index]:
                    res += s[index]
                    index += 1

                res += "</b>"

            else:
                res += s[index]
                index += 1

        return res
        