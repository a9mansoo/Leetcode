from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
        flattened = []

        for r in matrix:
            flattened.extend(r)
        
        left = 0
        right = len(flattened) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if flattened[mid] == target:
                return True
            elif flattened[mid] < target:
                left = mid + 1
            elif flattened[mid] > target:
                right = mid - 1
        return False

searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)