import random
import pygame
import pygame.image
import math
from Indstillinger import *


class PlayerClass2(pygame.sprite.Sprite):
    maxSpeed = 10
    rotation = random.randint(0,359) #Giver en tilfældig rotation
    xposition = random.randint(0,1280 ) #Giver et tilfældigt x og y koordinat
    yposition = random.randint(0,720 )
    scalefactor = 50/391 #Skalere vores billede til den størrelse vi vil have det
    points = 0 #Bruges potetielt senere til at holde styre på scoren mellem to spillere
    newrot = 0  # Forhindrer rotationen i at fordobles når vi loader spilleren ind

    def __init__(self):
        super(PlayerClass2, self).__init__()
        self.image = pygame.transform.rotozoom(pygame.image.load("Assets/Cat2.png").convert_alpha(),(self.rotation + 90), self.scalefactor)  # Variabel for billedet med rotation og scale
        self.pos = pygame.math.Vector2(self.xposition, self.yposition)  # Spillerens position i form af en vektor
        self.base_image = self.image #Gør at vi rotere baseimagen i stedet for en allerede roteret billede
        self.hitbox_rect = self.base_image.get_rect(center=self.pos)
        self.rect = self.hitbox_rect.copy()
        self.surf = pygame.Surface((self.scalefactor*391, self.scalefactor*391)) #Vi bruger scalefactor for at gøre det nemmere at justere størrelsen. Vi gange med 441 for at få dens reele størrelse.
        self.shoot = False
        self.shoot_cooldown = 0


    def player2_input (self):
        self.x_velocity = 0
        self.y_velocity = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.x_velocity = -1*self.maxSpeed * math.cos(math.radians(self.rotation)) #Udregning for x værdien ved brug af cosinus
            self.y_velocity = self.maxSpeed * math.sin(math.radians(self.rotation)) #Udregning for y værdien ved brug af sinus
        if keys[pygame.K_DOWN]:
            self.x_velocity = self.maxSpeed * math.cos(math.radians(self.rotation)) #Fjerner -1 for at få den modsatte x værdi ift w keypress
            self.y_velocity = -1*self.maxSpeed * math.sin(math.radians(self.rotation)) #Tilføjer -1 for at få den modsatte y værdi ift w keypress
        if keys[pygame.K_LEFT]:
            self.rotation += 5
            self.newrot += 5  # Opdaterer begge variabler for at både billedets og bevægelses rotation forbliver ens
            Bullet.rotation = self.rotation
        if keys[pygame.K_RIGHT]:
            self.rotation -= 5
            self.newrot -= 5
            Bullet.rotation = self.rotation
        if keys[pygame.K_m]:
            self.shoot = True
            self.is_shooting()
        else:
            self.shoot = False

    def is_shooting(self):
        import Playertest as test
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = SHOOT_COOLDOWN
            spawn_bullet_pos = self.pos
            self.bullet = Bullet(spawn_bullet_pos[0], spawn_bullet_pos[1], self.rotation)
            test.bullet_group.add(self.bullet)
            test.all_sprites_group.add(self.bullet)

    def move2 (self):
        self.image = pygame.transform.rotate(self.base_image, ((self.newrot)))
        self.rect = self.image.get_rect(center=self.hitbox_rect.center)
        self.pos += pygame.math.Vector2(self.x_velocity, self.y_velocity)  # Tilføjer hastigheden til dens position
        self.hitbox_rect.center = self.pos
        self.rect.center = self.hitbox_rect.center
    def update(self):
        self.player2_input() #
        self.move2() #

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

class Bullet(pygame.sprite.Sprite):
    rotation = PlayerClass2.rotation
    def __init__(self, x, y, rotation):
        super().__init__()
        self.image = pygame.image.load("Assets/bullet.png").convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, BULLET_SCALE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.speed =BULLET_SPEED
        self.x_vel = -1*math.cos(self.rotation * (2 * math.pi / 360)) * self.speed
        self.y_vel = math.sin(self.rotation * (2 * math.pi / 360)) * self.speed

    def bullet_movement(self):
        self.x += self.x_vel
        self.y += self.y_vel

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def update(self):
        self.bullet_movement()
