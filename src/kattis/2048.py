# Problem: 2048 Game Simulation
# URL: https://open.kattis.com/problems/2048
#
# Simulate one move in the 2048 game. Tiles slide in the chosen direction
# and merge if they have the same value. Merged tiles can't merge again
# in the same move.

def merge_line(line):
    # remove zeros
    nums = [x for x in line if x != 0]
    
    # merge adjacent equal numbers
    result = []
    i = 0
    while i < len(nums):
        if i + 1 < len(nums) and nums[i] == nums[i + 1]:
            result.append(nums[i] * 2)
            i += 2
        else:
            result.append(nums[i])
            i += 1
    
    # pad with zeros
    while len(result) < 4:
        result.append(0)
    
    return result

def move_left(grid):
    new_grid = []
    for row in grid:
        new_grid.append(merge_line(row))
    return new_grid

def move_right(grid):
    new_grid = []
    for row in grid:
        reversed_row = row[::-1]
        merged = merge_line(reversed_row)
        new_grid.append(merged[::-1])
    return new_grid

def move_up(grid):
    new_grid = [[] for _ in range(4)]
    for col in range(4):
        column = [grid[row][col] for row in range(4)]
        merged = merge_line(column)
        for row in range(4):
            new_grid[row].append(merged[row])
    return new_grid

def move_down(grid):
    new_grid = [[] for _ in range(4)]
    for col in range(4):
        column = [grid[row][col] for row in range(4)]
        column = column[::-1]
        merged = merge_line(column)
        merged = merged[::-1]
        for row in range(4):
            new_grid[row].append(merged[row])
    return new_grid

grid = []
for _ in range(4):
    row = list(map(int, input().split()))
    grid.append(row)

direction = int(input())

if direction == 0:
    grid = move_left(grid)
elif direction == 1:
    grid = move_up(grid)
elif direction == 2:
    grid = move_right(grid)
else:
    grid = move_down(grid)

for row in grid:
    print(' '.join(map(str, row)))