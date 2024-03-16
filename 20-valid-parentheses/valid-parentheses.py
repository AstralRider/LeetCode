class Solution:
    def isValid(self, s: str) -> bool:
      stack = []
      
      bracketsMap = {")": "(", "]": "[", "}":"{"}

      for bracket in s:
        if bracket not in bracketsMap:
          stack.append(bracket)
        else:
          if not stack or bracketsMap[bracket] != stack[-1]:
            return False
          else:
            stack.pop()

      if not stack:
        return True
      else:
        return False 

