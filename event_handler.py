import pygame

class Handler():
    def __init__(self):
        self.event = pygame.event.get()
        self.keys = pygame.key.get_pressed()
    
    def get_event(self):
        self.event = pygame.event.get()
        self.keys = pygame.key.get_pressed()
        
    
    def quit(self):
        for event in self.event:
            if event.type == pygame.QUIT:
                print('check quit event!')
                return False
        return True
    
    def get_key_move(self):
        if self.keys[pygame.K_a]:
            return -1
        if self.keys[pygame.K_d]:
            return 1