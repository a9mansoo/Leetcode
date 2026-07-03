from collections import deque

grid = [[1,2]]


""" 
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
"""

total_rows = len(grid)
total_cols = len(grid[0])

class CELL_STATES:
    EMPTY = 0
    FRESH_ORANGE = 1
    ROTTEN_ORANGE = 2



def rotting_orange(grid):
    q = deque()
    total_rows = len(grid)
    total_cols = len(grid[0])
    fresh_oranges = 0

    for i in range(total_rows):
        for j in range(total_cols):
            if grid[i][j] == 1:
                fresh_oranges += 1
            elif grid[i][j] == 2:
                q.append((i, j, 2))

    print(fresh_oranges)

    timeframe = 0
    while q:
        changed = False

        for _ in range(len(q)):
            curr_cell = q.popleft()
            i = curr_cell[0]
            j = curr_cell[1]
            value = curr_cell[2]

            if value != 2:
                continue

            left = j - 1
            right = j + 1
            up = i - 1
            down = i + 1

            if left >= 0 and grid[i][left] == 1:
                grid[i][left] = 2
                changed = True
                fresh_oranges -= 1
                q.append((i, left, 2))
            
            if right < total_cols and grid[i][right] == 1:
                grid[i][right] = 2
                changed = True
                fresh_oranges -= 1
                q.append((i, right, 2))
            
            if up >= 0 and grid[up][j] == 1:
                grid[up][j] = 2
                changed = True
                fresh_oranges -= 1
                q.append((up, j, 2))
            
            if down < total_rows and grid[down][j] == 1:
                grid[down][j] = 2
                changed = True
                fresh_oranges -= 1
                q.append((down, j, 2))
        
        if changed:
            timeframe += 1
    
    print(fresh_oranges)
    return timeframe if fresh_oranges == 0 else -1


rotting_orange(grid)




