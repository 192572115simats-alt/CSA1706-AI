def solve(board, row, n):
    if row == n:
        for r in board:
            print(" ".join(r))
        return True

    for col in range(n):
        if safe(board, row, col, n):
            board[row][col] = "Q"

            if solve(board, row + 1, n):
                return True

            board[row][col] = "."

    return False


def safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


n = 4
board = [["."] * n for _ in range(n)]

if not solve(board, 0, n):
    print("No solution")
