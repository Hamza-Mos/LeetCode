class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low = 0
        high = len(citations) - 1

        res = 0

        while low <= high:
            mid = (low + high) // 2

            numCitations = citations[mid]

            if numCitations >= len(citations) - mid:
                res = max(res, len(citations) - mid)
                high = mid - 1

            elif numCitations < len(citations) - mid:
                low = mid + 1

        return res
        