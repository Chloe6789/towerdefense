from drawable import *
import pygame
import game
import math
import bullet

class plant(drawable): # explain the new variables and have them type them out
    def __init__(self, screen, x, y, range = 300, reload_time = 100, scatter = 20):
        super().__init__(screen)
        self.image = pygame.image.load("assets/plant.png")

        self.screen = screen
        self.x = x
        self.y = y

        self.range = range
        self.reload_time = reload_time
        self.scatter = scatter
        self.zombie_seen = None
        
        self.time_since_reload = 0

    def face_last(self): 
        # look for proximity
        for enemy in reversed(game.zombies):
            relative = (enemy.x - self.x, enemy.y - self.y)
            if math.hypot(relative[0], relative[1]) < self.range:
                self.direction = math.degrees(math.atan2(relative[1], relative[0]))
                return True
        return False

    def face_closest(self): #warm up is what are lists and how do they work
        # look for proximity
        closest_distance = 10000000
        closest_zombie = None

        for zombie in game.zombies:
            distance = math.hypot(zombie.x-self.x, zombie.y-self.y)
            if distance < closest_distance:
                closest_distance = distance
                closest_zombie = zombie

        if closest_zombie == None:
            return False
        else:
            self.zombie_seen = True

    def loop(self, elapsed): #write this out
        self.time_since_reload += elapsed
        

        if self.time_since_reload > self.reload_time:
            newBullet = bullet.bullet(self.screen, self.x, self.y)
            game.addBullet(newBullet)
            newBullet.setVelocity(self.direction)
        self.time_since_reload = 0
        print(self.time_since_reload)
