class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        forward = []
        backward = []
        count = 0
        res = ""

        for char in s:
            if char != '(' and char != ')':
                forward.append(char)

            elif count == 0 and char == ')':
                pass
            
            elif char == '(':
                count += 1
                forward.append(char)
            
            elif char == ")":
                count -= 1
                forward.append(char)
        
        for i in range(len(forward) -1, -1, -1):
            if count > 0 and forward[i] == '(':
                count -= 1
                continue
            else:
                backward.append(forward[i])
        
        backward.reverse(),
            
        return''.join(backward)

            


     
             