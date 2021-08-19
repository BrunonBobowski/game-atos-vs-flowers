""" atos-vs-flowers is a game that was created in order to practise coding and its style.
 The purpose of atos-vs-flowers is to pee the highest number of flowers and avoid the enemy
"""

import pygame
import random
import math

ATOS_SPEED = 0.5
""" ATOS_SPEED informs how fast the player runs """

RIGHT_BORDER_X = 736
LEFT_BORDER_X = 0
TOP_BORDER_Y = 0
BOTTOM_BORDER_Y = 536

pygame.init()

screen = pygame.display.set_mode((800, 600))

score = 0

pygame.display.set_caption("atos vs flowers")
background = pygame.image.load("assets/tło.png")
icon = pygame.image.load("assets/atos32.png")
flower_1_img = pygame.image.load("assets/floral1.png")
flower_2_img = pygame.image.load("assets/floral2.png")
flower_3_img = pygame.image.load("assets/floral3.png")
flower_4_img = pygame.image.load("assets/floral4.png")
flower_5_img = pygame.image.load("assets/floral5.png")

pygame.display.set_icon(icon)

player_img = pygame.image.load("assets/atos.png")
player_x = 368
player_y = 480
speed_x = 0
speed_y = 0

enemy_r_img = pygame.image.load("assets/enemy_1R.png")
enemy_l_img = pygame.image.load("assets/enemy_1L.png")
enemy_speed = 0.2
enemy_x = LEFT_BORDER_X
enemy_y = TOP_BORDER_Y

pee_img = pygame.image.load("assets/pee2.png")
pee_x = 0
pee_y = 0
PEE_SPEED_y = 0.3
pee_state = "ready"


def player(x, y):
    """ this function generates the player on coordinates x and y """

    screen.blit(player_img, (x, y))


def enemy():
    """ this function generates the enemy on coordinates x and y """

    screen.blit(enemy_r_img, (enemy_x, enemy_y))


def flower():
    """ this function generates the flower on coordinates x and y """

    screen.blit(flower_1_img, (flower_x, flower_y))


def pee_done(x, y):
    """ this function changes the pee state from ready to done and generate the pee"""

    global pee_state
    pee_state = "done"
    screen.blit(pee_img, (x + 16, y + 16))


def iscollision(dx, x1, y1, x2, y2):
    """ this function measures the distance between two points [x1, y1] and [x2, y2]
     if the distance is less than 'dx' the function returns True
     """
    distance = math.sqrt((math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2)))
    if distance < dx:
        return True
    else:
        return False


def generate_flower():
    """ this function generate flower on random coordinates"""

    global flower_x, flower_y
    flower_x = random.randint(1, 735)
    flower_y = random.randint(100, 535)


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
                pee_y = player_y
                pee_x = player_x
                pee_done(player_x, player_y)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x = -ATOS_SPEED
            if event.key == pygame.K_RIGHT:
                speed_x = ATOS_SPEED
            if event.key == pygame.K_UP:
                speed_y = -ATOS_SPEED
            if event.key == pygame.K_DOWN:
                speed_y = ATOS_SPEED
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                speed_x = 0
                speed_y = 0

    player_x += speed_x
    player_y += speed_y
    enemy_x += enemy_speed

    if player_x <= LEFT_BORDER_X:
        player_x = LEFT_BORDER_X
    elif player_x >= RIGHT_BORDER_X:
        player_x = RIGHT_BORDER_X

    if player_y <= TOP_BORDER_Y:
        player_y = TOP_BORDER_Y
    elif player_y >= BOTTOM_BORDER_Y:
        player_y = BOTTOM_BORDER_Y
    """ conditions above limit movement, so the player con only move on the 800px x 600px screen """

    if enemy_x <= LEFT_BORDER_X:
        """ if the enemy touches the left border it changes his y by adding 64, reverses the speed
         and changes the enemy picture to enemy_r_img so the enemy is looking to the right """

        enemy_speed *= -1
        enemy_y += 64
        def enemy():
            screen.blit(enemy_r_img, (enemy_x, enemy_y))

    elif enemy_x >= RIGHT_BORDER_X:
        """ if the enemy touches the right border it changes his y by adding 64, reverses the speed
                 and changes the enemy picture to enemy_l_img so the enemy is looking to the left """

        enemy_speed *= -1
        enemy_y += 64
        def enemy():
            screen.blit(enemy_l_img, (enemy_x, enemy_y))

    if enemy_y >= BOTTOM_BORDER_Y:
        enemy_x = 0
        enemy_y = 100

    if pee_state == "done":
        pee_done(pee_x, pee_y)
        pee_y += PEE_SPEED_y

    if iscollision(25, flower_x - 16, flower_y - 16, pee_x, pee_y):
        pee_state = "ready"
        pee_y = -50
        score += 1
        generate_flower()

    if iscollision(75, player_x - 32, player_y - 32, enemy_x, enemy_y):
        """ this function returns false and prints the score if the player collides with the enemy """

        running = False
        print("Score: "+str(score))

    if score % 5 == 0:
        def flower():
            screen.blit(flower_1_img, (flower_x, flower_y))
    elif score % 5 == 1:
        def flower():
            screen.blit(flower_2_img, (flower_x, flower_y))
    elif score % 5 == 2:
        def flower():
            screen.blit(flower_3_img, (flower_x, flower_y))
    elif score % 5 == 3:
        def flower():
            screen.blit(flower_4_img, (flower_x, flower_y))
    else:
        def flower():
            screen.blit(flower_5_img, (flower_x, flower_y))

    """ functions above generates flowers """

    font = pygame.font.SysFont("Kristen ITC", 50)
    label = font.render(("Score: " + str(score)), False, (0, 0, 0))
    screen.blit(label, (300, 10))
    """ setting font, size and displaying score on screen """

    flower()
    player(player_x, player_y)
    enemy()

    pygame.display.update()
