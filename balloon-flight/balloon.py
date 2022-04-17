from random import randint
import pygame

# Initialise the pygame
pygame.init()

# background
background = pygame.image.load('background.png')

# create the screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("Balloon Flight")
icon = pygame.image.load('air-hot-balloon.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('balloon.png')
playerX = 370
playerY = 300

# test
houseImg = pygame.image.load('house.png')
houseX = 100
houseY = 300

treeImg = pygame.image.load('tree.png')
treeX = 200
treeY = 200


def player():
    screen.blit(playerImg, (playerX, playerY))
    screen.blit(houseImg, (houseX, houseY))
    screen.blit(treeImg, (treeX, treeY))


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
