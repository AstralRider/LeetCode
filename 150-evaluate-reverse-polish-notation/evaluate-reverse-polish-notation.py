class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
          if token == "+":
            stack.append(stack.pop() + stack.pop())
          elif token == "-":
            lastVal = stack.pop()
            secondLastVal = stack.pop()
            stack.append(secondLastVal - lastVal)
          elif token == "*":
            stack.append(stack.pop() * stack.pop())
          elif token == "/":
            lastVal = stack.pop()
            secondLastVal = stack.pop()
            stack.append(int(secondLastVal / lastVal))
          else:
            stack.append(int(token))
        return stack[0]