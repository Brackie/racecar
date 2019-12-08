import pygame
from physics import *
from pygame.locals import (
    K_UP,
    K_w,
    K_DOWN,
    K_s,
    K_LEFT,
    K_d,
    K_RIGHT,
    K_a,
)

class Car(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./resources/racecar.png').convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x = (LANE_MARGIN + (CAR_WIDTH * 2))
        self.rect.y = int(PAGE_HEIGHT * 0.8)

        self.vel = 100

    def reset(self):
        self.vel = 100
        self.rect.x = (LANE_MARGIN + (CAR_WIDTH * 2))
        self.rect.y = int(PAGE_HEIGHT * 0.8)

    def update(self, pressed_keys, a, dt):

        self.vel = apply_accelaration(self.vel, a, dt)
        self.ds = int(apply_displacement(self.vel, dt))

        # if pressed_keys[K_UP] or pressed_keys[K_w]:
        #     self.rect.move_ip(0, -self.ds)
        
        # elif pressed_keys[K_DOWN] or pressed_keys[K_s]:
        #     self.rect.move_ip(0, self.ds)

        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            self.rect.move_ip(-self.ds, 0)

        elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            self.rect.move_ip(self.ds, 0)

        if self.rect.left < LANE_MARGIN:
            self.rect.left = LANE_MARGIN

        if self.rect.right > (PAGE_WIDTH - LANE_MARGIN):
            self.rect.right = (PAGE_WIDTH - LANE_MARGIN)

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= PAGE_HEIGHT:
            self.rect.bottom = PAGE_HEIGHT

