import pygame
from random import randint, choice
from physics import PAGE_WIDTH, PAGE_HEIGHT, CAR_WIDTH, CAR_HEIGHT, LANE_MARGIN, NO_OF_LANES, RED, GREEN, BLUE, WHITE

car_choices = [
    "obstacle_1.png",
    "obstacle_2.png",
    "obstacle_3.png",
    "obstacle_4.png"
]

lane_width = int((PAGE_WIDTH - (LANE_MARGIN * (NO_OF_LANES - 1)))/NO_OF_LANES)
lane_choices = [
    [0, (lane_width - CAR_WIDTH)],
    [(lane_width + LANE_MARGIN), (((lane_width * 2) + LANE_MARGIN) - CAR_WIDTH)],
    [(lane_width + LANE_MARGIN), (((lane_width * 2) + LANE_MARGIN) - CAR_WIDTH)],
    [((lane_width + LANE_MARGIN) * 2), (PAGE_WIDTH - CAR_WIDTH)]
]

class Obstacle(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        lane_choice = choice(lane_choices)
        image_path = "./resources/{}".format(choice(car_choices))

        self.x = randint(lane_choice[0], lane_choice[1])
        self.y =  randint(0, int(PAGE_HEIGHT * 0.3))

        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.yVel = randint(5, 10)

    def move(self):
        self.rect.move_ip(0, self.yVel)
        if self.rect.bottom < 0:
            self.kill()





