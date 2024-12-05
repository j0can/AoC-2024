import re

# Your input (use your actual input string here)
with open('values.txt', 'r') as file:
    puzzle_input = file.read

# Regular expression to find valid `mul(X,Y)` patterns
pattern = r"mul\((\d+),(\d+)\)"

# Find all matches
matches = re.findall(pattern, puzzle_input)

# Compute the sum of the multiplications
result = sum(int(x) * int(y) for x, y in matches)

print(f"The sum of all valid mul(X,Y) results is: {result}")
