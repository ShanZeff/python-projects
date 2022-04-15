from random import randint
import pgzrun
from pgzero.actor import Actor

WIDTH = 800
HEIGHT = 600

balloon = Actor("balloon")
balloon.pos = 400, 300

# initialise the pygame zero
pgzrun.go()
