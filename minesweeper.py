import numpy as np
import pygame

# Initialize pygame and create a window
pygame.init()
screen = pygame.display.set_mode((320, 320))
pygame.display.set_caption("Minesweeper")

# Define the colors
red = (255, 0, 0)
green = (0, 255, 0)

# Define the bomb symbol
BOMB = -1

# Create a 8x8 matrix filled with zeros
matrix = np.zeros((8, 8))

# Place mines at random locations
for i in range(10):
    x, y = np.random.randint(0, 8), np.random.randint(0, 8)
    if matrix[x][y] == BOMB:
        i -= 1 # Decrement i so that the loop doesn't skip an iteration
        continue
    matrix[x][y] = BOMB # Place a bomb in the matrix

# Count the number of mines in the surrounding cells
for x in range(8):
    for y in range(8):
        if matrix[x][y] == BOMB:
            continue # Skip cells that contain a bomb
        count = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                if x + dx < 0 or x + dx >= 8 or y + dy < 0 or y + dy >= 8:
                    continue
                if matrix[x + dx][y + dy] == BOMB:
                    count += 1
        matrix[x][y] = count

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Draw the matrix
    for x in range(8):
        for y in range(8):
            if matrix[x][y] == BOMB:
                pygame.draw.rect(screen, red, (40 * x, 40 * y, 40, 40))
            else:
                pygame.draw.rect(screen, green, (40 * x, 40 * y, 40, 40))
    pygame.display.update()

# Quit pygame
pygame.quit()