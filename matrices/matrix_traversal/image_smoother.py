import math
from typing import List

class Solution:

    def calculateCellAverage(self, pos, val, grid):
        x, y = pos
        number_of_neighbours = 0
        sum_of_cells = 0

        #print(f"Evaluating cell: x: {x} y: {y} val: {val}")
        # left
        if (y-1) >= 0:
            #print(f"Left value: x: {x} y: {y-1}")
            sum_of_cells += grid[x][y-1]
            number_of_neighbours += 1
        # right
        if (y+1) < len(grid[0]):
            #print(f"Right value x: {x} y: {y+1}")
            sum_of_cells += grid[x][y+1]
            number_of_neighbours += 1
        # up
        if (x-1) >= 0:
            #print(f"Up value x: {x-1} y: {y}")
            sum_of_cells += grid[x-1][y]
            number_of_neighbours += 1
        # down
        if (x+1) < len(grid):
            #print(f"Down value x: {x+1} y: {y}")
            sum_of_cells += grid[x+1][y]
            number_of_neighbours += 1
        # left diag
        if (x+1) < len(grid) and (y-1) >= 0:
            #print(f"Left diag x: {x+1} y: {y-1}")
            sum_of_cells += grid[x+1][y-1]
            number_of_neighbours += 1
        # right diag
        if (x+1) < len(grid) and (y+1) < len(grid[0]):
            #print(f"Right diag x: {x+1} y: {y+1}")
            sum_of_cells += grid[x+1][y+1]
            number_of_neighbours += 1
        # up diag
        if (x-1) >= 0 and (y-1) >= 0:
            #print(f"Up diag x: {x-1} y: {y-1}")
            sum_of_cells += grid[x-1][y-1]
            number_of_neighbours += 1
        # down diag
        if (x-1) >= 0 and (y+1) < len(grid[0]):
            #print(f"Down diag x: {x-1} y: {y+1}")
            sum_of_cells += grid[x-1][y+1]
            number_of_neighbours += 1

        average_value = math.floor((val+sum_of_cells)/(number_of_neighbours + 1))
        return average_value

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])
        new_grid = [[0 for _ in range(cols)] for _ in range(rows)]
        
        for row in range(len(img)):
            for col in range(len(img[row])):
                cellAvg = self.calculateCellAverage((row, col), img[row][col], img)
                new_grid[row][col] = cellAvg
        return new_grid
