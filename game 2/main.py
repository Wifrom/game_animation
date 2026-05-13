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

ground_pos = (0,player.rect.bottom, WIDTH, HEIGHT)

obstacles = [Obstacles((400, 270,20, 10)), Obstacles((700, 220,20, 10))]


while True:
    screen.fill("light blue")
    pygame.draw.rect(screen, "green", ground_pos )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and player.status in ("runr","runl", "stay"):
        player.status = "jump"


    if keys[pygame.K_LCTRL] and player.status in ("runr","runl", "stay"):
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

