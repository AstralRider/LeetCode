class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

      pairs = []
      stack = []

      for i in range(len(position)):
          pairs.append((position[i], speed[i]))
      
      pairs.sort(reverse=True)

      for pos, spd in pairs:
        time = (target - pos) / spd

        if not stack:
          stack.append(time)

        if stack and time > stack[-1]:
          stack.append(time)
      
      return len(stack)








