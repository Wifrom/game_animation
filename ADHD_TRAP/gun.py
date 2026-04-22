import pygame
import math

pygame.init()
screen = pygame.display.set_mode((600, 400))


class Gun:
    def __init__(self, gun_img_path, coords):
        self.cannon_img = pygame.image.load(gun_img_path).convert_alpha()
        self.cannon_img_original = pygame.transform.scale(self.cannon_img, (400, 200))
        self.cannon_img = self.cannon_img_original.copy()
        self.rect = self.cannon_img.get_rect(center=(200, 400))

        self.coords = coords

    def on_mouse_motion(self, position):
        self.coords = list(position)

    def gun_angle_count(self):
        if self.rect.center[1] - self.coords[1] != 0:
            tan = (self.coords[0] - self.rect.center[0]) / (self.rect.center[1] - self.coords[1])
            angle_in_degrees = math.atan(tan)
            angle = angle_in_degrees * 180 / math.pi
            if self.rect.center[1] - self.coords[1] > 0:
                self.cannon_img = pygame.transform.rotate(self.cannon_img_original, -angle).convert_alpha()
            else:
                self.cannon_img = pygame.transform.rotate(self.cannon_img_original, -angle + 180).convert_alpha()
                # ToDo изменить на tg
    def get_gun_angle(self):
        dx = self.coords[0] - self.rect.center[0]
        dy = self.coords[1] - self.rect.center[1]
        angle_in_radian = math.atan2(-dx, dy)
        angle_in_degrees = math.degrees(angle_in_radian)

        if angle_in_degrees < 0:
            angle_in_degrees += 360

        return angle_in_degrees




    def show_gun(self, display):
        self.rect = self.cannon_img.get_rect(center=(200, 400))
        display.blit(self.cannon_img, self.rect)

    def rotate_by_keyboard(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.coords[0] += 3
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.coords[0] -= 3
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.coords[1] -= 3
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.coords[1] += 3