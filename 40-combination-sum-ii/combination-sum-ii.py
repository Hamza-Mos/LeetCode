class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = set()
        curSet = []

        def backtrack(index, curSum):
            if curSum == target:
                res.add(tuple(curSet))
                return

            if index == len(candidates) or curSum > target:
                return

            # include current number in the current list and sum
            curSet.append(candidates[index])
            backtrack(index + 1, curSum + candidates[index])

            # do not include current number in the current list and sum
            curSet.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1

            backtrack(index + 1, curSum)

        backtrack(0, 0)

        return res
        