import itertools
import random


def makeBoard(dif=50):
    board = None
    while board is None:
        board = attemptBoard()
    clearRandom(board, dif)
    return board


def attemptBoard():
    n = 9
    numbers = list(range(1, n + 1))
    board = [[None for _ in range(n)] for _ in range(n)]
    for i, j in itertools.product(range(n), repeat=2):
        i0, j0 = i - i % 3, j - j % 3
        random.shuffle(numbers)
        for x in numbers:
            if (x not in board[i]
                and all(row[j] != x for row in board)
                and all(x not in row[j0:j0+3]
                        for row in board[i0:i])):
                board[i][j] = x
                break
        else:
            return None
    return board


def clearRandom(board, dif):
    attempts = dif

    while attempts > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        while board[row][col] == 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
        board[row][col] = 0
        attempts -= 1
    return board
