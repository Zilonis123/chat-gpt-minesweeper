import numpy as np

# Create a 8x8 matrix filled with zeros
matrix = np.zeros((8, 8))

# Place mines at random locations
for i in range(10):
    x, y = np.random.randint(0, 8), np.random.randint(0, 8)
    matrix[x][y] = -1 # -1 represents a bomb in the matrix

# Count the number of mines in the surrounding cells
for x in range(8):
    for y in range(8):
        if matrix[x][y] == -1:
            continue
        count = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                if x + dx < 0 or x + dx >= 8 or y + dy < 0 or y + dy >= 8:
                    continue
                if matrix[x + dx][y + dy] == -1:
                    count += 1
        matrix[x][y] = count

print(matrix)