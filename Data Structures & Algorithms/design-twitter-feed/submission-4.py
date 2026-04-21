class Twitter:

    def __init__(self):
        # self.tweetIDs = set()
        self.userIDs = set()
        self.news = {}
        self.following = {}
        self.followed = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        import heapq
        if userId not in self.userIDs:
            self.userIDs.add(userId)
            self.following[userId] = []
            self.news[userId] = []

        self.news[userId].append(-tweetId)
        heapq.heapify(self.news[userId])
        print(f"postTweet user {userId} posted {tweetId}")
        
    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.userIDs and userId not in self.following[userId]:
            print(f"getNewsFeed {userId} null")
            return []
        else:
            ans = []
            k = 10
            tweets = self.news[userId].copy()
            while tweets and k > 0:
                ans.append(-1 * heapq.heappop(tweets))
                k-= 1
            print(f"getNewsFeed {userId} feed {ans}")
            del tweets
            return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userIDs:
            print(f"{followerId} created")
            self.userIDs.add(followerId)
            self.following[followerId] = []
        if followeeId not in self.userIDs:
            print(f"{followeeId} created")
            self.userIDs.add(followeeId)
            self.following[followeeId] = []
        if followerId in self.userIDs and followeeId in self.userIDs \
            and followeeId not in self.following[followerId]:
            print(f"{followerId} follow {followeeId}")
            self.following[followerId].append(followeeId)

            followee_feed = self.news[followeeId].copy()
            follower_feed = self.news[followerId].copy()
            while followee_feed:
                pop = heapq.heappop(followee_feed)
                heapq.heappush(follower_feed, pop)
            heapq.heapify(follower_feed)
            self.news[followerId] = follower_feed


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.userIDs and followeeId in self.userIDs \
            and followeeId in self.following[followerId]:
            print(f"{followerId} unfollow {followeeId}")
            self.following[followerId].remove(followeeId)

            followee_feed = self.news[followeeId].copy()
            followee_posted = set()
            follower_feed = self.news[followerId].copy()
            follower_feed_new = []
            while followee_feed:
                followee_posted.add(heapq.heappop(followee_feed))
            while follower_feed:
                pop = heapq.heappop(follower_feed)
                if pop not in followee_posted:
                    follower_feed_new.append(pop)
            heapq.heapify(follower_feed_new)
            self.news[followerId] = follower_feed_new

            


        
