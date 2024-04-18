class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.length = 0

        def backtrack(i, string):
            if i >= len(arr):
                if len(string) == len(set(string)):
                    self.length = max(self.length, len(string))
                return
            
            backtrack(i + 1, string + arr[i])

            backtrack(i + 1, string)
        
        backtrack(0, "")

        return self.length
    
