import pygame
import game

# setup pygame
pygame.init()

last_tick = pygame.time.get_ticks()

screen = pygame.display.set_mode((500, 500))

game.screen = screen

clock = pygame.time.Clock()


is_running = True
while is_running:
    # when I press the x button quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                game.finance.placePlant(pygame.mouse.get_pos())


    # make a background color
    screen.fill((255,230,230))

    #miliseconds
    frame_duration = pygame.time.get_ticks() - last_tick
    last_tick = pygame.time.get_ticks()



    game.loop(screen, frame_duration)



    # send new image to the window
    pygame.display.update()
    clock.tick(60)
