class Solution:
    def partition(self, s: str) -> List[List[str]]:
      res = []
      string = []
      def dfs(index):
        if index >= len(s):
          res.append(string.copy())
          return

        for j in range(index, len(s)):
          if self.isPalindrome(s, index, j):
            string.append(s[index : j+1])
            dfs(j + 1)
            string.pop()
        
      dfs(0)
      return res
        
    def isPalindrome(self, s, start, end):
      L = start
      R = end
      
      while L < R:
        if s[L] == s[R]:
          L += 1
          R -=1
        else:
          return False
      return True

          

          
