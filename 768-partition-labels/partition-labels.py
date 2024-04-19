class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndexMap = {}

        # map each character to its last index
        for index, char in enumerate(s):
            lastIndexMap[char] = index

        endOfCurrentPartition = 0
        startOfCurrentPartition = 0
        res = []

        # partition string
        for index, char in enumerate(s):
            endOfCurrentPartition = max(lastIndexMap[char], endOfCurrentPartition)

            if index == endOfCurrentPartition:
                res.append(endOfCurrentPartition - startOfCurrentPartition + 1)
                startOfCurrentPartition = index + 1

        return res
        