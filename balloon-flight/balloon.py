from random import randint
import pygame

# Initialise the pygame
pygame.init()

background = pygame.image.load('background.png')
screen = pygame.display.set_mode((800, 600))        # create the screen

# title and icon
pygame.display.set_caption("Balloon Flight")
icon = pygame.image.load('air-hot-balloon.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('balloon.png')
playerBalloon = pygame.transform.scale(playerImg, (160, 160))
playerX = 400
playerY = 300

# obstacles
birdImg = pygame.image.load('bird-up.png')
itemBird = pygame.transform.scale(birdImg, (95, 55))
birdX = randint(200, 200)
birdY = randint(10, 200)

houseImg = pygame.image.load('house.png')
itemHouse = pygame.transform.scale(houseImg, (160, 160))
houseX = 580
houseY = 430

treeImg = pygame.image.load('tree.png')
itemTree = pygame.transform.scale(treeImg, (170, 200))
treeX = 20
treeY = 390


def player():
    screen.blit(playerBalloon, (playerX, playerY))
    screen.blit(itemBird, (birdX, birdY))
    screen.blit(itemHouse, (houseX, houseY))
    screen.blit(itemTree, (treeX, treeY))


# Game loop
running = True
while running:

    # background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()
