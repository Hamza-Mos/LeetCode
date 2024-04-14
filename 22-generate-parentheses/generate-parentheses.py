class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(s, open, close):
            if len(s) == 2*n:
                res.append(s)

            if open > 0:
                backtrack(s + "(", open - 1, close)

            if open < close:
                backtrack(s + ")", open, close - 1)

        
        backtrack("", n, n)

        return res