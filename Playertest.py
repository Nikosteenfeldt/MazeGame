from sys import exit
from Playerclassfile import *
from Playerclassfile2 import *
from Mazes import maze as maze

pygame.init()

player = PlayerClass()
player_2 = PlayerClass2()
all_sprites_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

all_sprites_group.add(player)
all_sprites_group.add(player_2)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define maze (0 = wall, 1 = path)
# Draw the maze
def draw_maze():
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 0:
                pygame.draw.rect(screen, BLACK, (x*50, y*50, 50, 50))
            elif maze[y][x] == 1:
                pygame.draw.rect(screen, WHITE, (x*50, y*50, 50, 50))

while True:
    screen.fill(BLACK) #Gør skærmen sort
    draw_maze() #Tegner mazen ind
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]: #Gør at man kan stoppe progammet
            pygame.quit() #Stopper pygame
            exit() #Lukker programmet
    all_sprites_group.draw(screen) #Tegner ting ind
    all_sprites_group.update()


    pygame.display.update()
    clock.tick(FPS)