class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        L = 0 
        R = len(nums) - 1

        while L <= R:
          mid = (L + R) // 2

          if nums[mid] == target:
            return mid
          
          #mid belongs to left
          if nums[L] <= nums[mid]:
            if target < nums[L] or target > nums[mid]:
              L = mid + 1
            else:
              R = mid - 1
          
          #mid belongs to right
          else:
            if target < nums[mid] or target > nums[R]:
              R = mid - 1
            else:
              L = mid + 1
        
        return - 1
