import random
import pygame
import pygame.image
import math
from Indstillinger import screen



class PlayerClass:
    maxSpeed = 10
    rotation = random.randint(0,359) #Giver en tilfældig rotation
    xposition = random.randint(0,1280 ) #Giver et tilfældigt x og y koordinat
    yposition = random.randint(0,720 )
    scalefactor = 50/441 #Skalere vores billede til den størrelse vi vil have det
    points = 0 #Bruges potetielt senere til at holde styre på scoren mellem to spillere
    newrot = 0 #Forhindrer rotationen i at fordobles når vi loader spilleren ind
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.rotozoom(pygame.image.load("../GameGame/Assets/Cat.png").convert_alpha(),(self.rotation+90),self.scalefactor) #Variabel for billedet
        self.pos = pygame.math.Vector2(self.xposition, self.yposition)  # Spillerens position i form af en vektor
        self.base_image = self.image
        self.hitbox_rect = self.base_image.get_rect(center = self.pos)
        self.rect = self.hitbox_rect.copy()



    def player_input (self):
        self.x_velocity = 0
        self.y_velocity = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x_velocity = -1*self.maxSpeed * math.cos(math.radians(self.rotation)) #Udregning for x værdien ved brug af cosinus
            self.y_velocity = self.maxSpeed * math.sin(math.radians(self.rotation)) #Udregning for y værdien ved brug af sinus
        if keys[pygame.K_s]:
            self.x_velocity = self.maxSpeed * math.cos(math.radians(self.rotation)) #Fjerner -1 for at få den modsatte x værdi ift w keypress
            self.y_velocity = -1*self.maxSpeed * math.sin(math.radians(self.rotation)) #Tilføjer -1 for at få den modsatte y værdi ift w keypress
        if keys[pygame.K_a]:
            self.rotation += 5
            self.newrot += 5  #Opdaterer begge variabler for at både billedets og bevægelses rotation forbliver ens
        if keys[pygame.K_d]:
            self.rotation -= 5
            self.newrot -= 5



    def move (self):
        self.image = pygame.transform.rotate(self.base_image, ((self.newrot)))
        self.rect = self.image.get_rect(center = self.hitbox_rect.center)
        self.pos += pygame.math.Vector2(self.x_velocity, self.y_velocity) #Tilføjer hastigheden til dens position
        self.hitbox_rect.center = self.pos
        self.rect.center = self.hitbox_rect.center


    def update(self):
        self.player_input() #
        self.move() #








