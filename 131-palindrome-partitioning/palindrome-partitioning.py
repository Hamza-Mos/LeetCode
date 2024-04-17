class Solution:
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1

        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        currPartition = []

        def backtrack(index):
            if index == len(s):
                res.append(currPartition[:])
                return

            for i in range(index, len(s)):
                if self.isPalindrome(s[index : i + 1]):
                    currPartition.append(s[index : i + 1])
                    backtrack(i + 1)
                    currPartition.pop()

        backtrack(0)
        return res