class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        L = 0
        maxLength = 0

        for R in range(len(s)):
          while s[R] in charSet:
            charSet.remove(s[L])
            L += 1
          
          maxLength = max((R - L)+ 1, maxLength)

          charSet.add(s[R])
        
        return maxLength

