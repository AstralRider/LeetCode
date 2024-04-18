class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.length = 0

        def backtrack(i, string):
            if i >= len(arr):
                if self.checkUnique(string):
                    self.length = max(self.length, len(string))
                return

            backtrack(i + 1, string + arr[i])

            backtrack(i + 1, string)
        
        backtrack(0, "")

        return self.length
    
    def checkUnique(self, string):
        chars = set()

        for s in string:
            if s in chars:
                return False
            chars.add(s)
        return True
