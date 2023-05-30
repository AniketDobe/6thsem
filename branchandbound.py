class NQueensProblem:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n
        self.solution = []

    def solve(self):
        self._solve_util(0)

    def _solve_util(self, col):
        if col == self.n:
            self.solution.append(self.board[:])
            return True

        for row in range(self.n):
            if self._is_safe(row, col):
                self.board[col] = row
                if self._solve_util(col + 1):
                    return True
                self.board[col] = -1

        return False

    def _is_safe(self, row, col):
        for i in range(col):
            if (
                self.board[i] == row or
                self.board[i] == row - (col - i) or
                self.board[i] == row + (col - i)
            ):
                return False
        return True


def solve_n_queens(n):
    problem = NQueensProblem(n)
    problem.solve()
    return problem.solution


# Example usage:
n = 4
solutions = solve_n_queens(n)
for solution in solutions:
    print(solution)
