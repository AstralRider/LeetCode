class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        def backtrack(i):
            if i == len(s):
                res.append(curr.copy())
                return
            
            for j in range(i, len(s)):
                partition = s[i:j+1]
                if self.isPalindromic(i,j,s):
                    curr.append(partition)
                    backtrack(j+1)
                    curr.pop()

        backtrack(0)
        return res
    
    def isPalindromic(self, start, end, string):
        L = start
        R = end

        while L <= R:
            if string[L] != string[R]:
                return False
            else:
                L += 1
                R -= 1
        return True
            