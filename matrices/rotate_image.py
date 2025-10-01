from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # square matrix:
        n = len(matrix)
        # Convert rows to columns
        for r in range(n):
            for c in range(n):
                if r <= c:
                    temp = matrix[r][c]
                    matrix[r][c] = matrix[c][r]
                    matrix[c][r] = temp
        

        for r in range(n):
            matrix[r].reverse()
        print(matrix)


sol = Solution()
sol.rotate([[1,2,3],[4,5,6],[7,8,9]])

