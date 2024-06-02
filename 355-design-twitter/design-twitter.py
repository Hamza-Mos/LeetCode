class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.followerMap = defaultdict(set)
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        self.followerMap[userId].add(userId)

        # grab most recent tweet from each user that the current user follows
        for user in self.followerMap[userId]:
            if self.posts[user]:
                count, tweetId = self.posts[user][-1]

                # count, tweetId, userId, index
                heap.append([count, tweetId, user, len(self.posts[user]) - 1])

        heapq.heapify(heap)
        res = []

        while heap and len(res) < 10:
            count, tweetId, user, index = heapq.heappop(heap)
            res.append(tweetId)

            if index > 0:
                index -= 1
                count, tweetId = self.posts[user][index]
                heapq.heappush(heap, [count, tweetId, user, index])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)