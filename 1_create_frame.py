import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("My Game")

clock = pygame.time.Clock()  # Frame per Second

background = pygame.image.load(
    "C:/Users/melis/OneDrive/바탕 화면/독학실습/Py_Game/Background.png")

character = pygame.image.load(
    "C:/Users/melis/OneDrive/바탕 화면/독학실습/Py_Game/character.png")

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2)-(character_width/2)
character_y_pos = screen_height-character_height

# character movement
to_x = 0
to_y = 0
# character speed
character_speed = 0.55
running = True  # is game running?
# Build Enemy
enemy = pygame.image.load(
    "C:/Users/melis/OneDrive/바탕 화면/독학실습/Py_Game/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width/2)-(enemy_width/2)
enemy_y_pos = (screen_height/2)-(enemy_height/2)

# Game Font
game_font = pygame.font.Font(None, 40)

total_time = 10

# Game Starting Time
start_ticks = pygame.time.get_ticks()

while running:
    dt = clock.tick(50)  # Setting FPS
    for event in pygame.event.get():  # Is event occured?
        if event.type == pygame.QUIT:  # Closing display event occur
            running = False  # Game not running

        if event.type == pygame.KEYDOWN:  # Key pressed
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP:  # Key Pressed
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x*dt
    character_y_pos += to_y*dt
# character movement - width threshold
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width-character_width:
        character_x_pos = screen_width-character_width

# character movement - height threshold
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height-character_height:
        character_y_pos = screen_height-character_height

    # Character & Enemy BOOM! Collide
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # Is collide
    if character_rect.colliderect(enemy_rect):
        print("BOO*°OO★M!!!☆$*.°★* 。")
        running = False

    # screen.fill("#c5cae9") #setting background with color
    screen.blit(background, (0, 0))  # setting background with png.file
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # Timer
    elapsed_time = (pygame.time.get_ticks()-start_ticks)/1000  # ms => second
    timer = game_font.render(
        str(int(total_time-elapsed_time)), True, (255, 255, 255))  # print ment, True, color
    screen.blit(timer, (10, 10))

    # If time<0
    if total_time-elapsed_time < 0:
        print("===== T I M E == O V E R =====")
        running = False

    pygame.display.update()  # game screen keep drawing
# if game not running
pygame.quit()
