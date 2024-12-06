import sys
from collections import deque

def print_and_copy(value):
    print(value)
    try:
        import pyperclip
        pyperclip.copy(value)
    except ImportError:
        pass

infile = sys.argv[1] if len(sys.argv) >= 2 else '6.in'
grid = open('values.txt').read().strip().split('\n')
rows, cols = len(grid), len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '^':
            start_r, start_c = r, c
            break

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def simulate_guard(o_r, o_c): #this is actually stupid guard movement but fuck it
    r, c, d = start_r, start_c, 0
    seen = set() 
    visited_positions = set()
    
    while True:
        if (r, c, d) in seen:
            return True
        seen.add((r, c, d))
        visited_positions.add((r, c))


        dr, dc = directions[d]
        next_r, next_c = r + dr, c + dc

        if not (0 <= next_r < rows and 0 <= next_c < cols):
            break 
        if grid[next_r][next_c] == '#' or (next_r, next_c) == (o_r, o_c):
            d = (d + 1) % 4
        else:
            r, c = next_r, next_c

    return False

valid_positions = 0
for o_r in range(rows):
    for o_c in range(cols):
        if grid[o_r][o_c] == '.' and (o_r, o_c) != (start_r, start_c):
            if simulate_guard(o_r, o_c):
                valid_positions += 1
print_and_copy(valid_positions)
