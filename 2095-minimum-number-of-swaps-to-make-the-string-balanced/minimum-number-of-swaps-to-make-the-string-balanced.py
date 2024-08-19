class Solution:
    def minSwaps(self, s: str) -> int:
        maxCount = 0
        count = 0
        for char in s:
            
            if char == ']':
                count += 1
            else:
                count -= 1
            
            maxCount = max(maxCount, count)
        
        #We divide by 2 since a single swap fixes 2 unmatched brackets.
        return (maxCount + 1) //2
                

