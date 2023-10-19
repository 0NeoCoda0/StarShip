import pygame
from config import HEIGHT_SCREEN, WIDTH_SCREEN
from config import BLACK
from config import GAME_SPEED
from config import QUANTITY_STARS
from sky import Sky
from event_handler import Handler
from spaceship import StarShip


    
def main():
    
    pygame.init()
    handler = Handler()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
    sky = Sky(QUANTITY_STARS)
    space_ship = StarShip()
    
    while handler.quit():
        handler.get_event()
        direction = handler.get_key_move()
        
        sky.update()
        space_ship.update(direction)
            
        sky.draw(screen)
        space_ship.draw(screen)
                   
        pygame.display.flip()
        clock.tick(GAME_SPEED)
        screen.fill(BLACK)
            

        
if __name__ == "__main__":
    main()