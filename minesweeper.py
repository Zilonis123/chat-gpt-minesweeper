import pygame
from minesweeper_logic import generate_matrix, count_mines

# Initialize pygame
pygame.init()

# Define the screen size
screen_size = (320, 320)

# Create the screen with defined size and set caption and icon
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Minesweeper")
icon = pygame.image.load("Dalle-thumbnail.png")
pygame.display.set_icon(icon)

def draw_matrix(matrix, matrix_size):
    """
    Draws the matrix on the screen using pygame.
    Uses different background colors for different numbers.
    """
    # Define color dictionary for numbers
    color_dict = {1: (0, 255, 0), 2: (0, 0, 255), 3: (255, 0, 0), 
                  4: (0, 255, 255), 5: (255, 0, 255), 6: (255, 255, 0),
                  7: (128, 0, 128), 8: (128, 128, 0)}
    
    # Initialize font
    font = pygame.font.SysFont("comicsans", 20)

    for x in range(matrix_size):
        for y in range(matrix_size):
            # Look up color for current cell
            number = matrix[x][y]
            color = color_dict.get(number, (255, 255, 255))
            
            # Draw rectangle with background color
            rect = (40 * x, 40 * y, 40, 40)
            pygame.draw.rect(screen, color, rect)
            
            # Draw number if cell is not empty
            if number > 0:
                text = font.render(str(int(matrix[x][y])), True, (0, 0, 0))
                screen.blit(text, (40 * x + 15, 40 * y + 10))


# main function
matrix = generate_matrix()
count_mines(matrix)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    draw_matrix(matrix, 8)
    pygame.display.update()
