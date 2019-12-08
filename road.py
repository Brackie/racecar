import pygame
from physics import *


class Road(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.gameDisplay = pygame.display.set_mode((PAGE_WIDTH, PAGE_HEIGHT))
        self.road = pygame.Surface((PAGE_WIDTH, PAGE_HEIGHT))

        self.vel = 100

        pygame.display.set_caption('A Bit Racey')

    def draw(self):
        
        self.gameDisplay.fill(WHITE)
        self.road.fill(WHITE)
        self.road.fill(BROWN, pygame.Rect(0, 0, LANE_MARGIN, PAGE_HEIGHT))
        self.road.fill(BROWN, pygame.Rect((PAGE_WIDTH - LANE_MARGIN), 0, LANE_MARGIN, PAGE_HEIGHT))

        lane_width = int((PAGE_WIDTH - (LANE_MARGIN * (NO_OF_LANES + 1)))/NO_OF_LANES)
        lan2_x_offset = (lane_width + (LANE_MARGIN * 2))

        pygame.draw.rect(self.road, TARMAC, (LANE_MARGIN, 0, lane_width, PAGE_HEIGHT))
        pygame.draw.line(self.road, WHITE, ((LANE_MARGIN + (int(lane_width/2))), 0), ((LANE_MARGIN + int(lane_width/2)), PAGE_HEIGHT), 2)

        pygame.draw.rect(self.road, TARMAC, (lan2_x_offset, 0, lane_width, PAGE_HEIGHT))
        pygame.draw.line(self.road, WHITE, ((lan2_x_offset + int(lane_width/2)), 0), ((lan2_x_offset + int(lane_width/2)), PAGE_HEIGHT), 2)

        self.gameDisplay.blit(self.road, self.road.get_rect())
        
        pygame.display.update()

    def move(self, a, dt):
        self.vel = apply_accelaration(self.vel, a, dt)
        self.dy = int(apply_displacement(self.vel, dt))
        self.road.scroll(0, self.dy)
