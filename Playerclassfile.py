import random
import pygame
import pygame.image
import math

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
        self.image = pygame.transform.rotozoom(pygame.image.load("Assets/Cat.png").convert_alpha(),(self.rotation+90),self.scalefactor)
        self.pos = pygame.math.Vector2(self.xposition, self.yposition)

    def player_input (self):
        self.x_velocity = 0
        self.y_velocity = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x_velocity = -1*self.maxSpeed * math.cos(math.radians(self.rotation))
            self.y_velocity = self.maxSpeed * math.sin(math.radians(self.rotation))
        if keys[pygame.K_s]:
            self.x_velocity = self.maxSpeed * math.cos(math.radians(self.rotation))
            self.y_velocity = -1*self.maxSpeed * math.sin(math.radians(self.rotation))


    def move (self):
        self.pos += pygame.math.Vector2(self.x_velocity, self.y_velocity)

    def update(self):
        self.player_input()
        self.move()







