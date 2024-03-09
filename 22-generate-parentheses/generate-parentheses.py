class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
      
      res = []

      def recur(current, openP, closedP):
        if openP == closedP == n:
          res.append(current)
        
        #add an opening bracket since starting with a closed bracket is never valid
        if openP < n:
          recur(current + "(", openP + 1, closedP)
        
        #as long as there are more open brackets than closed brackets, adding a closed bracket is always valid
        if closedP < openP:
          recur(current + ")", openP, closedP + 1)
      
      recur("", 0, 0)
      return res

        
      

    