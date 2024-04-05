class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.word = word
        self.ROWS = len(board)
        self.COLS = len(board[0])
        for r in range(self.ROWS):
          for c in range(self.COLS):
            if self.backtrack(0, r, c, board, []):
              return True
        return False

    def backtrack(self, index, r, c, board, search):
      if index == len(self.word):
        return True
      if r < 0 or r == self.ROWS:
        return False
      if c < 0 or c == self.COLS:
        return False
      if (r,c) in search:
        return False
      if self.word[index] != board[r][c]:
        return False
      
      search = search[:]
      search.append((r, c))
      
      return (
      self.backtrack(index + 1, r + 1, c, board, search) or
      self.backtrack(index + 1, r - 1, c, board, search) or
      self.backtrack(index + 1, r, c + 1, board, search) or
      self.backtrack(index + 1, r, c - 1, board, search)
      )




      
      