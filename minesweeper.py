# visualization.py
from minesweeper_logic import generate_matrix, BOMB, count_mines
import pygame

# Define the screen
matrix_size = 8
cell_size = 40
screen_size = (matrix_size * cell_size, matrix_size * cell_size)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Minesweeper")
icon = pygame.image.load("Dalle-thumbnail.png")
pygame.display.set_icon(icon)

# Initialize pygame
pygame.init()

# Define the font
font = pygame.font.SysFont("comicsans", 20)

# Draw the matrix function
def draw_matrix(matrix):
    for x in range(matrix_size):
        for y in range(matrix_size):
            rect = (cell_size * x, cell_size * y, cell_size, cell_size)
            pygame.draw.rect(screen, (0, 255, 0), rect)
            if matrix[x][y] > 0:
                text = font.render(str(int(matrix[x][y])), True, (0, 0, 0))
                screen.blit(text, (cell_size * x + 15, cell_size * y + 10))


# main function
matrix = generate_matrix()
count_mines(matrix)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    draw_matrix(matrix)
    pygame.display.update()
