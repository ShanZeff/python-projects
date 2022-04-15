from random import randint
import pgzrun
from pgzero.actor import Actor
from pgzero.game import screen

WIDTH = 800
HEIGHT = 600

balloon = Actor("balloon")
balloon.pos = 400, 300
bird = Actor("bird-up")
bird.pos = randint(800, 1600), randint(10, 200)
house = Actor("house")
house.pos = randint(800, 1600), 460
tree = Actor("tree")
tree.pos = randint(800, 1600), 450

BirdUp = True
up = False
GameOver = False
score = 0
NumberOfUpdates = 0
scores = []


def update_high_scores():
    pass


def display_high_scores():
    pass


def draw():
    screen.blit("background, (0,0)")
    if not GameOver:
        balloon.draw()
        bird.draw()
        house.draw()
        tree.draw()
        screen.draw.text("Score: " + str(score), (700, 5), color="black")
    else:
        display_high_scores()


# initialise the pygame zero
pgzrun.go()
