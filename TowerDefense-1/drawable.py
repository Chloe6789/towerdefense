import pygame
import math

class drawable(object):
    def __init__(self, screen):
        self.screen = screen
        self.image = None
        self.x = 0
        self.y = 0
        self.direction = 90

    def draw(self):
        self.screen.blit(pygame.transform.rotate(self.image, -self.direction), (self.x, self.y))

    def distanceBetween(self, one, two):
        return math.hypot(one.x - two.x, one.y - two.y)
