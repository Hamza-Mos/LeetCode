class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        res = []

        combinations = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def dfs(index, currString):
            # we have reached end of string (constructed a full string) so add it to res list and return
            if index == len(digits):
                res.append(currString)
                return

            # get the current digit
            curDigit = digits[index]

            for c in combinations[curDigit]:
                dfs(index + 1, currString + c)

        dfs(0, "")

        return res
            
        