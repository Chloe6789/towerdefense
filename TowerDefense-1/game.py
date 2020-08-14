from plant import *
from zombie import *
from bullet import *
from money import *
import spawn


zombies = []
plants = []
bullets = []

map = [(30,30),(400,30),(400, 400),(30, 400)]

finance = money()

def go():
    zomb = game.zombie(screen, 8)
    zombies.append(zomb)
    bossZombie = game.zombie(screen, 45)
    zombies.append(bossZombie)

spawn.addAction(go, 80)

def loop(screen, frame_duration):
    spawn.check(frame_duration)
    finance.draw(screen)
    # tell all objects to update

    for zombie in zombies:
        # move zombie
        zombie.loop(frame_duration)
        # draw zombie
        zombie.draw()

    for plant in plants:
        plant.draw()
        plant.face_last()
        plant.loop(frame_duration)

    for bullet in bullets:
        bullet.draw()
        bullet.loop()
        bullet.setVelocity(35)

    #testing 123
    i = 0
    while i < len(zombies):
        if zombies[i].delete:
            del zombies[i]
            i -= 1
        i += 1

def addBullet(bullet):
    bullets.append(bullet)

def addPlant(x,y):
    plants.append(game.plant(screen, x, y))

