from pygame.transform import rotate
from pygame import Surface
from pygame import SRCALPHA
from pygame.sprite import Sprite
from pygame.draw import  line, rect
from random import randint


from config import STAR_SPEED, MAX_STAR_SIZE, MIN_STAR_SIZE

class Point():
    def __init__(self, surface_width, thickness):
        self.width = surface_width
        self.half_thickness = thickness // 2    
        self.square_size = self.width // 4
            
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
        self.width = randint(MIN_STAR_SIZE, MAX_STAR_SIZE)
        self.flicker_rate = randint(1, 3)
        self.image = Surface([self.width, self.width], SRCALPHA)
        self.rect = self.image.get_rect()
        
        self.rect.y = y
        self.rect.x = x
        
        self.radius = randint(self.width * 4, self.width * 5)
        
        self.center_brightness = randint(150, 255)
        self.bg_brightness = randint(110, 170)
        
        self.draw_star()
        #self.image = rotate(self.image, randint(0, 360))
    def draw_star(self):
        bg_color = randint(60, 255)
        ct_color = randint(233, 255)
        
        background_color = (bg_color, bg_color, bg_color, self.bg_brightness)
        center_color = (ct_color, ct_color, ct_color, self.center_brightness)
        
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
        self.rect.y += STAR_SPEED + (self.width * 0.1)
        
        # Логика мерцания
        self.center_brightness += self.flicker_rate
        if self.center_brightness > 255:
            self.center_brightness = 255
            self.flicker_rate = -self.flicker_rate
        elif self.center_brightness < 100:
            self.center_brightness = 100
            self.flicker_rate = -self.flicker_rate 

        self.bg_brightness += self.flicker_rate // 2
        if self.bg_brightness > 170:
            self.bg_brightness = 170
            self.flicker_rate = -self.flicker_rate // 24
        elif self.bg_brightness < 50:
            self.bg_brightness = 50
            self.flicker_rate = -self.flicker_rate // 25

        self.draw_star()  # перерисовываем звезду с новой яркостью
        
    def get_coordinates(self):
        x = self.rect.x + self.width // 2
        y = self.rect.y + self.width // 2
        return (x, y, self.radius)
    
    def flash(self, curve=None):
        pass