import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))

class Obstacles:
    def __init__(self, coords):
        self.rect = pygame.Rect(*coords)




    def draw(self, display):
        pygame.draw.rect(display, "red", self.rect)