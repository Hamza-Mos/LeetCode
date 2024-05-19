class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = { char: index for index, char in enumerate(order) }

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]

            foundDiff = False

            for j in range(min(len(word1), len(word2))):
                char1, char2 = word1[j], word2[j]

                # no difference found
                if char1 == char2:
                    continue

                # valid
                if orderMap[char1] < orderMap[char2]:
                    foundDiff = True
                    break

                # invalid order
                else:
                    return False

            # invalid
            if not foundDiff and len(word1) > len(word2):
                return False

        return True