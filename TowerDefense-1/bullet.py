from drawable import *
import game

class bullet(drawable):
    # what does the bullet do?
    #draw itself
    # flies in a straight line
    # kill things
    
    def __init__(self, screen, x, y):
        super().__init__(screen)

        self.x = x
        self.y = y

        self.xVelocity = 0
        self.yVelocity = 0

        self.image = pygame.image.load("assets/bullet.png")
        self.direction = 0

    def setVelocity(self, direction, speed=5, durability=1):
        self.direction = direction
        self.xVelocity = speed * math.cos(math.radians(direction))
        self.yVelocity = speed * math.sin(math.radians(direction))


    def loop(self):
        self.x += self.xVelocity
        self.y += self.yVelocity

        for zombie in game.zombies:
            if math.hypot(self.x - zombie.x, self.y - zombie.y) < 30:
                zombie.health -= 1

