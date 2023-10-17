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
    