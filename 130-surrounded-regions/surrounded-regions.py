class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r,c):
            if(
                r < 0
                or c < 0
                or c >= COLS
                or r >= ROWS
                or board[r][c] == "T"
                or board[r][c] == "X"):
                    return

            board[r][c] = "T"
        
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        #similar to pacific atlantic water flow
        #dfs from borders inwards, and O's connected to border O's are changed to T's
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS-1, c)
        
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        
        #every O connected to the border or adjacent to an O connected to a border is now a T
        #turn remaining O's to X's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                    
        #turn T's back to X's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
        
        return board
        
        

