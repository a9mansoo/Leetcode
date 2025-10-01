from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix)

        left = 0
        right = len(matrix[0])


        while top < bottom and left < right:
            while left < right:
                print(matrix[top][left])
                left += 1
            
            left -= 1
            top += 1
            while top < bottom:
                print(matrix[top][left])
                top += 1
            
            top -= 1
            right -= 1
            while right >= left:
                print(matrix[top][right])
                right -= 1
            
            bottom -= 1


sol = Solution()
sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])