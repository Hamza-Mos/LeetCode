class Solution:
    # helper function to check if input string is a palindrome
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        currPartition = []

        def dfs(i):
            # we have reached the end of the current string
            if i == len(s):
                # append a copy of the current partition to the result list
                res.append(currPartition[:])
                return

            for j in range(i, len(s)):
                # current substring is a palindrome
                if self.isPalindrome(s[i:j + 1]):
                    # partition the string at index j + 1
                    currPartition.append(s[i: j + 1])
                    dfs(j + 1)

                    # backtrack
                    currPartition.pop()

        dfs(0)

        return res
        