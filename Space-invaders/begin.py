import math
import random

import pygame
from pygame import mixer


pygame.init()

screen = pygame.display.set_mode((800, 600))


background = pygame.image.load('assets/background.png')


mixer.music.load("assets/background.wav")
mixer.music.play(-1)


pygame.display.set_caption("Space Invader")
icon = pygame.image.load('assets/ufo.png')
pygame.display.set_icon(icon)


playerImg = pygame.image.load('assets/player.png')
playerX = 370
playerY = 500
playerX_change = 0


enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('assets/enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    if i%2:
        enemyX_change.append(5)
    else:
        enemyX_change.append(-5)

    enemyY_change.append(40)


bulletImg = pygame.image.load('assets/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 15
bullet_state = "ready"


score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) +
                         (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            playerX_change = -5
        if keys[pygame.K_d]:
            playerX_change = 5
        if keys[pygame.K_SPACE]:
            if bullet_state == "ready":
                bulletSound = mixer.Sound("assets/laser.wav")
                bulletSound.play()
                bulletX = playerX
                fire_bullet(bulletX, bulletY)


    playerX += playerX_change

    if playerX <= 50:
        playerX = 51
    elif playerX >= 700:
        playerX = 701

    for i in range(num_of_enemies):

        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("assets/explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, testY)
    pygame.display.update()
