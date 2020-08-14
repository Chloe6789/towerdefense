import pygame
import game


class money():
    def __init__(self):
        pygame.font.init()
        self.money = 300
        self.font = pygame.font.Font('freesansbold.ttf', 15)

    def draw(self, screen):
        text = self.font.render('money:' + str(self.money), True, (0, 0, 0))
        screen.blit(text, (30, 20))

    def placePlant(self, mousePosition):
        if self.money >= 200:
            self.money -= 100
            game.addPlant(mousePosition[0], mousePosition[1])
    
        else:
            print("not enough $$")