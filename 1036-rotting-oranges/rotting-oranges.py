class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #check if there are any fresh oranges
        #check if any oranges are 4 directionally isolated
        
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = collections.deque()
        

        freshOrangeCount = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    freshOrangeCount += 1
        
        minute = -1
        if not freshOrangeCount:
            return 0 

        while queue:
             
            for i in range(len(queue)):
                r,c = queue.popleft()

                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    new_row = dr + r
                    new_col = dc + c

                    if(
                        new_row in range(ROWS)
                        and new_col  in range(COLS)
                        and grid[new_row][new_col] == 1):
                            queue.append((new_row, new_col))
                            freshOrangeCount -= 1
                            grid[new_row][new_col] = 2
                    
            minute += 1
               
        if freshOrangeCount == 0:
            return minute
        else:
            return -1
                



