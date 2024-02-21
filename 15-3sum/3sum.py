class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #sort array first
        nums.sort()
        res = []

        for i in range(len(nums)):

          #check for a duplicate value
          if i > 0 and nums[i] == nums[i-1]:
            continue

          #left and right pointers
          L = i + 1
          R = len(nums) - 1

          #basically 2sum sorted
          while L < R:
            threeSum = nums[i] + nums[L] + nums[R]

            if threeSum > 0:
              R -= 1
            elif threeSum < 0:
              L += 1
            else:
              res.append([nums[i], nums[L], nums[R]])
              L += 1
              R -= 1
              #handle duplicate Left values to ensure we don't duplicate answers
              while nums[L] == nums[L - 1] and L < R:
                L += 1
        return res