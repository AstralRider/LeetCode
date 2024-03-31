class Solution:
    def findMin(self, nums: List[int]) -> int:
    
      res = float("inf")

      L = 0
      R = len(nums) - 1

      while L <= R:
        mid = (L + R) // 2

        if nums[L] < nums[R]:
          res = min(nums[L], res)
          break
        
        res = min(nums[mid], res)

        #key condition for all rotated sorted array problems nums[L] <= nums[mid]
        if nums[L] <= nums[mid]:
          L = mid + 1
        else:
          R = mid - 1

      return res
      



