import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))

score = 0

pygame.display.set_caption("atos vs flowers")
background = pygame.image.load("assets/tło.png")
icon = pygame.image.load("assets/atos32.png")
flower_1_img = pygame.image.load("assets/floral.png")
flower_2_img = pygame.image.load("assets/floral2.png")
flower_3_img = pygame.image.load("assets/floral3.png")
pygame.display.set_icon(icon)

atos_speed = 0.5

player_img = pygame.image.load("assets/atos.png")
playerX = 368
playerY = 480
speedX = 0
speedY = 0

pee_img = pygame.image.load("assets/pee2.png")
peeX = 0
peeY = 0
pee_speedX = 0.3
pee_speedY = 0.3
pee_state = "ready"


def player(x, y):
    screen.blit(player_img, (x, y))


def flower1():
    screen.blit(flower_1_img, (flower_X, flower_Y))


def pee_done(x, y):
    global pee_state
    pee_state = "done"
    screen.blit(pee_img, (x + 16, y + 16))


def iscollision(x1, y1, x2, y2):
    distance = math.sqrt((math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2)))
    if distance < 25:
        return True
    else:
        return False


def generate_flower():
    global flower_X, flower_Y, flower_speedX, flower_speedY
    flower_X = random.randint(1, 735)
    flower_Y = random.randint(100, 535)
    flower_speedX = 0
    flower_speedY = 0

generate_flower()

running = True
while running:
    screen.fill((164, 255, 110))  # screen.blit(background, (0, 0)) #screen.fill((164, 255, 110))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("Final score:", score)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                peeY = playerY
                peeX = playerX
                pee_done(playerX, playerY)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speedX = -atos_speed
            if event.key == pygame.K_RIGHT:
                speedX = atos_speed
            if event.key == pygame.K_UP:
                speedY = -atos_speed
            if event.key == pygame.K_DOWN:
                speedY = atos_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                speedX = 0
                speedY = 0

    playerX += speedX
    playerY += speedY

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536

    if pee_state == "done":
        pee_done(peeX, peeY)
        peeY += pee_speedY

    if iscollision(flower_X, flower_Y, peeX, peeY):
        pee_state = "ready"
        peeY = -50
        score += 1
        generate_flower()

    myfont = pygame.font.SysFont("Calibri", 50)
    label = myfont.render(("Score: "+str(score)), False, (0, 0, 0))
    screen.blit(label, (300, 10))

    if score % 3 == 0:
        def flower1():
            screen.blit(flower_1_img, (flower_X, flower_Y))
    elif score % 3 == 1:
        def flower1():
            screen.blit(flower_2_img, (flower_X, flower_Y))
    else:
        def flower1():
            screen.blit(flower_3_img, (flower_X, flower_Y))


    flower1()
    player(playerX, playerY)

    pygame.display.update()
