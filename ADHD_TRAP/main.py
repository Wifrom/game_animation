import pygame
import sys
import math
import random
import colorsys
from ADHD_TRAP.gun import Gun
pygame.init()
from ADHD_TRAP.ball import Ball

pygame.mixer.music.load("gamemusic1.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

bg_img = pygame.image.load("background.jpg")
bg_img = pygame.transform.scale(bg_img, (900, 900 *bg_img.get_height()/ bg_img.get_width() ))

clock = pygame.time.Clock()
METEOR_RADIUS = 35

gun = Gun("../img/cannon.png", [400, 300])


class Metiors:
    def __init__(self):
        gap = random.randint(-80, 20)
        self.speed = random.randint(5, 8)
        self.rect = pygame.Rect((WIDTH + 70, HEIGHT / 2 - 70 + gap, 70, 70, ))

        h = random.random()
        l = 0.5
        s = 1


        rgb = colorsys.hls_to_rgb(h, l, s)
        self.color = (int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))
        self.not_collisions = True






time = 1
HEIGHT = 500
WIDTH = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
first_metior = Metiors()
first_metior.speed = 2
metiors = [first_metior]

ball = None
balls = []

while True:
    screen.fill("light blue")
    screen.blit(bg_img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            gun.on_mouse_motion(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            new_ball = Ball(math.pi / 180 * gun.get_gun_angle(), event.pos, gun.rect.center)
            balls.append(new_ball)
    gun.gun_angle_count()
    gun.show_gun(screen)
    if not time % 200:
        metiors.append(Metiors())
    for m in metiors:
        if time % 2:
            m.rect.left -= m.speed
        pygame.draw.circle(screen, m.color, m.rect.center, METEOR_RADIUS)
        for b in balls:
            if m.rect.colliderect(b.ball):
                m.not_collisions = False

    metiors = [m for m in metiors if (m.rect.right > 0  and m.not_collisions)]

    for b in balls:
        b.change_coords()
        b.draw_ball(screen)


    time += 1
    clock.tick(80)
    pygame.display.flip()