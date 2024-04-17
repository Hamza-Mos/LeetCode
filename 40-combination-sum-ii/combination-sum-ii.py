class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort to easily remove duplicates
        candidates.sort()

        res = []
        currSet = []

        def backtrack(index, currSum):
            if currSum == target:
                res.append(currSet[:])
                return

            if currSum > target:
                return

            if index == len(candidates):
                return

            # add candidates[index] to currSet and move to next number
            currSet.append(candidates[index])
            backtrack(index + 1, candidates[index] + currSum)

            # do not add candidates[index] to currSet
            currSet.pop()

            # move index to last occurrence of candidates[index]
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1

            backtrack(index + 1, currSum)

        backtrack(0, 0)
        return res
        