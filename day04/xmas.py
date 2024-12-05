import numpy as np

def count_xmas_in_motherfucka(file_path):
    word = "XMAS"
    count = 0

    with open(file_path, 'r') as f:
        grid = [line.strip() for line in f.readlines()]

    rows = len(grid)
    cols = len(grid[0])

    grid = np.array([list(row) for row in grid])
    directions = [(dr, dc) for dr in range(-1, 2) for dc in range(-1, 2) if not (dr == 0 and dc == 0)]

    def check_word(r, c, dr, dc):
        for i in range(4):
            nr, nc = r + dr * i, c + dc * i
            if not (0 <= nr < rows and 0 <= nc < cols):
                return False
            if grid[nr, nc] != word[i]:
                return False
        return True

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == word[0]:
                for dr, dc in directions:
                    if check_word(r, c, dr, dc):
                        count += 1
    
    return count

def count_xmas_in_x_shape(file_path):
    word = "MAS"
    count = 0

    with open(file_path, 'r') as f:
        grid = [line.strip() for line in f.readlines()]

    rows = len(grid)
    cols = len(grid[0])

    grid = np.array([list(row) for row in grid])

    directions = [
        (1, 1),
        (-1, 1)
    ]
    
    def check_word(r, c, dr, dc):
        for i in range(3):
            nr, nc = r + dr * i, c + dc * i
            if not (0 <= nr < rows and 0 <= nc < cols):
                return False
            if grid[nr, nc] != word[i]:
                return False
        return True

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == "M":
                for dr1, dc1 in directions:
                    for dr2, dc2 in directions:
                        if check_word(r, c, dr1, dc1) and check_word(r, c, dr2, dc2):
                            count += 1

    return count

file_path = 'values.txt'
result  = count_xmas_in_motherfucka(file_path)
result2 = count_xmas_in_x_shape(file_path)
print(f"XMAS appears {result} times.")
print(f"X-MAS appears {result2} times.")
