class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        res = []
        
        i = 0

        for num in pushed:
            res.append(num)
            while i < len(pushed) and res and res[-1] == popped[i]:
                res.pop()
                i += 1
        
        if i < len(pushed):
            return False
        else:
            return True
    
    

        





            

