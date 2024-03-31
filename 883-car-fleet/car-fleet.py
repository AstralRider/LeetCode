class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
      #[10, 8, 5, 3, 0]
      #[1, 1, 7, 3, 12]

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








