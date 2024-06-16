class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        cache = {len(s): True}
        for i in range(len(s)-1, -1, -1):
            cache[i] = False
            for word in wordDict:
                if i + len(word) <= len(s):
                    if word == s[i:i+len(word)]:
                        cache[i] = cache[i + len(word)]
                    if cache[i]:
                        break
        
        return cache[0]
                    



#"leetcode"
#["leet","code"]