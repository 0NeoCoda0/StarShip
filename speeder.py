from config import MAX_STAR_SIZE, SPEED_LEVELS
from time import time

class Speeder():
    def __init__(self):
        self.now = None
        self.past = time()
    
    def update(self):
        self.now = time()
    
    def normalize(self, x, max):
        return x/max
    
    def get_speed(self, distance, delta_time):
        norm_distance = self.normalize(distance, MAX_STAR_SIZE)
        moving_speed = int(1 + norm_distance * SPEED_LEVELS)
        stand_speed = 0
        if self.now - self.past > delta_time:
            self.past = self.now    
            return moving_speed
        else:
            return stand_speed
        
    def can_pass(self, delay):
        if self.now - self.past > delay:
            self.past = self.now  
            return True
        return False