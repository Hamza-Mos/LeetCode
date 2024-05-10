class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = sorted([(-scor, index) for index, scor in enumerate(score)])
        res = [0] * len(score)

        for i, (scor, index) in enumerate(ranks):
            if i == 0:
                res[index] = "Gold Medal"

            elif i == 1:
                res[index] = "Silver Medal"

            elif i == 2:
                res[index] = "Bronze Medal"
            
            else:
                res[index] = str(i + 1)

        return res
        