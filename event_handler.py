import pygame

class Handler():
    def __init__(self):
        self.event = pygame.event.get()
    
    def get_event(self):
        self.event = pygame.event.get()
    
    def quit(self):
        for event in self.event:
            if event.type == pygame.QUIT:
                print('check quit event!')
                return False
        return True