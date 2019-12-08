import pygame
from car import Car
from road import Road
from bush import Bush
from time import sleep, time
from obstacle import Obstacle
from physics import *

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
bushes = pygame.sprite.Group()

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

    a = 0
    t0 = time() 

    while not gameEnded:
        road.draw()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameEnded = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameEnded = True

                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    a = ACCELARATION
                
                elif (
                        event.key == pygame.K_LEFT or 
                        event.key == pygame.K_a or 
                        event.key == pygame.K_RIGHT or 
                        event.key == pygame.K_d
                    ):
                    a = 0

            elif event.type == pygame.KEYUP:
                if (
                    event.key == pygame.K_UP or 
                    event.key == pygame.K_DOWN or 
                    event.key == pygame.K_w or 
                    event.key == pygame.K_s or 
                    event.key == pygame.K_LEFT or 
                    event.key == pygame.K_a or 
                    event.key == pygame.K_RIGHT or 
                    event.key == pygame.K_d
                ):
                    a = 0
                    
            elif event.type == E_ADDOBSTACLE:
                obstacle = Obstacle()
                bush = Bush()

                allSprites.add(bush)
                bushes.add(bush)

                if not car.rect.colliderect(obstacle.rect):                   
                    allSprites.add(obstacle)
                    obstacles.add(obstacle)

        t1 = time()
        dt = (t1 - t0)
        t0 = t1

        pressed_keys = pygame.key.get_pressed()

        car.update(pressed_keys, ACCELARATION, dt)

        for obstacle in obstacles:
            if obstacle.rect.colliderect(car.rect):
                gameEnded = True
                crash()
                break
            else:
                obstacle.move(ACCELARATION, dt)  
        
        for bush in bushes:
            bush.move(ACCELARATION, dt)
            
        road.move(ACCELARATION, dt)

        allSprites.draw(road.gameDisplay)
        
        pygame.display.update()

        clock.tick(30)

game_loop()