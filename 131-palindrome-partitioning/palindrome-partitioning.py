class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(i, ans):
            if i >= len(s):
                res.append(ans.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(i, j, s):
                    ans.append(s[i:j+1])
                    backtrack(j + 1, ans)
                    ans.pop()
        
        backtrack(0, [])
        return res

    #O(N)
    def isPalindrome(self, left, right, string):
        while left <= right:
            if string[left] != string[right]:
                return False
            else:
                left += 1
                right -= 1
        return True