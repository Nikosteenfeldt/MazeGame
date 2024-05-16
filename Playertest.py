import pygame
from sys import exit
import os
import math
import Assets
  #Gør vi har adgang til værdierne i PlayerClass

screenWidth = 1280    #Gør det nemmere at ændre skærmbredden senere
screenHeight = 720    #Gør det nemmere at ændre skærmhøjden senere
FPS = 60

pygame.init()


screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

background = pygame.image.load("Assets/Background.jpg").convert()
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
    pygame.display.update()
    clock.tick(FPS)