import random

# Create a 3x3 grid initialized with zeros
grid = [[0 for _ in range(3)] for _ in range(3)]

# Fill the grid with valid numbers
for row in range(3):
    for col in range(3):
        valid = False
        while not valid:
            num = random.randint(1, 3)
            valid = True
            
            # Check if the number is not in the current row
            for x in range(3):
                if grid[row][x] == num:
                    valid = False
                    break
            
            # Check if the number is not in the current column
            if valid:
                for x in range(3):
                    if grid[x][col] == num:
                        valid = False
                        break
            
            # If valid, place the number
            if valid:
                grid[row][col] = num

# Print the Sudoku grid
print("Sudoku Grid:")
for row in grid:
    print(" ".join(str(num) for num in row))
