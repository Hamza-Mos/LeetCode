class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        currSet = []
        candidates.sort()

        def dfs(index, currSum):
            if currSum == target:
                res.append(currSet[::])
                return

            if index == len(candidates):
                return

            if currSum > target:
                return

            currSet.append(candidates[index])
            dfs(index + 1, currSum + candidates[index])

            currSet.pop()

            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1

            dfs(index + 1, currSum)

        dfs(0, 0)

        return res
        