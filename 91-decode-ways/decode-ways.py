class Solution:
    def numDecodings(self, s: str) -> int:

        cache = {len(s): 1}

        def dfs(i, cache):
            if i in cache:
                return cache[i]
            
            if s[i] == '0':
                return 0

            res = dfs(i+1, cache)
            
            if i + 1 < len(s):
                if s[i] =='1' or (s[i] == '2' and s[i+1] in '0123456'):
                    # we consider i and i+1 as a valid pairing and are adding the number after it
                    # to determine how many ways i can be decoded
                    res += dfs(i + 2, cache)
            cache[i] = res
            return cache[i]
        
        return dfs(0, cache)

            #         2 1 1
            #"1 2 0 1 2 3 4"

         

        



            
            
            
        



            
