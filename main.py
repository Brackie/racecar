import pygame
from car import Car
from time import sleep
from obstacle import Obstacle
from physics import PAGE_WIDTH, PAGE_HEIGHT, CAR_WIDTH, CAR_HEIGHT, LANE_MARGIN, COLLISION_ALLOWANCE, NO_OF_LANES, TARMAC, WHITE, BLACK, RED, GREEN, BLUE, WHITE

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

E_ADDOBSTACLE = pygame.USEREVENT + 1
pygame.time.set_timer(E_ADDOBSTACLE, 800)

pygame.init()

clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((PAGE_WIDTH, PAGE_HEIGHT))
pygame.display.set_caption('A Bit Racey')

allSprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

car = Car()
allSprites.add(car)

def setup_scene(): 
    gameDisplay.fill(WHITE)
    lane_width = int((PAGE_WIDTH - (LANE_MARGIN * (NO_OF_LANES - 1)))/NO_OF_LANES)
    lan2_x_offset = (lane_width + LANE_MARGIN)
    lan3_x_offset = (lan2_x_offset + lane_width + LANE_MARGIN)
    pygame.draw.rect(gameDisplay, TARMAC, (0, 0, lane_width, PAGE_HEIGHT))
    pygame.draw.line(gameDisplay, WHITE, (int(lane_width/2), 0), (int(lane_width/2), PAGE_HEIGHT), 2)
    lane2 = pygame.draw.rect(gameDisplay, TARMAC, (lan2_x_offset, 0, lane_width, PAGE_HEIGHT))
    pygame.draw.line(gameDisplay, WHITE, ((lan2_x_offset + int(lane_width/2)), 0), ((lan2_x_offset + int(lane_width/2)), PAGE_HEIGHT), 2)
    lane3 = pygame.draw.rect(gameDisplay, TARMAC, (lan3_x_offset, 0, lane_width, PAGE_HEIGHT))
    pygame.draw.line(gameDisplay, WHITE, ((lan3_x_offset + int(lane_width/2)), 0), ((lan3_x_offset + int(lane_width/2)), PAGE_HEIGHT), 2)
    pygame.display.flip()

def crash():
    display_message('You crashed!')
    sleep(2)
    allSprites.empty()
    obstacles.empty()
    car.reset()
    allSprites.add(car)
    game_loop()

def display_message(message):
    mediumTxt = pygame.font.Font('./resources/innermountingflame.ttf', 40)
    textSurface = mediumTxt.render(message, True, WHITE)
    textRect = textSurface.get_rect()
    textRect.center = (int(PAGE_WIDTH/2), int(PAGE_HEIGHT/2))
    gameDisplay.blit(textSurface, textRect)
    pygame.display.update(textRect)
    

def game_loop():     
    
    gameEnded = False
    pygame.event.clear()

    while not gameEnded:

        setup_scene()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameEnded = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameEnded = True
            elif event.type == E_ADDOBSTACLE:
                obstacle = Obstacle()
                allSprites.add(obstacle)
                obstacles.add(obstacle)

        for obstacle in obstacles:
            if pygame.sprite.spritecollideany(car, obstacles):
                gameEnded = True
                crash()
                break
            else:
                obstacle.move()  

        pressed_keys = pygame.key.get_pressed()
        car.update(pressed_keys)

        allSprites.draw(gameDisplay)
        pygame.display.update()
        clock.tick(30)

game_loop()