


def exists(board, word):


    def backtrack(i, board, curr_col, curr_row, visited):
        if i == len(word):
            return True

        if curr_col >= len(board[0]) or curr_col < 0:
            return False

        if curr_row >= len(board) or curr_row < 0:
            return False

        if word[i] != board[curr_row][curr_col]:
            return False

        if (curr_row, curr_col) in visited:
            return False

        visited.add((curr_row, curr_col))
        found = (
            backtrack(i+1, board, curr_col + 1, curr_row, visited) or
            backtrack(i+1, board, curr_col, curr_row + 1, visited) or
            backtrack(i+1, board, curr_col - 1, curr_row, visited) or
            backtrack(i+1, board, curr_col, curr_row - 1, visited)
        )

        visited.remove(curr_row, curr_col)
        return found

    for i in range(len(board)):
        visited = set()
        for j in range(len(board[i])):
            if backtrack(0, board, j, i, visited):
                return True
    return False
