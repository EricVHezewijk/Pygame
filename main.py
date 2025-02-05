import pygame
import random
import math

pygame.init()

# screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG = (0, 0, 0)

# obstacle settings
OBSTACLE_COLOR = (255, 255, 255)

# player settings
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_COLOR = (255, 0, 0)

# aim line settings
MAX_AIM_LENGTH = 100
AIM_COLOR = (0, 255, 0)
AIM_WIDTH = 3

# initialize display and pygame settings
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")
player = pygame.Rect(300, 250, 50, 50)

# initalize obstacles
obstacles = []
for _ in range(16):
    obstacle = pygame.Rect((random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), 25, 25))
    obstacles.append(obstacle)

# main loop
running = True
while running:

    # refresh screen
    screen.fill(BG)

    # draw in obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, OBSTACLE_COLOR, obstacle)

    # draw in player
    pygame.draw.rect(screen, PLAYER_COLOR, player)

    # draw in aim line
    start_pos = player.center
    mouse_pos = pygame.mouse.get_pos()

    dx = mouse_pos[0] - start_pos[0]
    dy = mouse_pos[1] - start_pos[1]
    distance = math.hypot(dx, dy)

    if distance > MAX_AIM_LENGTH:
        scale = MAX_AIM_LENGTH / distance
        end_pos = (start_pos[0] + dx * scale, start_pos[1] + dy*scale)
    else:
        end_pos = mouse_pos

    pygame.draw.line(screen, AIM_COLOR, start_pos, end_pos, width=AIM_WIDTH)

    # handle player movements
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player.move_ip(-1, 0)
        if player.collidelist(obstacles) != -1 or player.x <= 0:
            player.move_ip(1, 0)
    elif key[pygame.K_d]:
        player.move_ip(1, 0)
        if player.collidelist(obstacles) != -1 or player.x >= SCREEN_WIDTH-PLAYER_WIDTH:
            player.move_ip(-1, 0)
    elif key[pygame.K_w]:
        player.move_ip(0, -1)
        if player.collidelist(obstacles) != -1 or player.y <= 0:
            player.move_ip(0, 1)
    elif key[pygame.K_s]:
        player.move_ip(0, 1)
        if player.collidelist(obstacles) != -1 or player.y >= SCREEN_HEIGHT-PLAYER_HEIGHT:
            player.move_ip(0, -1)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()