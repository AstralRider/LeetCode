class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if mid - 1 >= 0 and nums[mid - 1] == nums[mid]:
                size = (mid - l + 1)
                if size % 2 == 0:
                    l = mid + 1
                else:
                    r = mid - 2

            elif mid + 1 < len(nums) and nums[mid + 1] == nums[mid]:
                size = (r - mid + 1)
                if size % 2 == 0:
                    r = mid - 1
                else:
                    l = mid + 2
            
            else:
                return nums[mid]

        #       *
        #[1,1,2,2,3]
