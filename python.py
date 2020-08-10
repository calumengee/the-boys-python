import pygame, os, pygame.mixer, time
#size of screen
screen_size = screen_width, screen_hight = 1920, 1080
#setting display and surface objects
screen=pygame.display.set_mode(screen_size)
#defining colors
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255

#getting clock object 
clock = pygame.time.Clock()

class MyCircle:

    def __init__(self, position, size, color = (255,255,255), width = 1):
        self.x = position.x
        self.y = position.y 
        self.size=size
        self.color = color
        self.width = width

    def display(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size, self.width)

#title
pygame.display.set_caption('deez nuts gottem!')

my_circle = MyCircle((100, 100), 10, red)

#def for fps and continued running
fps_limit=60
RunMe=True
while RunMe:
    #limit for framrate
    clock.tick(fps_limit)

    for event in pygame.event.get():
        if event.type == pygame.quit:
            RunMe = False

            #Clearing screen
            screen.fill(white)

            my_circle.display()

            #display everything on screen
            pygame.display.flip()

#Quit game
pygame.quit()
sys.exit()