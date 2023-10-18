import pygame
from config import HEIGHT_SCREEN, WIDTH_SCREEN
from config import BLACK
from config import GAME_SPEED
from config import QUANTITY_STARS
from sky import Sky
from event_handler import Handler



    
def main():
    
    pygame.init()
    handler = Handler()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
    sky = Sky(QUANTITY_STARS)
    
    while handler.quit():
        handler.get_event()
        
        sky.update()
            
        sky.draw(screen)
            
        pygame.display.flip()
        clock.tick(GAME_SPEED)
        screen.fill(BLACK)
            

        
if __name__ == "__main__":
    main()