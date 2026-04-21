class Twitter:
    from collections import defaultdict
    import heapq
    def __init__(self):
        # self.tweetIDs = set()
        self.time = 0
        self.news = defaultdict(list)
        self.following = defaultdict(set)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        
        self.news[userId].append([self.time, tweetId])
        self.time -= 1
        print(f"postTweet user {userId} posted {tweetId} at {self.time}")
        
    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        minHeap = []

        k = 10
        # my feed contains my post
        self.following[userId].add(userId)
        # 1 latest tweet per followee into the heap at first (efficient concerns)
        for following in self.following[userId]:
            if following in self.news:
                following_last_posted = len(self.news[following]) - 1
                time, tweetId = self.news[following][following_last_posted]
                heapq.heappush(minHeap, [time, tweetId, following, following_last_posted - 1])
        # pop each latest tweet, if this is not the last, add next latest to minHeap
        while minHeap and len(ans) < 10:
            time, tweetId, following, following_last_posted = heapq.heappop(minHeap)
            ans.append(tweetId)
            if following_last_posted >= 0:
                time, tweetId = self.news[following][following_last_posted]
                heapq.heappush(minHeap, [time, tweetId, following, following_last_posted -1])
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)