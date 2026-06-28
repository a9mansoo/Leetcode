grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

def numberOfIslands(grid):
    visited = set()
    count = 0


    def dfs(index):
      stack = [index]

      while stack:
          i, j = stack.pop()
          value = grid[i][j]
          if (i, j) not in visited and value == "1":
              visited.add((i, j))

              if (i - 1) >= 0 and grid[i-1][j] == "1":
                  # i - 1, j
                  stack.append((i-1, j))
              
              if (i+1) < len(grid) and grid[i+1][j] == "1":
                  # i+1, j
                  stack.append((i+1, j))

              if (j-1) >= 0 and grid[i][j-1] == "1":
                  # i, j-1
                  stack.append((i, j-1))
              
              if (j+1) < len(grid[i]) and grid[i][j+1] == "1":
                  stack.append((i, j+1))
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "1" and (i, j) not in visited:
                count += 1
                dfs((i, j))
    return count


            
def numberOfIslandsRecursive(grid):
    visited = []

    def dfs(square):
        i = square[0]
        j = square[1]

        if (i, j) in visited:
            return
        
        visited.append((i, j))

        # Now look for neighbours which are 1
        # Up
        if (i - 1) >= 0 and grid[i-1][j] == "1":
            dfs((i-1, j))

        # Down
        if (i+1) < len(grid) and grid[i+1][j] == "1":
            dfs((i+1, j))

        # Left
        if (j - 1) >= 0 and grid[i][j-1] == "1":
            dfs((i, j-1))

        # Right
        if (j + 1) < len(grid[0]) and grid[i][j+1] == "1":
            dfs((i, j+1))



    islands = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1" and (i, j) not in visited:
                islands += 1
                dfs((i, j))




count = numberOfIslands(grid)
print(count)