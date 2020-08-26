import math
import pygame
from queue import PriorityQueue

WIDTH = 600
ROWS = 50

WIN = pygame.display.set_mode((WIDTH, WIDTH))

pygame.display.set_caption("A* pathfinding Algorithm")

RED = (255, 100, 100)
GREEN = (100, 255, 100)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (100, 100, 100)
ORANGE = (255, 165, 0)
PURPLE = (128, 50, 128)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row*width
        self.y = col*width
        self.color = WHITE
        self.neigh = []
        self.width = width
        self.total_rows = total_rows

    def getPos(self):
        return self.row, self.col

    def isClosed(self):
        return self.color == RED

    def isOpen(self):
        return self.color == GREEN

    def isWall(self):
        return self.color == BLACK

    def isStart(self):
        return self.color == ORANGE

    def isEnd(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE

    def makeClosed(self):
        self.color = RED

    def makeOpen(self):
        self.color = GREEN

    def makeWall(self):
        self.color = BLACK

    def makeStart(self):
        self.color = ORANGE

    def makeEnd(self):
        self.color = TURQUOISE

    def makePath(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color,
                         (self.x, self.y, self.width, self.width))

    def updateNeigh(self, grid):
        self.neigh = []
        # down = grid[self.row+1][self.col]
        # up = grid[self.row-1][self.col]
        # right = grid[self.row][self.col+1]
        # left = grid[self.row][self.col-1]

        if self.row < self.total_rows - 1 and not grid[self.row+1][self.col].isWall():
            self.neigh.append(grid[self.row+1][self.col])

        if self.row > 0 and not grid[self.row-1][self.col].isWall():
            self.neigh.append(grid[self.row-1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col+1].isWall():
            self.neigh.append(grid[self.row][self.col+1])

        if self.col > 0 and not grid[self.row][self.col-1].isWall():
            self.neigh.append(grid[self.row][self.col-1])

    def __lt__(self, other):
        return False


def makeGrid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)

    return grid


def drawGrid(win, rows, width):
    gap = width//rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i*gap), (width, i*gap))

    for j in range(rows):
        pygame.draw.line(win, GREY, (j*gap, 0), (j*gap, width))


def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(win)

    drawGrid(win, rows, width)
    pygame.display.update()


def mousePos(pos, rows, width):
    gap = width//rows
    y, x = pos

    row = y//gap
    col = x//gap

    return row, col


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)


def reconstructPath(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.makePath()
        draw()


def algo(draw, grid, start, end):
    cnt = 0
    open_set = PriorityQueue()
    open_set.put((0, cnt, start))
    came_from = {}
    g_score = {node: float('inf') for row in grid for node in row}
    g_score[start] = 0
    f_score = {node: float('inf') for row in grid for node in row}
    f_score[start] = h(start.getPos(), end.getPos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstructPath(came_from, end, draw)
            start.makeStart()
            end.makeEnd()
            return True

        for neigh in current.neigh:
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[neigh]:
                came_from[neigh] = current
                g_score[neigh] = temp_g_score
                f_score[neigh] = temp_g_score + h(neigh.getPos(), end.getPos())
                if neigh not in open_set_hash:
                    cnt += 1
                    open_set.put((f_score[neigh], cnt, neigh))
                    open_set_hash.add(neigh)
                    neigh.makeOpen()

        draw()

        if current != start:
            current.makeClosed()

    return False


def main(win, rows, width):
    grid = makeGrid(rows, width)

    start = None
    end = None

    run = True

    while run:
        draw(win, grid, rows, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = mousePos(pos, rows, width)
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    node.makeStart()
                elif not end and node != start:
                    end = node
                    end.makeEnd()

                elif node != end and node != start:
                    node.makeWall()

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = mousePos(pos, rows, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                if node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            if node != start and node != end and not node.isWall():
                                node.reset()
                            node.updateNeigh(grid)

                    algo(lambda: draw(win, grid, rows, width), grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = makeGrid(rows, width)
    pygame.quit()


if __name__ == "__main__":

    main(WIN, ROWS, WIDTH)
