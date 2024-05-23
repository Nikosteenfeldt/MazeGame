import pygame
from sys import exit
from Indstillinger import *

pygame.init()

background = pygame.image.load("Assets/Background.jpg").convert()
from Playerclassfile import PlayerClass
player = PlayerClass()
while True:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            pygame.quit()
            exit()
    screen.blit(background, (0,0))
    screen.blit(player.image, player.rect)
    player.update()

    pygame.display.update()
    clock.tick(FPS)