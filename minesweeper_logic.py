import numpy as np

# Define the bomb symbol
BOMB = -1

def generate_matrix():
    """This function generates an 8x8 matrix filled with zeros and
    places mines at random locations.
    """
    # Create a 8x8 matrix filled with zeros
    matrix = np.zeros((8, 8))

    # Place mines at random locations
    for i in range(10):
        x, y = np.random.randint(0, 8), np.random.randint(0, 8)
        if matrix[x][y] == BOMB:
            i -= 1 # Decrement i so that the loop doesn't skip an iteration
            continue
        matrix[x][y] = BOMB # Place a bomb in the matrix
    return matrix

def count_mines(matrix):
    """This function counts the number of mines in the surrounding cells
    of the matrix.
    """
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
    return matrix