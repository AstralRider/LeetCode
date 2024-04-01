class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        curCom = []
        self.helper(0, 0, combinations, curCom, candidates, target)
        return combinations

    def helper(self, index, curSum, combinations, curCom, candidates, target):
      if curSum == target:
        combinations.append(curCom.copy())
        return
      elif curSum > target:
        return
      elif index == len(candidates):
        return
      curCom.append(candidates[index])

      self.helper(index, curSum + candidates[index], combinations, curCom, candidates, target)
      curCom.pop()
    
      self.helper(index + 1, curSum, combinations, curCom, candidates, target)
