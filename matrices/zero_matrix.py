from typing import List



class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(0, rows):
            for c in range(0, cols):
                if matrix[r][c] == 0:
                    # Set the first element in column -1
                    matrix[0][c] = -1
                    # Set the first element in the row -1
                    matrix[r][0] = -1
        
        for r in range(0, rows):
            if matrix[r][0] == -1:
                for c in range(0, cols):
                    if matrix[r][c] == -1:
                        continue
                    matrix[r][c] = 0
        
        for c in range(0, cols):
            if matrix[0][c] == -1:
                for r in range(0, rows):
                    matrix[r][c] = 0

        print(matrix)



sol = Solution()
sol.setZeroes([[1,1,1],[1,0,1],[1,1,1]])
sol.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])