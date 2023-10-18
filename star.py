import math
from pygame import Surface
from pygame import SRCALPHA
from pygame.sprite import Sprite
from pygame.draw import  line, rect
from random import randint, uniform
from config import STAR_SPEED, MAX_STAR_SIZE, MIN_STAR_SIZE 
from config import MAX_STARS_FLICKER_SPEED, MIN_STARS_FLICKER_SPEED
from point import Point
from speeder import Speeder


class Star(Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        #surface
        self.width = randint(MIN_STAR_SIZE, MAX_STAR_SIZE)
        self.image = Surface([self.width, self.width], SRCALPHA)
        self.rect = self.image.get_rect()
        
        #colors
        self.red = self.__get_color()
        self.green = self.__get_color()
        self.blue = self.__get_color()
        self.ct_color = randint(200, 233)
        self.bg_brightness = randint(160, 210)
        
        #animations
        self.flash_generator = self.__flash()
        self.bright_speed = uniform(MIN_STARS_FLICKER_SPEED ,MAX_STARS_FLICKER_SPEED)
        
        #coordinates
        self.rect.y = y
        self.rect.x = x
        self.radius = randint(self.width * 4, self.width * 5)

        #moving
        self.delta_time = 1 / STAR_SPEED
        self.speeder = Speeder()
        self.distance = self.width
        
        #first initialization
        self.draw_star()
        
    def __get_color(self):
        return randint(0, 255)
    
    def __flash(self):
        i = 0
        while True:
            yield 110 + math.sin(i) ** 2 * 145
            i += self.bright_speed
    
    def __get_bright(self):
        return next(self.flash_generator)
            
    def draw_star(self):
        
        background_color = (self.red, self.green, self.blue, self.bg_brightness)
        center_color = (self.ct_color, self.ct_color, self.ct_color, self.__get_bright())
        
        line_thickness = 2
        surface = Point(self.width, line_thickness)  
        
        # Рисуем линии хвостов
        is_short = randint(0, 1)
        if is_short:
            center_left = surface.half_center_left()
            center_right = surface.half_center_right()
        else:
            center_left = surface.center_left()
            center_right = surface.center_right()
            
        line(self.image, background_color, surface.center_top(), surface.center_bottom(), line_thickness)
        line(self.image, background_color, center_left, center_right, line_thickness)
        
        # Рисуем прямоугольник центра
        rect(self.image, background_color, (surface.half_left_top_center(), surface.square()), 0)
        
        # Рисуем сияющий центр
        line(self.image, center_color, surface.half_center_top(), surface.half_center_bottom(), line_thickness)
        line(self.image, center_color, surface.half_center_left(), surface.half_center_right(), line_thickness)
        
    def update(self):
        self.speeder.update()
        self.rect.y += self.speeder.get_speed(self.distance, self.delta_time)

        self.draw_star()  # перерисовываем звезду с новой яркостью
        
    def get_coordinates(self):
        x = self.rect.x + self.width // 2
        y = self.rect.y + self.width // 2
        return (x, y, self.radius)