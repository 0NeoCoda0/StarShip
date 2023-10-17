# Сначала появляются все звезды на небе
# Затем генерируются сверху экрана
# Входные параметры: группа_спрайтов, количество_генерируемых_звезд, (начальная_высота, конечная_высота)
# Результат: плоскость с непересекающимися звездами

from star import Star
import pygame
from pygame.sprite import Sprite
from random import randint
from config import WIDTH_SCREEN, HEIGHT_SCREEN, MAX_STAR_SIZE
from pygame import SRCALPHA
from time import sleep

class Sky(Sprite):
    def __init__(self, stars_quantity):
        super().__init__()
        self.image = pygame.surface.Surface([WIDTH_SCREEN, HEIGHT_SCREEN], SRCALPHA)
        self.rect = self.rect = self.image.get_rect()
        self.stars_quantity = stars_quantity
        self.stars_coordinates = set()
        self.all_stars = pygame.sprite.Group()

    def create_stars(self, delta_height):
        def is_overlapping(star_1, star_2):
            x_1, y_1, radius_1 = star_1
            x_2, y_2, radius_2 = star_2
            star_distance = (x_1 - x_2)**2 + (y_1 - y_2)**2
            radius_distance = (radius_1 + radius_2)**2
            return star_distance < radius_distance
        
        if len(self.stars_coordinates) <= self.stars_quantity:
            print(f'{len(self.stars_coordinates)}')
            a, b = delta_height
            x, y = randint(0 , WIDTH_SCREEN - MAX_STAR_SIZE), randint(a, b) 
            star = Star(x, y)
            new_star = star.get_coordinates
            
            if not self.stars_coordinates:
                self.stars_coordinates.add(new_star)
                self.all_stars.add(star)
            
            is_overlap = False
            for exist_star in list(self.stars_coordinates):
                if is_overlapping(new_star(), exist_star()):
                    is_overlap = True
                
            if not is_overlap:
                self.stars_coordinates.add(new_star)
                self.all_stars.add(star)
                
    def update(self):
        for star in self.all_stars:
            star.update()
            if star.rect.y > HEIGHT_SCREEN:
                self.stars_coordinates.remove(star.get_coordinates)
                star.kill()
                

    def draw(self, screen):
        self.all_stars.draw(screen)
        
    