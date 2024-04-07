class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []
        def dfs(i):
            if i >= len(s):
                res.append(curr.copy())
                return
          
            for j in range(i, len(s)):
                if self.isPal(i, j, s):
                    curr.append(s[i: j + 1])
                    dfs(j + 1)
                    curr.pop()
        
        dfs(0)
        return res
    
    def isPal(self, L, R, string):

        while L <= R:
            if string[L] != string[R]:
                return False
            else:
                L += 1
                R -= 1
        return True
    
          
    
