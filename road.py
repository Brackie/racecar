import pygame
from physics import PAGE_WIDTH, PAGE_HEIGHT, CAR_WIDTH, CAR_HEIGHT, LANE_MARGIN, COLLISION_ALLOWANCE, NO_OF_LANES, TARMAC, WHITE, BLACK, RED, GREEN, BLUE, WHITE


class Road(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.gameDisplay = pygame.display.set_mode((PAGE_WIDTH, PAGE_HEIGHT))
        self.road = pygame.Surface((PAGE_WIDTH, PAGE_HEIGHT))

        pygame.display.set_caption('A Bit Racey')

    def draw(self):
        
        self.gameDisplay.fill(WHITE)
        self.road.fill(WHITE)

        lane_width = int((PAGE_WIDTH - (LANE_MARGIN * (NO_OF_LANES - 1)))/NO_OF_LANES)
        lan2_x_offset = (lane_width + LANE_MARGIN)
        lan3_x_offset = (lan2_x_offset + lane_width + LANE_MARGIN)

        pygame.draw.rect(self.road, TARMAC, (0, 0, lane_width, PAGE_HEIGHT))
        pygame.draw.line(self.road, WHITE, (int(lane_width/2), 0), (int(lane_width/2), PAGE_HEIGHT), 2)

        lane2 = pygame.draw.rect(self.road, TARMAC, (lan2_x_offset, 0, lane_width, PAGE_HEIGHT))
        pygame.draw.line(self.road, WHITE, ((lan2_x_offset + int(lane_width/2)), 0), ((lan2_x_offset + int(lane_width/2)), PAGE_HEIGHT), 2)

        lane3 = pygame.draw.rect(self.road, TARMAC, (lan3_x_offset, 0, lane_width, PAGE_HEIGHT))
        pygame.draw.line(self.road, WHITE, ((lan3_x_offset + int(lane_width/2)), 0), ((lan3_x_offset + int(lane_width/2)), PAGE_HEIGHT), 2)

        self.gameDisplay.blit(self.road, self.road.get_rect())
        
        pygame.display.update()

    def move(self):
        self.road.get_rect().move(0, 5)
