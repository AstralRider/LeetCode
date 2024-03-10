class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = []

        for i in range(len(position)):
          pairs.append((position[i], speed[i]))
        
        pairs.sort(reverse=True)

        for i in range(len(pairs)):
          position, speed = pairs[i]
          t = (target - position)/speed
          stack.append(t)
          if len(stack) > 1 and stack[-1] <= stack[-2]:
            stack.pop()
        return len(stack)
