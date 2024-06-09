import random
import pygame
import pygame.image
import math
from Indstillinger import *


class PlayerClass(pygame.sprite.Sprite):
    maxSpeed = 10
    size = 50
    rotation = random.randint(0,359) #Giver en tilfældig rotation
    xposition = random.randint(0,1280 ) #Giver et tilfældigt x og y koordinat
    yposition = random.randint(0,720 )
    scalefactor = 50/441 #Skalere vores billede til den størrelse vi vil have det
    points = 0 #Bruges potetielt senere til at holde styre på scoren mellem to spillere
    newrot = 0  # Forhindrer rotationen i at fordobles når vi loader spilleren ind

    def __init__(self):
        super().__init__()
        self.image = pygame.transform.rotozoom(pygame.image.load("Assets/Cat.png").convert_alpha(),(self.rotation + 90), self.scalefactor)  # Variabel for billedet
        self.pos = pygame.math.Vector2(self.xposition, self.yposition)  # Spillerens position i form af en vektor
        self.base_image = self.image
        self.hitbox_rect = self.base_image.get_rect(center=self.pos)
        self.rect = self.hitbox_rect.copy()
        self.shoot = False
        self.shoot_cooldown = 0


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
            self.newrot += 5  # Opdaterer begge variabler for at både billedets og bevægelses rotation forbliver ens
            Bullet.rotation = self.rotation
        if keys[pygame.K_d]:
            self.rotation -= 5
            self.newrot -= 5
            Bullet.rotation = self.rotation
        if keys[pygame.K_q]:
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

    def bordercontrol(self):
        hypotenuse = 25*math.sqrt(2)
        yderstx = abs(hypotenuse * math.cos(math.radians(self.rotation+45)))
        ydersty = abs(hypotenuse * math.sin(math.radians(self.rotation+45)))
        inderstx = abs(hypotenuse * math.cos(math.radians(self.rotation - 45)))
        indersty = abs(hypotenuse * math.sin(math.radians(self.rotation - 45)))
        xlist = [yderstx, inderstx]
        ylist = [ydersty, indersty]
        xpunkt = max(xlist)
        ypunkt = max(ylist)
        if self.hitbox_rect.centerx + xpunkt > screenHeight:
            self.xposition = screenWidth - xpunkt
            self.pos = (self.xposition, self.hitbox_rect.centery)
        if self.hitbox_rect.centery + ypunkt > screenHeight:
            self.yposition = screenHeight - ypunkt
            self.pos = (self.hitbox_rect.centerx, self.yposition)
        if self.hitbox_rect.centerx - xpunkt < 0:
            self.xposition = xpunkt
            self.pos = (self.xposition, self.hitbox_rect.centery)
        if self.hitbox_rect.centery - ypunkt < 0:
            self.yposition = ypunkt
            self.pos = (self.hitbox_rect.centerx, self.yposition)


    def move (self):
        self.image = pygame.transform.rotate(self.base_image, ((self.newrot)))
        self.rect = self.image.get_rect(center=self.hitbox_rect.center)
        self.pos += pygame.math.Vector2(self.x_velocity, self.y_velocity)  # Tilføjer hastigheden til dens position
        self.hitbox_rect.center = self.pos
        self.rect.center = self.hitbox_rect.center
    def update(self):
        self.player_input() #
        self.bordercontrol()
        self.move() #

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

class Bullet(pygame.sprite.Sprite):
    rotation = PlayerClass.rotation
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