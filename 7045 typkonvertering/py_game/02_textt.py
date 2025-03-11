import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

pygame.init()


size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Show text")


font = pygame.font.Font(None, 36)


name_text = font.render('Adrian', True, BLACK)


color_text = font.render('Blå', True, WHITE)


nameRect = name_text.get_rect()
nameRect.topleft = (10, 10)

colorRect = color_text.get_rect()
colorRect.bottomright = (size[0] - 10, size[1] - 10)


clock = pygame.time.Clock()


is_running = True


while is_running:
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

   

    
    screen.fill(BLUE)  

    
    screen.blit(name_text, nameRect)  
    screen.blit(color_text, colorRect)  

    
    pygame.display.flip()

  
    clock.tick(60)


pygame.quit()
