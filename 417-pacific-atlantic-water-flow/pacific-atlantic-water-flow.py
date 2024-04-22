class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        ROWS = len(heights)
        COLS = len(heights[0])

        def dfs(r, c, visit, prevHeight):
            if (
                (r,c) in visit
                or r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                #since we are going outside in, we flip the condition
                #we always want our previous height to be smaller than our current height
                or prevHeight > heights[r][c]):
                    return
            
            visit.add((r,c))

            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        
        pacific = set()
        atlantic = set()
        res = []

        #iterate through each value in the first and last rows to check for values that can reach them
        #if our value passes the dfs conditionals, it will be added to the respective set
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])
        
        #iterate through each value in the first and last cols to check for values that can reach them
        #if our value passes the dfs conditionals, it will be added to the respective set
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])
        
        #now check every position, if it is in both sets, it's a valid coordinate
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append((r,c))
        return res
            