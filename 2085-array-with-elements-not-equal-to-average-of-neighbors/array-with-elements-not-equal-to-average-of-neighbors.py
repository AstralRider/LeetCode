class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        r = len(nums)-1
        mid = r // 2 


        first = nums[0 : mid + 1]
 
        second = nums[mid + 1: len(nums)]
  
        c = 0
        n = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = first[c]
                c += 1
            else:
                nums[i] = second[n]
                n += 1
        return nums
