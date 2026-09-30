# Source - https://stackoverflow.com/a/73180236
# Posted by Scott, modified by community. See post 'Timeline' for change history
# Retrieved 2026-07-11, License - CC BY-SA 4.0

# Importing the library
import pygame

def create_map():
    # Initializing Pygame
    pygame.init()

    # Initializing surface
    surface = pygame.display.set_mode((1280, 720))

    # Initializing color
    color = (255,0,0)

    # Drawing Rectangle
    pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
    pygame.display.flip()
