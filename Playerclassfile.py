import random

import pygame.image


class PlayerClass:
    maxSpeed = 10
    rotation = random.randint(0,359)
    xposition = random.randint(0,1280 )
    yposition = random.randint(0,720 )
    scalefactor = 50/441
    color = (0, 128.5, 255)
    points = 0
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.rotozoom(pygame.image.load("Assets/Cat.png").convert_alpha(),0,self.scalefactor)
        self.pos = pygame.math.Vector2(self.xposition, self.yposition)



