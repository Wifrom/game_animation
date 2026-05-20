import pygame
import sys
from person import Player
from obstacles import Obstacles

pygame.init()
clock = pygame.time.Clock()
HEIGHT = 500
WIDTH = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
player = Player()

ground_pos = (0, player.rect.bottom, WIDTH, HEIGHT)

obstacles = [Obstacles((400, 270, 20, 10)), Obstacles((700, 220, 20, 10))]

button_width = 150
button_heigh = 100

points = [(WIDTH / 2 - button_width / 2, HEIGHT / 2 - button_heigh / 2),
          (WIDTH / 2 - button_width / 2, HEIGHT / 2 + button_heigh / 2),
          (WIDTH / 2 + button_width / 2, HEIGHT / 2)]

x0 = points[0][0]
ku = (points[0][1] - points[2][1]) / (points[0][0] - points[2][0])
kd = (points[1][1] - points[2][1]) / (points[1][0] - points[2][0])
lu = points[2][1] - points[2][0] * ku
ld = HEIGHT / 2 + HEIGHT / 2 - lu
print(ku, kd, lu, ld)
scene = 1

def click_analys(x, y):
    if (y - ku*x - lu > 0) and (y - kd * x - ld < 0) and (x > x0):
        return True
    return False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and scene == 1:
          # print(event.pos)
            if click_analys(event.pos[0], event.pos[1]):
                scene = 2


    if scene == 1:
        screen.fill("blue")
        pygame.draw.polygon(screen, "green", points)
    else:
        screen.fill("light blue")
        pygame.draw.rect(screen, "green", ground_pos)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and player.status in ("runr", "runl", "stay"):
            player.status = "jump"

        if keys[pygame.K_LCTRL] and player.status in ("runr", "runl", "stay"):
            player.status = "roll"

        if keys[pygame.K_a] and player.is_obstacles == False:
            player.direction = player.directions[0]
            if player.status == "jump":
                # player.jump_rotate = True
                player.rect.x -= player.speed
                player.collision_rect.x -= player.speed
            elif player.status == "roll":
                player.rect.x -= player.speed
                player.collision_rect.x -= player.speed
            else:
                player.status = "runl"

        if keys[pygame.K_d] and player.is_obstacles == False:
            player.direction = player.directions[1]
            if player.status == "jump":
                player.rect.x += player.speed
                player.collision_rect.x += player.speed
            elif player.status == "roll":
                player.rect.x += player.speed
                player.collision_rect.x += player.speed
            else:
                player.status = "runr"

        player.change_collision_status(obstacles)

        player.main_status_update(screen)

        pygame.draw.rect(screen, "pink", player.rect, width=5)
        pygame.draw.rect(screen, "blue", player.collision_rect, width=3)

        for o in obstacles:
            o.draw(screen)
            o.change_is_collision_status(player)
            print(o.is_collision)

    clock.tick(12)
    pygame.display.flip()
