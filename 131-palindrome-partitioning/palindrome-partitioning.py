class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(i, curr):
            if i >= len(s):
                res.append(curr.copy())
                return
            
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if self.isPal(i,j,s):
                    curr.append(substring)
                    backtrack(j + 1, curr)
                    curr.pop()
        
        backtrack(0, [])
        return res
    
    def isPal(self,i, j, s):
        L = i
        R = j

        while L <= R:
            if s[L] == s[R]:
                L += 1
                R -= 1
            else: 
                return False
        return True
            
    
