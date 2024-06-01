class Solution:
    def numDecodings(self, s: str) -> int:
        
        cache = {len(s) : 1}

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                cache[i] = 0
            else:
                count = cache[i + 1]

                if (i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456'))):
                    count += cache[i + 2]
                cache[i] = count

        return cache[0]



        # def dfs(i):
        #     if i in cache:
        #         return cache[i]
            
        #     if s[i] == '0':
        #         return 0

        #     #solve the sub problem
        #     count = dfs(i + 1)

        #     if (i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456'))):

        #         count += dfs(i + 2)
        #         cache[i] = count
            
        #     return count
        
        # return dfs(0)


         

        



            
            
            
        



            
