class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
          slow = nums[slow]
          fast = nums[nums[fast]]
          if slow == fast:
            break

        slow2 = 0
        while True:
          slow2 = nums[slow2]
          fast = nums[fast]
          if slow2 == fast:
            return fast       
          
