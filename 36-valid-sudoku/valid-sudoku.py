import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #use a dict + set to keep a list of values at each row, col and square
        #example: {0: (1,2,3,4), 1: (1,2,3,4)}
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for r in range(9):
          for c in range(9):
            if board[r][c] == '.':
              continue
            elif (
            #check if val in a particular row set
            board[r][c] in rows[r]
            #check if val in a particular col set
            or board[r][c] in cols[c]
            #check if val in a particular square set 
            or board[r][c] in square[(r // 3 , c // 3)]):
              return False
            else:
              rows[r].add(board[r][c])
              cols[c].add(board[r][c])
              square[(r // 3, c //3)].add(board[r][c])
        return True
