class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {")": "(", "]": "[", "}": "{"}
        stack  = []

        for bracket in s:
            if bracket not in bracketMap:
                stack.append(bracket)
            else:
                if not stack or stack[-1] != bracketMap[bracket]:
                    return False
                stack.pop()

        return len(stack) == 0