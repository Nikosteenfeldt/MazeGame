import pygame
from sys import exit
import os
import math
from Indstillinger import *



pygame.init()



background = pygame.image.load("../GameGame/Assets/Background.jpg").convert()
from Playerclassfile import PlayerClass
player = PlayerClass()
while True:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background, (0,0))
    screen.blit(player.image, player.pos)
    player.update()

    pygame.display.update()
    clock.tick(FPS)