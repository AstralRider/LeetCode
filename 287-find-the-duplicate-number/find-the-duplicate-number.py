class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = 0
        fast = 0

        #this is ok because problem guarantees duplicate value
        #basically checking for a cycle
        while True:
          slow = nums[slow]
          fast = nums[nums[fast]]
          if slow == fast:
            break
        
        #trying to find head of cycle
        #head of list to head of cycle distance = intersection point of fast&slow to head of cycle
        slow1 = 0
        while True:
          slow1 = nums[slow1]
          slow = nums[slow]
          if slow1 == slow:
            return slow1