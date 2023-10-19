import pygame
from pygame.sprite import Sprite
from config import WIDTH_SCREEN, HEIGHT_SCREEN, SHIP_SPEED, DRIVE_INTENSE
from speeder import Speeder
import os

class StarShip(Sprite):
    def __init__(self):
        super().__init__()
        self.images = self.load_images()
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        
        self.rect.x = WIDTH_SCREEN / 2
        self.rect.y = HEIGHT_SCREEN - self.image.get_height()
        
        self.speeder = Speeder()
    
    def load_images(self):
        image_folder = os.getcwd()
        png_name_list = os.listdir('assets\mainship')
        png_list = []
        for png_name in png_name_list:
            png_list.append(pygame.image.load(f"{image_folder}\\assets\\mainship\\{png_name}"))
        return png_list
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def update(self, direction):
        self.speeder.update()
        
        left_wall = 0
        right_wall = (WIDTH_SCREEN - self.image.get_width())
        is_left_wall = self.rect.x < left_wall
        is_right_wall =  right_wall  < self.rect.x 

        #rules for wall stopped
        if is_left_wall and direction == -1:
            #can't move
            pass
        elif is_left_wall and direction == 1:
            self.rect.x += direction * SHIP_SPEED
        elif is_right_wall and direction == -1:
            self.rect.x += direction * SHIP_SPEED
        elif is_right_wall and direction == 1:
            #can't move
            pass
        elif direction:
            self.rect.x += direction * SHIP_SPEED
        
        #rules for drive animation
        if self.speeder.can_pass(1 / DRIVE_INTENSE):    
            if self.index < len(self.images) - 1:
                self.index += 1
                self.image = self.images[self.index]
            else:
                self.index = 0  
                self.image = self.images[self.index]
            