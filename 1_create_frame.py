import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("My Game")


background = pygame.image.load(
    "C:/Users/melis/OneDrive/바탕 화면/독학실습/Py_Game/Background.png")

character = pygame.image.load(
    "C:/Users/melis/OneDrive/바탕 화면/독학실습/Py_Game/character.png")

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2)-(character_width/2)
character_y_pos = screen_height-character_height

running = True
# is game running?

while running:
    for event in pygame.event.get():  # Is event occured?
        if event.type == pygame.QUIT:  # Closing display event occur
            running = False  # Game not running

    # screen.fill("#c5cae9") #setting background with color
    screen.blit(background, (0, 0))  # setting background with png.file
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()  # game screen keep drawing
# if game not running
pygame.quit()
