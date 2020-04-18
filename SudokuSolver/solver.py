from math import sqrt


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):

    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    x = int(sqrt(len(bo[0])))
    y = int(sqrt(len(bo)))

    box_x = pos[1]//x
    box_y = pos[0]//y

    for i in range(box_y * x, box_y*x + x):
        for j in range(box_x * y, box_x*y + y):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(bo):
    print()
    x = int(sqrt(len(bo[0])))
    y = int(sqrt(len(bo)))
    for i in range(len(bo)):
        if i % y == 0 and i != 0:
            print("-----------------------")
        for j in range(len(bo[0])):
            if j % x == 0 and j != 0:
                print(" |", end='')

            if j == (len(bo[0])-1):
                print(" " + str(bo[i][j]))
            else:
                print(" " + str(bo[i][j]), end='')


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return(i, j)
    return None

