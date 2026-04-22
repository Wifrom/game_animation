import pygame
import math

pygame.init()
screen = pygame.display.set_mode((600, 400))


class Ball:
    g = 5

    def __init__(self, angle, event_pos, gun_pos):
        distance = math.sqrt((event_pos[0] - gun_pos[0])**2 + (event_pos[1] - gun_pos[1])**2)
        self.v = 39 + 0.073 * distance
        self.alpha = angle
        self.vx = -self.v * math.sin(angle)
        self.vy = -self.v * math.cos(angle)
        self.ball = pygame.Rect(200, 400, 20, 20)
        self.y0 = self.ball.center[1]
        self.x0 = self.ball.center[0]
        self.a = 1
        self.t = 0
        self.t0 = 0

    def change_coords(self):
        self.ball.center = (self.x0 + self.vx * (self.t - self.t0),
                            self.y0 - self.vy * (self.t - self.t0) + self.g * (self.t - self.t0) ** 2 / 2)

        self.t += 0.3

    def draw_ball(self, display):
        pygame.draw.circle(display, 'white', self.ball.center, self.ball.w // 2)
