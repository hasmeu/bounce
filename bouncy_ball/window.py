import pygame
from shapes import *
from simulate import simulation

#border variables
border_color = ("black")  
border_thickness = 10


def window():
    #setup pygame window
    pygame.init()
    pygame.display.set_caption("Bounce")
    #clock tracks the framerate
    clock = pygame.time.Clock()
    running = True 
    
    #screen
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w * .65
    screen_height = screen_info.current_h * .85
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)

    #create initial circle
    x = screen_width / 2
    y = screen_height / 2
    circle = Circle("black", x, y, 20)    
    
    #create default mouse position
    mouse_position = (0, 0)

    
    while running:
        #checks for events
        
        for event in pygame.event.get():
            #if x clicked close program
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = event.pos
            
        # ensures the last frame of the window is cleared
        screen.fill("white")
        
        #everything is run for each frame in here
        #render game here!!
        
        #borders 
        borders(screen, screen_width, screen_height)
        
        #run simulation
        simulation(screen, screen_width, screen_height, border_thickness, circle, mouse_position)
        
        
        
        #updates front screen
        pygame.display.flip()
        
        clock.tick(60) #limit frames to 60
        
    pygame.quit()
    
def borders(screen, screen_width, screen_height):
    pygame.draw.rect(screen, border_color, (0, 0, screen_width, border_thickness))
    pygame.draw.rect(screen, border_color, (0, screen_height - border_thickness, screen_width, border_thickness))
    pygame.draw.rect(screen, border_color, (0, 0, border_thickness, screen_height))
    pygame.draw.rect(screen, border_color, (screen_width - border_thickness, 0, border_thickness, screen_height))
    

#Create a window for money tracking