class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top = 0
        bottom = ROWS - 1
        #perform binary search on nested arrays to find the array that may contain target
        #1.check if target > last index in middle array
        #2.check if target < first index in middle array
        #3.adjust array being searched accordingly
        while top <= bottom:
          row = (top + bottom) // 2
          if target > matrix[row][-1]:
            top = row + 1
          elif target < matrix[row][0]:
            bottom = row - 1
          else:
            break

        #can have a case where top > bottom
        # if not top <= bottom:
        #   return False
        #regular array binary search
        
        left = 0
        right = COLS - 1
        while left <= right:
          mid = (left + right) // 2
          if target > matrix[row][mid]:
            left = mid + 1
          elif target < matrix[row][mid]:
            right = mid - 1
          else:
            return True
        return False
            