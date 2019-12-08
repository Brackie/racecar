import pygame
from random import randint, choice
from physics import *

car_choices = [
    "obstacle_1.png",
    "obstacle_2.png",
    "obstacle_3.png",
    "obstacle_4.png"
]

lane_width = int((PAGE_WIDTH - (LANE_MARGIN * (NO_OF_LANES + 1)))/NO_OF_LANES)
lane_choices = [
    [LANE_MARGIN, (LANE_MARGIN + (lane_width - CAR_WIDTH))],
    [(lane_width + (LANE_MARGIN * 2)), (((LANE_MARGIN + lane_width) * 2) - CAR_WIDTH)]
]

class Obstacle(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        lane_choice = choice(lane_choices)
        image_path = "./resources/{}".format(choice(car_choices))

        self.x = randint(lane_choice[0], lane_choice[1])
        self.y = (0 + CAR_HEIGHT)

        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.vel = randint(200, 300)

    def move(self, a, dt):
        self.vel = apply_accelaration(self.vel, a, dt)
        self.dy = int(apply_displacement(self.vel, dt))
        self.rect.move_ip(0, self.dy)
        if self.rect.bottom < 0:
            self.kill()





