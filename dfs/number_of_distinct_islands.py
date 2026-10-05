class Solution:
    def dfs(self, grid, origin):
        stack = []
        stack.append(origin)
        visited = set()

        while stack:
            curr_x, curr_y = stack.pop()
            grid[curr_x][curr_y] = -1

            if (curr_x, curr_y) in visited:
                continue

            visited.add((curr_x, curr_y))

            # left
            if curr_y - 1 >= 0 and grid[curr_x][curr_y - 1] == 1:
                stack.append((curr_x, curr_y - 1))

            if curr_y + 1 < len(grid[curr_x]) and grid[curr_x][curr_y + 1] == 1:
                stack.append((curr_x, curr_y + 1))

            if curr_x + 1 < len(grid) and grid[curr_x + 1][curr_y] == 1:
                stack.append((curr_x + 1, curr_y))

            if curr_x - 1 >= 0 and grid[curr_x - 1][curr_y] == 1:
                stack.append((curr_x - 1, curr_y))

        return visited

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        islands = set()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    found_island = self.dfs(grid, (row, col))

                    new_set = []
                    for thing in found_island:
                        curr_x, curr_y = thing
                        new_set.append((curr_x - row, curr_y - col))
                    new_set.sort()
                    islands.add(tuple(new_set))

        return len(islands)
