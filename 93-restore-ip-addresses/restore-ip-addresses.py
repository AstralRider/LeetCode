class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def dfs(i, dots, string):
            if i >= len(s) and dots == 4:
                res.append(string[:-1])
                return
            if dots >= 4:
                return
            
            for j in range(i,  len(s)):
                
                digits = s[i: j+1]

                if len(digits) > 1 and digits[0] == '0':
                    return False

                if int(digits) > 255:
                    return False
                
                dfs(j+1, dots +1 , string + digits + ".")

        dfs(0, 0, "")
        return res


