class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        cache = {}

        def dfs(index):
            if index == len(books):
                return 0

            if index in cache:
                return cache[index]

            # we are starting a shelf at current index (empty shelf to begin with)
            currWidth = shelfWidth
            maxHeight = 0
            cache[index] = float('inf')

            for i in range(index, len(books)):
                width, height = books[i]

                # cannot fit more books on current shelf
                if width > currWidth:
                    break

                maxHeight = max(height, maxHeight)
                currWidth -= width

                cache[index] = min(cache[index], dfs(i + 1) + maxHeight)

            return cache[index]

        return dfs(0)
        