class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        
        pos = []
        neg = []
        res = []

        for n in nums:
            if n < 0:
                neg.append(n)
            else:
                pos.append(n)
        
        i = 0
        while i < len(pos):
            res.append(pos[i])
            res.append(neg[i])
            i += 1
        return res
        
