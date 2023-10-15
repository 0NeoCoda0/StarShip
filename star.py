from pygame import Surface
from pygame import SRCALPHA
from pygame.sprite import Sprite
from pygame.draw import circle, line, rect
from random import randint
from pygame.time import get_ticks

class Point():
    def __init__(self, surface_width, thickness, offset_x=0, offset_y=0):
        self.width = surface_width
        self.half_thickness = thickness // 2    
        self.square_size = self.width // 4
        self.offset_x = offset_x
        self.offset_y = offset_y
            
    def center_top(self):
        x =  self.width * 0.5 - self.half_thickness
        y = 0
        return (x, y)
    
    def center_bottom(self):
        x = self.width * 0.5 - self.half_thickness
        y = self.width
        return (x, y)
    
    def center_right(self):
        x = self.width
        y = self.width * 0.5 - self.half_thickness
        return (x, y)

    def center_left(self):
        x = 0
        y = self.width * 0.5 - self.half_thickness
        return (x, y)
    
    def half_center_top(self):
        x = self.width * 0.50 - self.half_thickness
        y = self.width * 0.25
        return (x, y)
    
    def half_center_bottom(self):
        x = self.width * 0.50 - self.half_thickness
        y = self.width * 0.75
        return (x, y)
    
    def half_center_left(self):
        y = self.width * 0.5 - self.half_thickness
        x = self.width * 0.25
        return (x, y)
    
    def half_center_right(self):
        y = self.width * 0.5 - self.half_thickness
        x = self.width * 0.75
        return (x, y)
    
    def half_left_top_center(self):
        free_space_x = self.width - self.square_size
        x = free_space_x // 2
        y = x
        return (x, y)
    
    def square(self):
        return (self.square_size, self.square_size)
    

    

class Star(Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.width = randint(1, 25)
        self.image = Surface([self.width, self.width], SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.time_create = get_ticks()
        
        background_color = (randint(1, 255), randint(1, 255), randint(1, 255), randint(110, 170))
        center_color = (randint(233, 255), randint(233, 255), randint(233, 255), randint(150, 255))
        
        line_thickness = 2
        surface = Point(self.width, line_thickness)  
        
        # Рисуем линии хвостов
        line(self.image, background_color, surface.center_top(), surface.center_bottom(), line_thickness)
        line(self.image, background_color, surface.center_left(), surface.center_right(), line_thickness)
        
        # Рисуем прямоугольник центра
        rect(self.image, background_color, (surface.half_left_top_center(), surface.square()), 0)
        
        # Рисуем сияющий центр
        line(self.image, center_color, surface.half_center_top(), surface.half_center_bottom(), line_thickness)
        line(self.image, center_color, surface.half_center_left(), surface.half_center_right(), line_thickness)
        
    def get_coordinates(self):
        return (self.rect.x, self.rect.y)
        
    def set_moving_speed(self, y):
        self.rect.y += y
    
    def get_current_time(self):
        return get_ticks()
    
    