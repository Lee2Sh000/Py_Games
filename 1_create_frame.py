import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("My Game")

running = True
# is game running?

while running:
    for event in pygame.event.get():  # Is event occured?
        if event.type == pygame.QUIT:  # Closing display event occur
            running = False  # Game not running


# if game not running
pygame.quit()
