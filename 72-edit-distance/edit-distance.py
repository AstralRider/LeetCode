class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
    
        cache = [ [float("inf")] * (len(word2)) for _ in range(len(word1))]

        def dfs(word1, word2, i1, i2):
            if i1 == len(word1) and i2 == len(word2):
                return 0
            
            if i1 == len(word1) and i2 < len(word2):
                return len(word2) - i2
            
            if i1 < len(word1) and i2 == len(word2):
                return len(word1) - i1
            
            if cache[i1][i2] != float("inf"):
                return cache[i1][i2]
            
            if word1[i1] == word2[i2]:
                cache[i1][i2] = dfs(word1, word2, i1+1, i2+1)
                return cache[i1][i2]
            else:
                cache[i1][i2] = min(1 + dfs(word1, word2, i1+1, i2), 1 + dfs(word1, word2, i1, i2 + 1), 1 + dfs(word1, word2, i1+1, i2+1))
                return cache[i1][i2]
        
        return dfs(word1, word2, 0, 0)


