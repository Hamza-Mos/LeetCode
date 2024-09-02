class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        bold = [False] * len(s)

        """

        there is no real optimization to this problem - brute force approach will work

        approach:

        - use a boolean array to mark whether or not the s[index] is bold
        - first loop:
            - for each index in the string, try checking if it is the start of any of the words 
              (by matching the current word with the same length substring in s)

                - if yes, then mark the entire substring as bold, otherwise do nothing

        - second loop:
            - create the result string
            - cover the bolded regions with the bold markers

        - return result string

        time: O(n * m * k) where n is len(s), m is len(words), and n is the max length of an individual word
        space: O(n) where n is len (s) for the boolean array

        """

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
        