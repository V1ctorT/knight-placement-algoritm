import random
import math

# =========================================
# Knight Placement Algorithm (DFS + Backtracking)
# =========================================

def create_board(size):
    """Create an NxN board initialized with zeros."""
    return [[0 for _ in range(size)] for _ in range(size)]


def max_knights(size):
    """Calculate maximum number of knights allowed."""
    return math.ceil(size / 2) * size


def count_knights(board):
    """Count knights placed on the board."""
    return sum(row.count('K') for row in board)


def count_available(board):
    """Count available positions (0) on the board."""
    return sum(row.count(0) for row in board)


def print_board(board):
    """Print the board."""
    for row in board:
        print(" ".join(map(str, row)))
    print()


def get_valid_positions(board):
    """Return all valid empty positions."""
    positions = []
    size = len(board)
    for i in range(size):
        for j in range(size):
            if board[i][j] == 0:
                positions.append((i, j))
    return positions


def place_knight(board, x, y):
    """Place a knight and mark attacked positions."""
    size = len(board)
    new_board = [row[:] for row in board]  # copy board

    new_board[x][y] = 'K'

    # Knight movement offsets
    moves = [
        (2, 2), (2, -2), (-2, 2), (-2, -2),
        (2, -2), (-2, 2), (-2, -2), (2, 2)
    ]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < size and 0 <= ny < size:
            if new_board[nx][ny] == 0:
                new_board[nx][ny] = 1

    return new_board


def dfs(board, solutions, limit):
    """Depth-First Search to find valid configurations."""
    if count_knights(board) == limit:
        solutions.append(board)
        return

    positions = get_valid_positions(board)

    for x, y in positions:
        new_board = place_knight(board, x, y)
        dfs(new_board, solutions, limit)


# =========================================
# MAIN
# =========================================

def main():
    size = int(input("Enter board size: "))
    board = create_board(size)

    solutions = []
    limit = max_knights(size)

    dfs(board, solutions, limit)

    print(f"Total solutions: {len(solutions)}")

    # Save solutions
    with open("solutions.txt", "w") as f:
        for idx, sol in enumerate(solutions, 1):
            f.write(f"Solution {idx}\n")
            for row in sol:
                f.write(f"{row}\n")
            f.write("\n")

    print("Solutions saved in 'solutions.txt'")


if __name__ == "__main__":
    main()
