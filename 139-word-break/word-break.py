class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        cache = {}

        def dfs(i):
            if i == len(s):
                return True
            
            if i in cache:
                return cache[i]


            for word in wordDict:
                if s[i:i + len(word)] == word:
                    if dfs(i + len(word)):
                        cache[i] = True
                        return True
                    cache[i] = False

        return dfs(0)
        
