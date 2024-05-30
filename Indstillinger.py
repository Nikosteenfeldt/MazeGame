import pygame

screenWidth = 1280    #Gør det nemmere at ændre skærmbredden senere
screenHeight = 720    #Gør det nemmere at ændre skærmhøjden senere
FPS = 60

SHOOT_COOLDOWN = 20
BULLET_SCALE = 20/138
BULLET_SPEED = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Skaber vores skærm som en variabel
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

