class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # very similar to longest common subsequence problem
        # if word1[i] == word2[j], then we move both pointers
        # else, we would try one of the operations (insert, delete, replace):
            # insert (move pointer j but keep i) - we would insert the character at word2[j] into word1[i]
            # so we would keep pointer i for word1 but move pointer j because we are guaranteed a match of 
            # the newly inserted character and word2[j]

            # delete (move pointer i but keep j) - we would delete the character at word1[i] and move onto the next
            # character in word1 to see if it matches with word2[j]

            # replace (move pointer i and j) - we would replace word1[i] with the character at word2[j]

        # first we build our 2D grid with initial values (dp[i][j] represents min number of operations to get 
        # word1[i:] == word2[j:])

        ROWS, COLS = len(word1), len(word2)

        dp = [ [float('inf')] * (COLS + 1) for i in range(ROWS + 1) ]

        # if word2 is empty then number of operations (deletes) will be the length of word1
        for row in range(ROWS + 1):
            dp[row][COLS] = len(word1) - row

        # if word1 is empty then number of operations (inserts) will be length of word2
        for col in range(COLS + 1):
            dp[ROWS][col] = len(word2) - col

        # now actual iterative dp:
        for index1 in range(len(word1) - 1, -1, -1):
            for index2 in range(len(word2) - 1, -1, -1):
                # match - so dp[i][j] = dp[i + 1][j + 1] (min number of operations at next index)
                if word1[index1] == word2[index2]:
                    dp[index1][index2] = dp[index1 + 1][index2 + 1]

                # no match - we apply operations
                else:
                    insert = dp[index1][index2 + 1]
                    replace = dp[index1 + 1][index2 + 1]
                    delete = dp[index1 + 1][index2]
                    dp[index1][index2] = 1 + min(insert, replace, delete)

        return dp[0][0]