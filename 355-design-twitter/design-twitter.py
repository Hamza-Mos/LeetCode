class Twitter:

    def __init__(self):
        self.time = 0 # keeps track of post times for tweets
        self.userMap = collections.defaultdict(set) # keeps track of followees for each user
        
        self.postMap = collections.defaultdict(list) # maps a user id to their posts

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postMap[userId].append([tweetId, self.time])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        posts = []

        self.userMap[userId].add(userId) # user should be able to see their own posts (their own follower)

        for user in self.userMap[userId]:
            if not self.postMap[user]:
                continue

            tweetId, time = self.postMap[user][-1] # most recent post
            posts.append([time, tweetId, user, len(self.postMap[user]) - 1]) # time, tweetId, user, index

        heapq.heapify(posts)
        res = []

        while posts and len(res) < 10:
            time, tweetId, user, index = heapq.heappop(posts)
            res.append(tweetId)

            if index - 1 >= 0:
                tweetId, time = self.postMap[user][index - 1]
                heapq.heappush(posts, [time, tweetId, user, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userMap[followerId]:
            self.userMap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)