import time


def is_safe(board, row, col, n):
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        solutions.append([row[:] for row in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, n, solutions)
            board[row][col] = 0


def solve_n_queens(n):
    solutions = []
    board = [[0] * n for _ in range(n)]
    solve_n_queens_util(board, 0, n, solutions)

    if not solutions:
        print("No solution exists")
        return False

    print(f"Total solutions found: {len(solutions)}")
    for i, solution in enumerate(solutions, start=1):
        print(f"Solution {i}:")
        for row in solution:
            print(" ".join("Q" if cell == 1 else "." for cell in row))
        print()

    return True


if __name__ == "__main__":
    n = int(input("Enter the size of the chessboard: "))

    start_time = time.time()
    solve_n_queens(n)
    end_time = time.time()

    print(f"Time taken: {end_time - start_time:.4f} seconds")
