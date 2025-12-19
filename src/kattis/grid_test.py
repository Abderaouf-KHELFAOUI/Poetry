from src.kattis.2048 import move_left, move_right, move_up, move_down

grid = [
    [2,0,2,2],
    [4,4,4,4],
    [0,2,0,2],
    [2,2,2,2]
]

print("left:")
for r in move_left(grid):
    print(r)

print("\nright:")
for r in move_right(grid):
    print(r)

print("\nup:")
for r in move_up(grid):
    print(r)

print("\ndown:")
for r in move_down(grid):
    print(r)
