class Solution:
    def isPathCrossing(self, path: str) -> bool:
        path_points = set()
        curr_x, curr_y = 0,0

        path_points.add((curr_x, curr_y))

        for part in path:
            if part == "N":
                curr_y += 1
            elif part == "S":
                curr_y -= 1
            elif part == "E":
                curr_x += 1
            elif part == "W":
                curr_x -= 1
            
            if (curr_x, curr_y) in path_points:
                return True
            path_points.add((curr_x, curr_y))
        return False
