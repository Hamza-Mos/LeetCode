class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        currSet = []
        res = []

        def dfs(index, currSum):
            if currSum == target:
                res.append(currSet[::])
                return

            if index == len(candidates):
                return

            if currSum > target:
                return

            currSet.append(candidates[index])
            dfs(index, currSum + candidates[index])

            currSet.pop()
            dfs(index + 1, currSum)

        dfs(0, 0)

        return res
        