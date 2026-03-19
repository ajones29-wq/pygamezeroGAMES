import pgzrun
import random
import os
import pygame
import time



WIDTH = 800
HEIGHT = 600

x = 1000
y = 1000

ship = Actor('playership1_blue')
ship.x = 370
ship.y = 550

gem = Actor('gemgreen')
gem.x = random.randint(20, 780)
gem.y = 0

gem2 = Actor('gemblue')
gem2.x = random.randint(20, 780)
gem2.y = 0

gem3 = Actor('gemred')
gem3.x = random.randint(20, 780)
gem3.y = 0

gem4 = Actor('gemyellow')
gem4.x = random.randint(20, 780)
gem4.y = 0



score = 0
game_over = False

def on_mouse_move(pos, rel, buttons):
    ship.x = pos[0]
    ship.y = pos[1]

def update():
    global score, game_over

    if keyboard.left:
        ship.x = ship.x - 5
        if ship.x < 60:
            ship.x = 60
    
    if keyboard.right:
        ship.x = ship.x + 5
        if ship.x > 740:
            ship.x = 740
    if keyboard.up:
        ship.y = ship.y - 5
        if ship.y < 50:
            ship.y = 50
    
    if keyboard.down:
        ship.y = ship.y + 5
        if ship.y > 540:
            ship.y = 540

    gem.y = gem.y + 5 + score / 5
    gem2.y = gem2.y + 5 + score / 5
    gem3.y = gem3.y + 5 + score / 5
    gem4.y = gem4.y + 5 + score / 5
    if gem.y > 600:
        score = score - 1
        gem.x = random.randint(20, 780)
        gem.y = 0
   
    if gem.colliderect(ship):
        gem.x = random.randint(20, 780)
        gem.y = 0
        score = score + 1
        gem.y = gem.y + 5 + score / 5
   
    if gem2.colliderect(ship):
        gem2.x = random.randint(20, 780)
        gem2.y = 0
        score = score + 2
    if gem2.y > 600:
        gem2.x = random.randint(20, 780)
        gem2.y = 0
        score = score - 2

    if gem3.colliderect(ship):
        gem3.x = random.randint(20, 780)
        gem3.y = 0
        score = score + 4
    if gem3.y > 600:
        gem3.x = random.randint(20, 780)
        gem3.y = 0
        score = score - 4
    
    if gem4.colliderect(ship):
        gem4.x = random.randint(20, 780)
        gem4.y = 0
        score = score + 6
    if gem4.y > 600:
        gem4.x = random.randint(20, 780)
        gem4.y = 0
        score = score - 6

    if score == score < 0:
        score = 0


def draw():
    screen.fill((80,0,70))
    
    if score == 100:
        screen.draw.text('You got to 100!', (360, 300), color=(255,255,255), fontsize=60)
        screen.draw.text('Score: ' + str(score), (360, 350), color=(255,255,255), fontsize=60)
        print(f'{score} gems caught!')
    
    else:
        gem.draw()
        ship.draw()
        gem2.draw()
        gem3.draw()
        gem4.draw()
        screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)



pgzrun.go() # Must be last line
