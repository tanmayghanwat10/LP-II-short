import time


def solve(board, row, cols, ndiag, rdiag, asf, count):
    if row == len(board):
        print_solution(board, count)
        return count + 1

    for col in range(len(board[0])):
        if not cols[col] and not ndiag[row + col] and not rdiag[row - col + len(board) - 1]:
            board[row][col] = True
            cols[col] = True
            ndiag[row + col] = True
            rdiag[row - col + len(board) - 1] = True

            count = solve(board, row + 1, cols, ndiag, rdiag, asf + str(row) + "-" + str(col) + ", ", count)

            board[row][col] = False
            cols[col] = False
            ndiag[row + col] = False
            rdiag[row - col + len(board) - 1] = False

    return count


def print_solution(board, solution_num):
    print(f"Solution {solution_num}:")
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()


if __name__ == "__main__":
    n = int(input("Enter the size of the chessboard: "))
    board = [[False] * n for _ in range(n)]
    cols = [False] * n
    ndiag = [False] * (2 * n - 1)
    rdiag = [False] * (2 * n - 1)

   
