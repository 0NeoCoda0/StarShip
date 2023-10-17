import pygame
from random import randint
from config import HEIGHT_SCREEN, WIDTH_SCREEN
from config import BLACK
from config import GAME_SPEED
from config import ON_BOARD, FROM_TOP, QUANTITY_STARS
from sky import Sky

def check_exit_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    
    return False

    
def main():
    
    pygame.init()
    running = True
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
    sky = Sky(QUANTITY_STARS)
    for _ in range(QUANTITY_STARS):
        sky.create_stars(delta_height=ON_BOARD)
    
    while running:
            if check_exit_event():
                running = False
            
            sky.create_stars(delta_height=FROM_TOP)
            sky.update()
            
            sky.draw(screen)
            
            pygame.display.flip()
            clock.tick(GAME_SPEED)
            screen.fill(BLACK)
            

        
if __name__ == "__main__":
    main()