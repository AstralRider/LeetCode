class Solution:
    def splitString(self, s: str) -> bool:

        def dfs(i, curr):
            print(curr)
            if i >= len(s):
                return True

            for j in range(i, len(s)):
                split = s[i:j+1]
                
                #need to check the edge case where the entire string is considered
                if(len(split) == len(s)):
                    return False
                split = int(split)

                if not curr or curr[-1] == split + 1:
                    curr.append(split)

                    if dfs(j + 1, curr):
                        return True
                    curr.pop()

            return False

        return dfs(0, [])

                    
            

            
