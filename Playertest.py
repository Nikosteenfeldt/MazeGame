import pygame
from sys import exit
import os
import math
from Indstillinger import *
from Playerclassfile import *

pygame.init()

background = pygame.image.load("Assets/Background.jpg").convert()
from Playerclassfile import PlayerClass
player = PlayerClass()
all_sprites_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

all_sprites_group.add(player)

while True:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            pygame.quit()
            exit()

    screen.blit(background, (0,0)) #Tegner baggrunden
    all_sprites_group.draw(screen) #Tegner ting ig
    all_sprites_group.update()

    pygame.display.update()
    clock.tick(FPS)