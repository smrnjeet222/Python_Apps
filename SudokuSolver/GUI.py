import pygame
import sys
from pygame.locals import *
from solver import solve, valid
from generateSudoku import makeBoard
from copy import deepcopy
import time

pygame.font.init()

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200)
RED = (255,   0,   0)
GREEN = (0, 255,   0)
BLUE = (0,   0, 255)
AQUA = (0, 255, 255)
FUCHSIA = (255, 0, 255)
SILVER = (192, 192, 192)
TEAL = (0, 128, 128)
PURPLE = (128, 0, 128)

FPS = 20
FPSCLOCK, DISPLAYSURF = None, None

WINDOWMULTIPLIER = 6
WINDOWSIZE = 90

WINDOWWIDTH = WINDOWSIZE*WINDOWMULTIPLIER
WINDOWHEIGHT = WINDOWSIZE*WINDOWMULTIPLIER

SQUARESIZE = int(WINDOWSIZE*WINDOWMULTIPLIER/3)
CELLSIZE = int(SQUARESIZE/3)

STRIKES = 0
END = False

board = makeBoard()

d_board = deepcopy(board)


def fillboard(win):
    fnt = pygame.font.SysFont("comicsans", 40)
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                txt = fnt.render(str(board[i][j]), 1, (BLACK))
                win.blit(txt, (CELLSIZE*(j)+CELLSIZE //
                               3, CELLSIZE*(i)+CELLSIZE//3))


def enterDigits(win, key, mx, my, yes):
    x = int(mx/CELLSIZE)
    y = int(my/CELLSIZE)
    try:
        fnt = pygame.font.SysFont("comicsans", 30)
        if board[y][x] == 0:
            if yes:
                board[y][x] = d_board[y][x]
                if solve(deepcopy(board)) and valid(board, board[y][x], (y, x)):
                    board[y][x] = d_board[y][x]
                else:
                    global STRIKES
                    STRIKES += 1
                    board[y][x] = 0
                    d_board[y][x] = 0
            elif key:
                d_board[y][x] = key
            elif key == 0:
                d_board[y][x] = 0
    except:
        pass

    for i in range(9):
        for j in range(9):
            if d_board[i][j] != 0 and board[i][j] == 0:
                if END:
                    txt = fnt.render(str(d_board[i][j]), 1, (TEAL))
                elif valid(board, d_board[i][j], (i, j)):
                    txt = fnt.render(str(d_board[i][j]), 1, (GREEN))
                else:
                    txt = fnt.render(str(d_board[i][j]), 1, (RED))

                win.blit(txt, (CELLSIZE*(j)+CELLSIZE //
                               4, CELLSIZE*(i)+CELLSIZE//4))


def drawBox(win, color, mouseX, mouseY):
    boxX = (mouseX - mouseX % CELLSIZE)
    boxY = (mouseY - mouseY % CELLSIZE)

    if mouseY < WINDOWHEIGHT:
        pygame.draw.rect(win, color, (boxX, boxY, CELLSIZE, CELLSIZE), 1)


def drawGrid():

    for x in range(0, WINDOWWIDTH, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, GRAY, (x, 0), (x, WINDOWHEIGHT))

    for y in range(0, WINDOWHEIGHT, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, GRAY, (0, y), (WINDOWWIDTH, y))

    for x in range(0, WINDOWWIDTH+1, SQUARESIZE):
        pygame.draw.line(DISPLAYSURF, BLACK, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT+1, SQUARESIZE):
        pygame.draw.line(DISPLAYSURF, BLACK, (0, y), (WINDOWWIDTH, y))

    return None


def drawWindow(win, time, key, mx, my, yes):
    win.fill(WHITE)

    fnt = pygame.font.SysFont('comicsans', 40)
    txt = fnt.render(f"Time : {format_time(time)}", 2, (PURPLE))
    win.blit(txt, (WINDOWWIDTH-170, WINDOWHEIGHT+15))

    txt = fnt.render(("X  "*STRIKES + ".   "*(5-STRIKES)), 1, (RED))
    win.blit(txt, (20, WINDOWHEIGHT+15))
    drawGrid()
    fillboard(win)
    enterDigits(win, key, mx, my, yes)


def format_time(secs):
    sec = secs % 60
    minute = secs//60
    hour = minute//60

    mat = " " + str(minute) + ":" + str(sec)
    return mat


def gameOver(win, h=0):
    win.fill(YELLOW)
    fnt = pygame.font.SysFont('comicsans', 100)
    txt = fnt.render("GAME OVER", WINDOWMULTIPLIER, (RED))
    win.blit(txt, (WINDOWWIDTH//9, h))


def drawSpace(win, text, outline=None):
    pygame.draw.rect(win, GREEN, ((2*WINDOWWIDTH)//5,
                                  WINDOWHEIGHT+2, WINDOWWIDTH//5, 48))

    if outline:
        pygame.draw.rect(win, FUCHSIA, ((2*WINDOWWIDTH)//5,
                                        WINDOWHEIGHT+2, WINDOWWIDTH//5, 48), outline)

    if text != '':
        font = pygame.font.SysFont('comicsans', 30)
        text = font.render(text, 1, FUCHSIA)
        win.blit(text, ((2*WINDOWWIDTH)//5 + 20,
                        WINDOWHEIGHT+18, WINDOWWIDTH//5, 40))


def isSpace(pos):
    if pos[0] > (2*WINDOWWIDTH)//5 and pos[0] < (2*WINDOWWIDTH)//5+WINDOWWIDTH//5:
        if pos[1] > WINDOWHEIGHT+10 and pos[1] < WINDOWHEIGHT+48:
            return True
    return False


def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH+1, WINDOWHEIGHT+51))
    icon = pygame.image.load('sudoku.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Sudoku")

    start = time.time()

    mouseClicked = False
    mouseX = 0
    mouseY = 0

    h = 0
    peek = False

    while True:
        key = None
        yes = False
        play_time = round(time.time()-start)

        for event in pygame.event.get():
            global STRIKES
            global d_board
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEMOTION:
                mouseHX, mouseHY = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                mouseClicked = True
                if STRIKES == 5:
                    STRIKES += 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    key = 0
                if event.key == pygame.K_RETURN:
                    yes = True
                if event.key == pygame.K_SPACE:
                    peek = not peek
                    if peek:
                        solve(d_board)
                    else:
                        d_board = deepcopy(board)

        # print(mouseX, mouseY)
        global END

        drawWindow(DISPLAYSURF, play_time, key, mouseX, mouseY, yes)
        if mouseClicked == True:
            drawBox(DISPLAYSURF, BLUE, mouseX, mouseY)
            if isSpace((mouseX, mouseY)):
                END = True
                solve(d_board)

        drawBox(DISPLAYSURF, RED, mouseHX, mouseHY)
        drawSpace(DISPLAYSURF, "SOLVE", 3)

        if STRIKES > 5:
            if h < (WINDOWHEIGHT//2-40):
                h += 15
            gameOver(DISPLAYSURF, h)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()
