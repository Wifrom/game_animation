import pygame
import sys
from person import Player

pygame.init()
clock = pygame.time.Clock()
HEIGHT = 500
WIDTH = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
player = Player()

ground_pos = (0,player.rect.bottom, WIDTH, HEIGHT)

while True:
    screen.fill("light blue")
    pygame.draw.rect(screen, "green", ground_pos )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        player.status = "jump"

    if keys[pygame.K_LCTRL]:
        player.status = "roll"

    if keys[pygame.K_a]:
        player.direction = player.directions[0]
        if player.status == "jump":
            # player.jump_rotate = True
            player.rect.x -= player.speed
        elif player.status == "roll":
            player.rect.x -= player.speed
        else:
            player.status = "runl"


    if keys[pygame.K_d]:
        player.direction = player.directions[1]
        if player.status == "jump":
            player.rect.x += player.speed
        elif player.status == "roll":
            player.rect.x += player.speed
        else:
            player.status = "runr"




    player.main_status_update(screen)

    pygame.draw.rect(screen, "pink", player.rect, width=3)

    clock.tick(12)
    pygame.display.flip()

