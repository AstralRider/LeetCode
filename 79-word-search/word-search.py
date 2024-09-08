class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c, string, visited, index):
            if index == len(word):
                return True
            if r == ROWS or r < 0 or c == COLS or c < 0:
                return False
            if (r,c) in visited:
                return False
            # string comparisons are O(N)
            if word[index] != board[r][c]:
                return False
            
            visited.add((r,c))
            res = (
                dfs(r + 1, c, string, visited, index + 1)
                or dfs(r - 1, c, string, visited, index + 1)
                or dfs(r, c + 1, string, visited, index + 1)
                or dfs(r, c - 1, string, visited, index + 1)
            )
            visited.remove((r,c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, "", set(), 0):
                    return True
        return False
