import pygame
from Playerclassfile import *
player = PlayerClass

maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


if player.check_collision(maze):
    player.rect = player.old_rect


    def check_collision(self, maze):
        for y in range(len(maze)):
            for x in range(len(maze[y])):
                if maze[y][x] == 0:
                    wall_rect = pygame.Rect(x*50, y*50, 50, 50)
                    if self.rect.colliderect(wall_rect):
                        return True
        return False

# Draw the maze
def draw_maze():
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 0:
                pygame.draw.rect(screen, BLACK, (x*50, y*50, 50, 50))
            elif maze[y][x] == 1:
                pygame.draw.rect(screen, WHITE, (x*50, y*50, 50, 50))

    # Update the player sprite based on user keypresses
    player.update(pressed_keys, maze)

    # Fill the screen with black
    screen.fill(BLACK)
