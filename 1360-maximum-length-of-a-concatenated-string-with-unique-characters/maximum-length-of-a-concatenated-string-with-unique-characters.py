class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.length = 0
        
        def backtrack(i, chars):
            if i == len(arr):
                self.length = max(self.length, len(chars))
                return
            
            if len(set(arr[i])) == len(arr[i]):  # Check if current string has no duplicates
                for c in arr[i]:
                    if c in chars:
                        break
                else:
                    backtrack(i + 1, chars | set(arr[i]))
            
            backtrack(i + 1, chars)
        
        backtrack(0, set())
        return self.length
    
    def checkUnique(self, string):
        chars = set()

        for s in string:
            if s in chars:
                return False
            chars.add(s)
        return True
