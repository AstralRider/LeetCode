class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        cache = [[-1] * len(text2) for _ in range(len(text1))]
        
        
        def helper(text1, text2, i1, i2, cache):
            if i1 == len(text1) or i2 == len(text2):
                return 0
            if cache[i1][i2] != -1:
                return cache[i1][i2]
            
            if text1[i1] == text2[i2]:
                cache[i1][i2] = 1 + helper(text1, text2, i1 + 1, i2+1, cache)
                return cache[i1][i2]
            else:
                cache[i1][i2] = max(helper(text1, text2, i1 + 1, i2, cache), helper(text1, text2, i1, i2 + 1, cache))
                return cache[i1][i2]
        
        return helper(text1, text2, 0, 0, cache)