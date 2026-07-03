board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]

def is_cell_alive(cell_value):
        if abs(cell_value) == 1:
            return True
        return False
    
def check_neighbours(cell_value, alive_neighbours):
    if is_cell_alive(cell_value):
        if alive_neighbours < 2:
            return -1
        elif alive_neighbours == 2 or alive_neighbours == 3:
            return 1
        elif alive_neighbours > 3:
            return -1
    else:
        if alive_neighbours == 3:
            return 2
    return cell_value


rows = len(board)
cols = len(board[0])

for i in range(len(board)):
    for j in range(len(board[i])):
        right = j + 1
        left = j - 1
        up = i - 1
        down = i + 1

        alive_neighbours = 0

        if right < cols:
            neighbour_val = board[i][right]
            if is_cell_alive(neighbour_val):
                alive_neighbours += 1

        if left >= 0:
            neighbour_val = board[i][left]
            if is_cell_alive(neighbour_val):
                alive_neighbours += 1
        
        if up >= 0:
            neighbour_val = board[up][j]
            if is_cell_alive(neighbour_val):
                alive_neighbours += 1
        
        if down < rows:
            neighbour_val = board[down][j]
            if is_cell_alive(neighbour_val):
                alive_neighbours += 1
        
        if (i - 1) >= 0 and (j - 1) >= 0:
            neighbour_val = board[i-1][j-1]
            if is_cell_alive(neighbour_val):
                alive_neighbours += 1
        
        if (i - 1) >= 0 and (j + 1) < cols:
            neighbour_val = board[i-1][j+1]
            if is_cell_alive(neighbour_val):
                alive_neighbours += 1

        if (i + 1) < rows and (j - 1) >= 0:
            neighbour_val = board[i+1][j-1]
            if is_cell_alive(neighbour_val):
                alive_neighbours += 1
        
        if (i + 1) < rows and (j + 1) < cols:
            neighbour_val = board[i+1][j+1]
            if is_cell_alive(neighbour_val):
                alive_neighbours += 1
        
        board[i][j] = check_neighbours(board[i][j], alive_neighbours)


for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == -1:
            board[i][j] = 0
        elif board[i][j] == 2:
            board[i][j] = 1


print(board)
