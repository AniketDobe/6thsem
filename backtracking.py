def is_safe(board, row, col, n):
    # Check if a queen can be placed at board[row][col]
  
    # Check left row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_n_queens_util(board, col, n):
    # Base case: All queens have been placed
    if col >= n:
        return True

    # Try placing a queen in each row of the current column
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1  # Place the queen

            # Recursively place queens in the remaining columns
            if solve_n_queens_util(board, col + 1, n):
                return True

            # Backtrack if placing the queen leads to an invalid solution
            board[i][col] = 0

    return False


def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]

    if solve_n_queens_util(board, 0, n):
        # Print the solution
        for row in board:
            print(' '.join(map(str, row)))
    else:
        print(f"No solution exists for n = {n}")


# Example usage
n = 4
solve_n_queens(n)
