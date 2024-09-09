class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        #integer < 256
        #integer doesn't start with 0

        res = []

        def backtrack(i, current, dots):
            if i >= len(s) and dots == 0:
                res.append(current[:-1])
                return
            
            for j in range(i, len(s)):

                if int(s[i: j + 1]) < 256:
                    if len(s[i: j + 1]) > 1 and s[i] != '0':
                        backtrack(j + 1, current + s[i: j + 1] + '.', dots - 1)
                    
                    if len(s[i: j + 1]) == 1:
                        backtrack(j + 1, current + s[i: j + 1] + '.', dots - 1)
        
        backtrack(0, "", 4)
        return res
                    
