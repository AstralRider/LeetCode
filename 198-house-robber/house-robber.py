class Solution:
    def rob(self, nums: List[int]) -> int:
        h1 = 0
        h2 = 0

        for n in nums:
            tmp = max(h1 + n, h2)
            h1 = h2
            h2 = tmp
        return h2

        