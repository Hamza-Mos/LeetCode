class Leaderboard:

    """
    approach:

        - basically use a hashmap to keep track of scores
        - use a heap to retrieve the top k scores then get the sum of those

    """

    def __init__(self):
        self.scores = defaultdict(int)
        

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score
        

    def top(self, K: int) -> int:
        # get top k values
        minHeap = []

        for score in self.scores.values():
            if len(minHeap) == K:
                if score > minHeap[0]:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, score)

            else:
                heapq.heappush(minHeap, score)

        return sum(minHeap)
        

    def reset(self, playerId: int) -> None:
        del self.scores[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)