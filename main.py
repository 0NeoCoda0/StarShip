import pygame
from random import randint
from config import HEIGHT_SCREEN, WIDTH_SCREEN
from config import BLACK
from config import GAME_SPEED

def check_exit_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    
    return False

    
def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
    
    while True:
        if check_exit_event():
            break
        screen.fill(BLACK)
        
        #sky - объект со звездами   
        #sky.draw(screen)
        
        pygame.display.flip()
        clock.tick(GAME_SPEED)
        
if __name__ == "__main__":
    main()