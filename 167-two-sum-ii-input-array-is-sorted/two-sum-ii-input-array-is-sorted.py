class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

      nums = numbers
      R = len(nums) - 1
      L = 0
      while L < R:
          if (nums[L] + nums[R]) > target:
              R -= 1
          elif (nums[L] + nums[R]) < target:
              L += 1
          else:
              return [L + 1, R + 1]
      