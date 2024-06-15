class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def dfs(i, cache):
            if i in cache:
                return cache[i]

            if i == len(s):
                return True

            

            for word in wordDict:
                length = len(word)
               
                if s[i:i + length] == word:
                    if dfs(i + length, cache):
                        cache[i] = True
                        return True
                    
            cache[i] = False
            return False
                        
        return dfs(0, {})