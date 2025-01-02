import pygame

class Shape:
    x_velocity = 0
    y_velocity = 0
    
    def __init__(self, color, x, y,):
        self.color = color
        self.x = x
        self.y = y
    
        
        
class Circle(Shape):
    gravity = .001
    
    def __init__(self, color, x, y, radius):
        super().__init__(color, x, y)
        self.radius = radius
        
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        