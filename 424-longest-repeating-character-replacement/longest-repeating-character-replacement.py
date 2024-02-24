class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}

        maxValue = 0

        L = 0

        for R in range(len(s)):
          charMap[s[R]] = 1 + charMap.get(s[R], 0)
          count = max(charMap.values())
          
          if (R - L + 1) - count > k:  
            charMap[s[L]] -= 1
            L += 1
          
          else:
            maxValue = max(R - L + 1, maxValue)
        
        return maxValue
