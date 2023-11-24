# lab9
# task 1 Clock Mickey Mouse

import pygame
import sys
import math
from datetime import datetime
pygame.init()

W, H = 829, 836
WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode( (W, H))
pygame.display.set_caption("Mickey Clock")
pygame.display.set_icon(pygame.image.load("E:\SUBJECT-My study))\III-SEMESTER\PP2\labs\lab9(1)/mickeyclock.jpeg"))

x = W//2
y = H//2

image = pygame.image.load("E:\SUBJECT-My study))\III-SEMESTER\PP2\labs\lab9(1)/main-clock.png")
minute_hand= pygame.image.load("E:\SUBJECT-My study))\III-SEMESTER\PP2\labs\lab9(1)/right-hand.png")
second_hand = pygame.image.load("E:\SUBJECT-My study))\III-SEMESTER\PP2\labs\lab9(1)/left-hand.png")

mickey_rect = image.get_rect(center=(x,y))

clock = pygame.time.Clock()
FPS = 1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    current = datetime.now()
    hour = current.hour
    minute = current.minute
    second = current.second
    
    min_angle = -(minute % 60)*6
    sec_angle = -(second % 60)*6

    mickey_min = pygame.transform.rotate(minute_hand, min_angle)
    mickey_sec = pygame.transform.rotate(second_hand, sec_angle)

    minutes_rect = mickey_min.get_rect(center=mickey_rect.center)
    seconds_rect = mickey_sec.get_rect(center=mickey_rect.center)

    screen.fill(WHITE)
    screen.blit(image, (0,0))
    screen.blit(mickey_min, minutes_rect.topleft)
    screen.blit(mickey_sec, seconds_rect.topleft)

    # pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)


