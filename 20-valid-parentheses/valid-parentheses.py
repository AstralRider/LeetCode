class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {"}":"{", ")":"(", "]":"["}
        
        stack = []

        for char in s:
            if char not in bracketMap:
                stack.append(char)
            
            if char in bracketMap:
                if len(stack) > 0 and bracketMap[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True

    