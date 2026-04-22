import pygame
import sys
import math

pygame.init()

clock = pygame.time.Clock()
HEIGHT = 500
WIDTH = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))

ball = pygame.Rect(100, 400, 20, 20)

v = 50
alpha = 30 * math.pi / 180
vx = v * math.cos(alpha)
vy = v * math.sin(alpha)
y0 = ball.center[1]
x0 = ball.center[0]
a = 1
t = 0
t0 = 0
g = 5


while True:
    # screen.fill("#cccccc")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball.center = (x0 + vx * (t - t0),
                   y0 - vy * (t - t0) + g * (t - t0) ** 2 / 2)
    print(ball.center)

    pygame.draw.circle(screen, "blue", ball.center, 10)

    t += 0.3
    clock.tick(80)
    pygame.display.flip()
