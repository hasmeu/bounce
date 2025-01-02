import pygame
from shapes import *
import random
#bounce loss is what makes the ball lose energy
#use round to reduce precision errors
def simulation(screen, screen_width, screen_height, border_thickness, circle, mouse_position):
    # 0, 0
    #increase velocity by gravity
    circle.y_velocity += circle.gravity
    #update positions based on velocity
    circle.x += circle.x_velocity
    circle.y += circle.y_velocity
         
    #collision for bottom border 
    if (circle.y >= screen_height - border_thickness - circle.radius):
        circle.y = screen_height - border_thickness - circle.radius
        circle.y_velocity = round(-circle.y_velocity * circle.bounce_loss, 2) # bounce with 80% of its energy. It will bounce back up but with less height
        
    #collision for top border 
    if (circle.y <= border_thickness + circle.radius):
        circle.y = border_thickness + circle.radius
        circle.y_velocity *= -circle.bounce_loss
        
    #collision for left border
    if (circle.x - circle.radius <= border_thickness):
        circle.x = border_thickness + circle.radius
        circle.x_velocity *= -circle.bounce_loss
    
    #collision for right border 
    if (circle.x >= screen_width - border_thickness - circle.radius):
        circle.x = screen_width - border_thickness - circle.radius
        circle.x_velocity = round(-circle.x_velocity * circle.bounce_loss, 2) 
    #lastly put the updated position on screen for the new frame
    
    
    #handle if clicking the ball and sending it in a random direction with increased velocity. set x and y velocity randomly 
    #if ball clicked
    
    # Calculate the distance between the mouse click and the center of the ball
    dx = mouse_position[0] - circle.x
    dy = mouse_position[1] - circle.y
    distance = (dx**2 + dy**2)**0.5
    #if ball clicked. apply random velocity gain
    if (distance <= circle.radius):
        circle.x_velocity += random.uniform(-100, 100)
        circle.y_velocity += random. uniform(-100, 100)
            
    
    
    #friction
    circle.x_velocity *= .99
    circle.y_velocity *= .99
    circle.draw(screen)
         
         
    
         

        