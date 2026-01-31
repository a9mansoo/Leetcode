from typing import List



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        found = False
        rows, cols = len(board), len(board[0])
        visited = set()
        word_length = len(word)

        def backtrack(i, row, col):
            nonlocal found
            if found:  # early exit if already found
                return
            if i == word_length:
                found = True
                return

            # boundary + visited + mismatch check
            if (
                row < 0 or col < 0 or 
                row >= rows or col >= cols or
                (row, col) in visited or 
                board[row][col] != word[i]
            ):
                return

            visited.add((row, col))

            # explore all 4 directions
            backtrack(i + 1, row - 1, col)
            backtrack(i + 1, row + 1, col)
            backtrack(i + 1, row, col - 1)
            backtrack(i + 1, row, col + 1)

            visited.remove((row, col))  # backtrack

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    backtrack(0, r, c)
                    if found:
                        return True

        return found


sol = Solution()

sol.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")