class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        currSet = []
        res = []

        def backtrack(index, currSum):
            if currSum == target:
                res.append(currSet[:])
                return

            if index == len(candidates):
                return 

            if currSum > target:
                return

            # add current number (possibly numerous times)
            currSet.append(candidates[index])
            backtrack(index, currSum + candidates[index])

            # do not add current number
            currSet.pop()
            backtrack(index + 1, currSum)

        backtrack(0, 0)

        return res
        