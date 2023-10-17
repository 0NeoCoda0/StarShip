import pygame

class Handler():
    def __init__(self):
        self.event = pygame.event.get()
    
    def quit(self):
        for event in self.event:
            if event.type == pygame.QUIT:
                return False