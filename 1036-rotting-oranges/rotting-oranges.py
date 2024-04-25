class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #check if there are any fresh oranges
        #check if any oranges are 4 directionally isolated
        
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = collections.deque()
        
        visited = set()

        freshOrangeCount = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                    visited.add((r,c))
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
                        new_row not in range(ROWS)
                        or new_col not in range(COLS)
                        or new_row < 0
                        or new_col < 0
                        or (new_row, new_col) in visited
                        or grid[new_row][new_col] != 1):
                            continue
                    
                    queue.append((new_row, new_col))
                    freshOrangeCount -= 1
                    visited.add((new_row, new_col))

            minute += 1
        
        print(minute, freshOrangeCount)
        
        if freshOrangeCount == 0:
            return minute
        else:
            return -1
                



