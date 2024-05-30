class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        length = 0
        start = 0
        end = 0

        for i in range(len(s)):
            #our substring starts with a single element
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l) + 1 > (end - start) + 1:
                    start,end = l, r
                l -= 1
                r += 1
            
            # our substring starts with 2 elements
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l) + 1 > (end - start) + 1:
                    start,end = l, r
                l -= 1
                r += 1
        return s[start:end+1]


