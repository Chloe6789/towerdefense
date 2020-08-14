from drawable import *
import pygame
import game
import math


def check_collision(x, y):
    for zombie in game.zombies:
        if math.hypot(zombie.x - x, zombie.y - y) < 30:
            zombie.health -= 1
            return True
    return False


class zombie(drawable):
    def __init__(self, screen, health=1):
        super().__init__(screen)
        self.image = pygame.image.load("assets/zombie.png")
        self.delete = False
        self.health = health

        self.xvel = 0
        self.yvel = 0

        self.xacc = 0
        self.yacc = 0

        self.landmark = 0

    def loop(self, elapsed):
        pos = game.map[self.landmark]
        self.xacc = (pos[0] - self.x)/2000
        self.yacc = (pos[1] - self.y)/2000

        self.xvel += self.xacc
        self.yvel += self.yacc

        # constant vel
        vel = math.hypot(self.xvel, self.yvel)
        self.xvel *= 3 / vel
        self.yvel *= 3 / vel

        self.x += self.xvel
        self.y += self.yvel

        #move along path
        if math.hypot(pos[0] - self.x, pos[1] - self.y) < 40:
            self.landmark += 1
        
        #end of path
        if self.landmark == len(game.map):
            self.delete = True

        #killed
        if self.health <= 0:
            game.finance.money += 15
            self.delete = True
