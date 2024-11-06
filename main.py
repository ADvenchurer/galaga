import pygame
import pgzrun
import random

#Screen Dimensions
WIDTH = 1200
HEIGHT = 600

#defining colours
WHITE = (255,255,255)
BLUE = (0,0,255)

#create a ship
ship = Actor('galaga')
bug = Actor('bug')

ship.pos = (WIDTH//2, HEIGHT-60)

speed = 5

#define a list for bullets
bullets = []

#defining a list of enemies
enemies = []

enemies.append(Actor('bug'))
#now the enimies will be in a straight line

enemies[-1].x = 10
#starting off the screen thats why putting it at 100,
#slowly the enemy will come down
enemies[-1].y = -100

score = 0




def draw():
    screen.clear()
    screen.fill(BLUE)
    #ship draw()
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    #ship to be drawn last
    ship.draw()
    #displayScore()


pgzrun.go()