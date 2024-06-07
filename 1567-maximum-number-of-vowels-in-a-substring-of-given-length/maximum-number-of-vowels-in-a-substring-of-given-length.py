class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = "aeiou"
        vowel_count = 0
        consonant_count = 0
        maxVowels = 0

        l = 0
        for r in range(len(s)):
            if s[r] in vowels:
                vowel_count += 1
            
            if (r - l) + 1 > k:
                if s[l] in vowels:
                    vowel_count -= 1
                l += 1
            
            maxVowels = max(maxVowels, vowel_count)
        
        return maxVowels
        
       #Time O(N)
       #Space O(1)

