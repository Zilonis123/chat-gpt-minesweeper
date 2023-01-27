import pygame
import numpy as np
from minesweeper_logic import BOMB, generate_matrix, count_mines

# Initialize pygame and create a window
pygame.init()
screen = pygame.display.set_mode((320, 320))
pygame.display.set_caption("Minesweeper")

# Set the window icon
icon = pygame.image.load("Dalle-thumbnail.png")
pygame.display.set_icon(icon)

# Define the colors
red = (255, 0, 0)
green = (0, 255, 0)

# Generate matrix
matrix = generate_matrix()

# Count mines
matrix = count_mines(matrix)

def draw_matrix(matrix):
    """This function takes a matrix as input and draws it on the screen using Pygame.
    """
    for x in range(8):
        for y in range(8):
            rect = (40 * x, 40 * y, 40, 40)
            if matrix[x][y] == BOMB:
                pygame.draw.rect(screen, red, rect)
            else:
                pygame.draw.rect(screen, green, rect)
                
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the matrix
    draw_matrix(matrix)
    pygame.display.update()

# Quit pygame
pygame.quit()
