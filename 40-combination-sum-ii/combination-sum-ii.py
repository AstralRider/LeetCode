class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combinations = []
        self.helper(0, [], combinations, candidates, target, 0)
        return combinations

    def helper(self, i, curSet, combinations, candidates, target, total):
      if total == target:
        combinations.append(curSet[:])
        return

      elif i == len(candidates) or total > target:
        return
      
      curSet.append(candidates[i])
      self.helper(i + 1, curSet, combinations, candidates, target, total + candidates[i])
      
      curSet.pop()

      while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
        i += 1
      self.helper(i + 1, curSet, combinations, candidates, target, total)

