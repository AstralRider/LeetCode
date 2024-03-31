class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = [(0, 30)]

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
              idx, temp = stack.pop()
              res[idx] = i - idx
            stack.append((i, temperatures[i]))
        
        return res


