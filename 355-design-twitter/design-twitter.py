from collections import defaultdict
class Twitter:

    def __init__(self):
      self.followers = defaultdict(set)
      self.tweets = defaultdict(list)
      self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
      self.tweets[userId].append([self.count,tweetId])
      self.count -= 1 #for the max heap to work

        

    def getNewsFeed(self, userId: int) -> List[int]:
      minHeap = []
      feed = []

      self.followers[userId].add(userId) #set user to follow themselves
      for followerId in self.followers[userId]:
        if followerId in self.tweets:
          index = len(self.tweets[followerId]) - 1
          count, tweetId = self.tweets[followerId][index]
          heapq.heappush(minHeap, [count, tweetId, followerId, index - 1])
      
      while minHeap and len(feed) < 10:
        count, tweetId, followerId, index = heapq.heappop(minHeap)
        feed.append(tweetId)

        if index >= 0:
          count, tweetId = self.tweets[followerId][index]
          heapq.heappush(minHeap, [count, tweetId, followerId, index - 1])
      
      return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
      if followeeId in self.followers[followerId]:
        self.followers[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)