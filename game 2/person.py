import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))


class Player:
    directions = ("left", "right")

    def __init__(self):

        self.anim_tick = 0
        self.rect = pygame.Rect(200, 200, 80, 80)
        self.collision_rect = pygame.Rect(220, 200, 40, 80)
        self.jump_tick = 0
        self.jump_force = 5
        self.status = "stay"
        self.speed = 15
        self.roll_speed = 10
        self.roll_tick = 0
        self.load_imgs()
        self.direction = self.directions[1]

    def load_imgs(self):
        self.runright_images = (pygame.transform.scale(pygame.image.load("img/runright1.png"), (80, 80)),
                                pygame.transform.scale(pygame.image.load("img/runright2.png"), (80, 80)),
                                pygame.transform.scale(pygame.image.load("img/runright3.png"), (80, 80)),
                                pygame.transform.scale(pygame.image.load("img/runright4.png"), (80, 80)),
                                pygame.transform.scale(pygame.image.load("img/runright5.png"), (80, 80)),
                                pygame.transform.scale(pygame.image.load("img/runright6.png"), (80, 80)))

        self.runleft_images = (pygame.transform.scale(pygame.image.load("img/runleft1.png"), (80, 80)),
                               pygame.transform.scale(pygame.image.load("img/runleft2.png"), (80, 80)),
                               pygame.transform.scale(pygame.image.load("img/runleft3.png"), (80, 80)),
                               pygame.transform.scale(pygame.image.load("img/runleft4.png"), (80, 80)),
                               pygame.transform.scale(pygame.image.load("img/runleft5.png"), (80, 80)),
                               pygame.transform.scale(pygame.image.load("img/runleft6.png"), (80, 80)))

        self.jump_images_right = (pygame.transform.scale(pygame.image.load("img/jump1.png"), (80, 80)),
                                  pygame.transform.scale(pygame.image.load("img/jump2.png"), (80, 80)),
                                  pygame.transform.scale(pygame.image.load("img/jump3.png"), (80, 80)),
                                  pygame.transform.scale(pygame.image.load("img/jump4.png"), (80, 80)),
                                  pygame.transform.scale(pygame.image.load("img/jump5.png"), (80, 80)),
                                  pygame.transform.scale(pygame.image.load("img/jump6.png"), (80, 80)))

        self.jump_images_left = list(map(pygame.transform.flip, self.jump_images_right,
                                         [True] * len(self.jump_images_right), [False] * len(self.jump_images_right)))

        self.roll_images_right = (pygame.transform.scale(pygame.image.load("img/roll1.png"), (80, 80)),
                                  pygame.transform.scale(pygame.image.load("img/roll2.png"), (80, 80)),
                                  pygame.transform.scale(pygame.image.load("img/roll3.png"), (80, 80)),
                                  pygame.transform.scale(pygame.image.load("img/roll4.png"), (80, 80)),
                                  pygame.transform.scale(pygame.image.load("img/roll5.png"), (80, 80)),
                                  pygame.transform.scale(pygame.image.load("img/roll6.png"), (80, 80)))

        self.roll_images_left = list(
            map(pygame.transform.flip, self.roll_images_right, [True] * len(self.roll_images_right),
                [False] * len(self.roll_images_right)))

    def main_status_update(self, display):
        self.anim_tick %= 6
        if self.status == "stay":
            display.blit(self.jump_images_left[5], self.rect)

        if self.status == "jump":
            if self.jump_tick == 10:
                self.jump_tick = 0
            self.jump(display)
            self.jump_tick += 1
            if self.jump_tick == 10:
                self.status = "stay"

        if self.status == "roll":
            if self.roll_tick == 10:
                self.roll_tick = 0
            self.roll(display)
            self.roll_tick += 1
            if self.roll_tick == 10:
                self.status = "stay"

        if self.status == "runr":
            self.draw_runright(display)
            self.rect.x += self.speed
            self.collision_rect.x += self.speed
            self.status = "stay"
            self.anim_tick += 1

        if self.status == "runl":
            self.draw_runleft(display)
            self.rect.x -= self.speed
            self.collision_rect.x -= self.speed
            self.anim_tick += 1
            self.status = "stay"

    def draw_runright(self, display):
        display.blit(self.runright_images[self.anim_tick], self.rect)

    def draw_runleft(self, display):
        display.blit(self.runleft_images[self.anim_tick], self.rect)

    def anim_tick_update(self):
        self.anim_tick += 1
        self.anim_tick %= 6

    def jump(self, display):
        if self.direction == self.directions[0]:
            jump_images = self.jump_images_left
        else:
            jump_images = self.jump_images_right

        if self.jump_tick == 0:
            display.blit(jump_images[0], self.rect)

        if self.jump_tick in (1, 2):
            self.rect.y -= self.jump_force
            self.collision_rect.y -= self.jump_force
            display.blit(jump_images[1], self.rect)

        if self.jump_tick in (3, 4):
            self.rect.y -= self.jump_force
            self.collision_rect.y -= self.jump_force
            display.blit(jump_images[2], self.rect)

        if self.jump_tick == 5:
            display.blit(jump_images[2], self.rect)

        if self.jump_tick in (6, 7):
            self.rect.y += 2 * self.jump_force
            self.collision_rect.y += 2 * self.jump_force
            display.blit(jump_images[3], self.rect)

        if self.jump_tick == 8:
            display.blit(jump_images[4], self.rect)

        if self.jump_tick == 9:
            display.blit(jump_images[5], self.rect)

    def roll(self, display):
        if self.direction == self.directions[0]:
            roll_images = self.roll_images_left
        else:
            roll_images = self.roll_images_right
        if self.roll_tick == 0:
            self.rect.y += 10
            self.collision_rect.h -= 40
            self.collision_rect.y += 40
            display.blit(roll_images[0], self.rect)

        if self.roll_tick in (1, 2):
            display.blit(roll_images[1], self.rect)

        if self.roll_tick in (3, 4):
            display.blit(roll_images[2], self.rect)

        if self.roll_tick == 5:
            display.blit(roll_images[2], self.rect)

        if self.roll_tick in (6, 7):
            display.blit(roll_images[3], self.rect)

        if self.roll_tick == 8:
            self.rect.y -= 10
            self.collision_rect.h += 40
            self.collision_rect.y -= 40
            display.blit(roll_images[4], self.rect)
