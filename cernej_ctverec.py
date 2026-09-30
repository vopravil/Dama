# cernej_ctverec.py
import pygame

class CernejCtverec:
    def __init__(self, x, y, velikost=80):
        self.x = x
        self.y = y
        self.velikost = velikost
        self.barva = (0, 0, 0)
        self.rectttt = pygame.Rect(self.x, self.y, self.velikost, self.velikost)

    def kresli(self, screen):
        pygame.draw.rect(screen, self.barva, self.rect)

    def klik(self, pozice_mysi):
        if self.rect.collidepoint(pozice_mysi):
            self.zmen_barvu()

    def zmen_barvu(self):
        if self.barva == (0, 0, 0):
            self.barva = (255, 0, 0)  # červená
        else:
            self.barva = (0, 0, 0)    # zpět na černou