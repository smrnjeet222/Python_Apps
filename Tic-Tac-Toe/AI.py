import random
import os

os.system("cls")

board = [' ']*10


def insertBoard(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le))


def playerMove():
    run = True
    while run:
        move = input("\n>>> Please select a position to place an 'X' (1_9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertBoard('X', move)
                else:
                    print('\n--- This postion is already occupied!')
            else:
                print('\n--- Please type a number within the range!')
        except:
            print("\n--- Please type a number!")


def selectRandom(li):
    r = random.randrange(0, len(li))
    return li[r]


def compMove():
    possibleMoves = [x for x, le in enumerate(board) if le == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            d_board = board[:]
            d_board[i] = let
            if isWinner(d_board, let):
                move = i
                return move
    cornerOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornerOpen.append(i)
        if len(cornerOpen) > 0:
            move = selectRandom(cornerOpen)
            return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)
        if len(edgesOpen) > 0:
            move = selectRandom(edgesOpen)

    return move


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def printBoard(board):
    p_b = [' ']*10
    for i in range(1,10):
        if board[i] == 'X':
            p_b[i] = ("\u001b[32;1m"+board[i]+"\u001b[33;1m")
        elif board[i]=='O':
            p_b[i] = ("\u001b[31;1m"+board[i]+"\u001b[33;1m")
        else:
            p_b[i] = (board[i])
    


    print('\u001b[33;1m ')
    print('\t\t _________________')
    print('\t\t|     |     |     |')
    print('\t\t|  '   +p_b[1]+'  |  '+p_b[2]+'  |  '+p_b[3]+'  |')
    print('\t\t|_____|_____|_____|')
    print('\t\t|     |     |     |')
    print('\t\t|  '   +p_b[4]+'  |  '+p_b[5]+'  |  '+p_b[6]+'  |')
    print('\t\t|_____|_____|_____|')
    print('\t\t|     |     |     |')
    print('\t\t|  '   +p_b[7]+'  |  '+p_b[8]+'  |  '+p_b[9]+'  |')
    print('\t\t|_____|_____|_____|')
    print('\u001b[0m ')


def main():
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print("\n>>> O's won this time")
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('\n>>> TIE GAME')
            else:
                insertBoard('O', move)
                print(f"\n>>> Computer placed 'O' in position {move} : ")
                printBoard(board)
        else:
            print("\n>>> X's won this time! Good Job")
            break

    if isBoardFull(board):
        print('\n>>> TIE GAME')


while True:
    answer = input('\n>>> Do you want to play again? (Y/N)\t')
    if answer.lower() == 'y' or answer.lower() == 'yes':
        board = [' ' for x in range(10)]
        print('_________________________________________________')
        main()
    else:
        break
