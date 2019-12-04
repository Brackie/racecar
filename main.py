import pygame
from car import Car
from road import Road
from time import sleep
from obstacle import Obstacle
from physics import PAGE_WIDTH, PAGE_HEIGHT, CAR_WIDTH, CAR_HEIGHT, LANE_MARGIN, COLLISION_ALLOWANCE, NO_OF_LANES, TARMAC, WHITE, BLACK, RED, GREEN, BLUE, WHITE

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

E_ADDOBSTACLE = pygame.USEREVENT + 1
pygame.time.set_timer(E_ADDOBSTACLE, 600)

pygame.init()

clock = pygame.time.Clock()

allSprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

road = Road()

car = Car()
allSprites.add(car)


def crash():
    display_message('You crashed!')
    sleep(1)
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
    road.gameDisplay.blit(textSurface, textRect)
    pygame.display.update(textRect)
    

def game_loop():     
    
    gameEnded = False
    pygame.event.clear()

    while not gameEnded:

        road.draw()

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

        road.move()

        pressed_keys = pygame.key.get_pressed()
        car.update(pressed_keys)

        allSprites.draw(road.gameDisplay)
        pygame.display.update()

        clock.tick(30)

game_loop()