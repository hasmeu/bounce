import pygame
from shapes import *

def simulation(screen, screen_width, screen_height):
    # 0, 0
    x = screen_width / 2
    y = screen_height / 2
    
    
    
    #initialize position
    circle = Circle("black", x, y, 20)    
    
    while (circle.y < screen_height):
        screen.fill("white")
        circle.draw(screen)
        
        circle.y_velocity += circle.gravity
        circle.y += circle.y_velocity
         
        pygame.display.flip()
        pygame.time.Clock().tick(60)
         
         
    
    # while ball gravity is not 0 
        