class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)):
          if not stack:
            stack.append((i, temperatures[i]))
          else:
            while stack and temperatures[i] > stack[-1][1]:
              idx, temp = stack.pop()
              res[idx] = i - idx
            stack.append((i, temperatures[i]))
        
        return res


