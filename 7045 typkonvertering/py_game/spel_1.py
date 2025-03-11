import pygame
import random

# Initiera pygame
pygame.init()

# Skärmstorlek
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Undvik Hindren")

# Färger
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Spelarens variabler
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 2 * player_size
player_speed = 7

# Hinder
obstacle_width = 50
obstacle_height = 50
obstacle_x = random.randint(0, WIDTH - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 5

# Spelloop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Rörelse
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    
    # Hindrets rörelse
    obstacle_y += obstacle_speed
    if obstacle_y > HEIGHT:
        obstacle_y = -obstacle_height
        obstacle_x = random.randint(0, WIDTH - obstacle_width)
    
    # Kollision
    if (player_x < obstacle_x + obstacle_width and
        player_x + player_size > obstacle_x and
        player_y < obstacle_y + obstacle_height and
        player_y + player_size > obstacle_y):
        running = False
    
    # Rita objekt
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, RED, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
