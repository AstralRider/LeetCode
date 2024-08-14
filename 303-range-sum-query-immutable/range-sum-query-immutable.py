class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        total = 0
        for n in nums:
            total += n
            self.prefix_sum.append(total)

    def sumRange(self, left: int, right: int) -> int:
        preLeft = left
        preRight = right
        if left == 0:
            return self.prefix_sum[preRight]
        else:
            preLeft = left - 1
        return (self.prefix_sum[preRight] - self.prefix_sum[preLeft])
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)