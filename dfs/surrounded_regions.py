board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]


def dfs(grid, pos):
    stack = []
    stack.append((pos[0], pos[1]))
    region = set()
    set_region = True

    while stack:
        pos = stack.pop()
        i = pos[0]
        j = pos[1]

        if (i, j) in region:
            continue

        left = j - 1
        right = j + 1
        up = i - 1
        down = i + 1

        region.add((i, j))

        if (left > 0) and grid[i][left] == "O":
            stack.append((i, left))
        
        if right < (len(grid[i]) - 1) and grid[i][right] == "O":
            stack.append((i, right))
        
        if (up > 0) and grid[up][j] == "O":
            stack.append((up, j))
        
        if down < (len(grid[i]) - 1) and grid[down][j] == "O":
            stack.append((down, j))
        
        if (left == 0) and grid[i][left] == "O":
            set_region = False
            break

        if (right == (len(grid[i]) - 1)) and grid[i][right] == "O":
            set_region = False
            break

        if (up == 0) and grid[up][j] == "O":
            set_region = False
            break

        if (down == (len(grid[i]) - 1)) and grid[down][j] == "O":
            set_region = False
            break
    
    if set_region and region:
        for reg in region:
            i = reg[0]
            j = reg[1]
            grid[i][j] = "X"


def surroundRegion(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'O' and (i != 0) and (j != 0) and (j != len(board[i]) - 1) and (i != len(board) - 1):
                dfs(board, (i, j))


def dfs2(grid, pos):
    pass


def surroundedRegion2(board):
    pass