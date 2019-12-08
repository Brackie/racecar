import pygame
from random import randint, choice
from physics import *


class Bush(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.x = choice([0, (PAGE_WIDTH - LANE_MARGIN)])
        self.y = 0

        self.image = pygame.image.load("./resources/bush.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.vel = 100

    def move(self, a, dt):
        self.vel = apply_accelaration(self.vel, a, dt)
        self.dy = int(apply_displacement(self.vel, dt))
        self.rect.move_ip(0, self.dy)
        if self.rect.bottom < 0:
            self.kill()





