class Twitter:

    def __init__(self):
        # maps a userId to a set of followeeIds
        self.followMap = collections.defaultdict(set)

        # maps a userId to a list of tweetIds
        self.tweetMap = collections.defaultdict(list)

        # acts as a timestamp of each tweet
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1 # decrement count because we want negative values for the max heap

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []

        # user should "follow" themselves (needed for algorithm to also include user's own posts in their feed)
        self.followMap[userId].add(userId)
        
        # initialize maxHeap
        for user in self.followMap[userId]:
            # if current user has tweets/posts
            if self.tweetMap[user]:
                index = len(self.tweetMap[user]) - 1
                count, tweetId = self.tweetMap[user][index]

                # add count, tweetId, userId of user that posted the tweet, and next index to max heap
                maxHeap.append([count, tweetId, user, index - 1])

        # heapify the heap (used to save some time complexity - more efficient than pushing k items to heap)
        heapq.heapify(maxHeap)

        # build output list
        while len(res) < 10 and maxHeap:
            count, tweetId, user, index = heapq.heappop(maxHeap)

            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweetMap[user][index]

                heapq.heappush(maxHeap, [count, tweetId, user, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)