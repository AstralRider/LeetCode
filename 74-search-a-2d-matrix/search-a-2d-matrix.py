class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0 
        bottom = len(matrix) - 1

        while top <= bottom:
            mid = (top + bottom) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                break


        l = 0
        r = len(matrix[mid]) - 1
        arr = matrix[mid]

        while l <= r:
            m = (l + r) // 2
            if target < arr[m]:
                r = m - 1
            elif target > arr[m]:
                l = m + 1
            else:
                return True
        return False
        






