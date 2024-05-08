import pygame
from sys import exit
import os
import math
from PlayerClass import PlayerClass #Gør vi har adgang til værdierne i PlayerClass

screenWidth = 1280    #Gør det nemmere at ændre skærmbredden senere
screenHeight = 720    #Gør det nemmere at ændre skærmhøjden senere

pygame.init()

playerObject = PlayerClass
screen = pygame.display.set_mode((screenWidth, screenHeight))
while True:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()