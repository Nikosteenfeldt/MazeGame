# Import the pygame module
import pygame
import sys

# Import pygame.locals for easier access to key coordinates
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Constants
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize pygame
pygame.init()

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Game with Player")

# Define the maze (0 = wall, 1 = path)
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

# Define a player object by extending pygame.sprite.Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect()
        self.rect.topleft = (50, 50)


    # Move the sprite based on user keypresses, with collision detection
    def update(self, pressed_keys, maze):
        old_rect = self.rect.copy()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)

        # Check for collisions with walls
        if self.check_collision(maze):
            self.rect = old_rect

    # Check if player collides with any wall in the maze
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

# Instantiate player
player = Player()

# Variable to keep the main loop running
running = True

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # Get all the keys currently pressed
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys, maze)

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the maze
    draw_maze()

    # Draw the player on the screen
    screen.blit(player.surf, player.rect)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()