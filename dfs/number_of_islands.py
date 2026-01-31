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


            





count = numberOfIslands(grid)
print(count)