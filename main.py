import pygame
from random import randint
from star import Star

WIDTH_SCREEN = 1280
HEIGHT_SCREEN = 1024

def check_exit_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    
    return False

def memorize(func):
    memorized_coords = set()

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for coord in result:
            memorized_coords.add(coord)
        return result

    wrapper.memorized_coords = memorized_coords
    return wrapper

@memorize
def fill_stars_group(stars: pygame.sprite.Group, count):
    added_coords = []

    def distance(point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

    for _ in range(count):
        star = Star(randint(0, WIDTH_SCREEN), -randint(0, 50))
        stars.add(star)
        added_coords.append(star.rect.topleft)

    return added_coords

def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
    stars = pygame.sprite.Group()
    
    while True:
        if check_exit_event():
            break
        screen.fill((0, 0, 0))

        fill_stars_group(stars, 1)
            
        print(stars)
        
        for sprite in stars:
            sprite.set_moving_speed(5)
            local_x, local_y = sprite.get_coordinates()
            if local_y > HEIGHT_SCREEN:
                sprite.kill()
                
        stars.draw(screen)
        
        pygame.display.flip()
        clock.tick(20)
        
if __name__ == "__main__":
    main()