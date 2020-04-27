import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

width, rows = 500, 20
s, snack = None, None


class Cube():
    w, rows = 500, 20

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0]+self.dirnx, self.pos[1]+self.dirny)

    def draw(self, surface, eyes=False):
        siz = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
        pygame.draw.rect(surface, self.color, (i*siz, j*siz, siz, siz))
        if eyes:
            centre = siz//2
            radius = 3
            circleMiddle = (i*siz+centre-radius, j*siz+8)
            circleMiddle2 = (i*siz + siz - radius*2, j*siz+8)
            pygame.draw.circle(surface, (250, 250, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (250, 250, 0), circleMiddle2, radius)


class Snake():
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    self.dirnx = -1
                    self.dirny = 0

                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    self.dirnx = 1
                    self.dirny = 0

                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    self.dirnx = 0
                    self.dirny = -1

                if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    self.dirnx = 0
                    self.dirny = 1

                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                if c.dirnx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1:
                    c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1:
                    c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows-1)
                else:
                    c.move(c.dirnx, c.dirny)

    def reset(self, pos):
        self.head = Cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny
        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.pos[0]-1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.pos[0]+1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.pos[0], tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.pos[0], tail.pos[1]+1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)


def drawGrid(w, rows, surface):
    sizebtw = w//rows
    x = 0
    y = 0
    for l in range(rows):
        x += sizebtw
        y += sizebtw

        pygame.draw.line(surface, (128, 128, 128), (x, 0), (x, w))
        pygame.draw.line(surface, (128, 128, 128), (0, y), (w, y))


def redrawWindow(win):
    global rows, width, s, snack
    win.fill((64, 64, 64))
    s.draw(win)
    drawGrid(width, rows, win)
    snack.draw(win)
    pygame.display.update()


def randomSnack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return (x, y)


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def main():
    global width, rows, s, snack
    win = pygame.display.set_mode((width, width))
    pygame.display.set_caption("--SNAKE--->")
    s = Snake((255, 0, 0), (10, 10))
    snack = Cube(randomSnack(rows, s), color=(0, 255, 0))
    run = True
    clock = pygame.time.Clock()
    while run:
        pygame.time.delay(70)
        clock.tick(30)
        s.move()
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = Cube(randomSnack(rows, s), color=(0, 255, 0))

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x+1:])):
                print('Score: ', len(s.body))
                message_box(
                    'You Lost!', f'Play again...\nUr SCORE : {len(s.body)}')
                s.reset((10, 10))
                break

        redrawWindow(win)


main()
