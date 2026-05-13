import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))

class Obstacles:
    def __init__(self, coords):
        self.rect = pygame.Rect(*coords)
        self.is_collision = False

    def draw(self, display):
        pygame.draw.rect(display, "red", self.rect)

    def change_is_collision_status(self, player_obj):
        if player_obj.rect.colliderect(self.rect):
            self.is_collision = True
        else:
            self.is_collision = False