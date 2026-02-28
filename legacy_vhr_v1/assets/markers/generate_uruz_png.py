grid = [[255]*16 for _ in range(16)]

# Analyzing the user's PNG Uruz proportions (thick black design on white):
# It has a tall left leg, a shorter right leg, and a thick diagonal bridge.
# The overall bounding box of the Uruz will be roughly 8x12 pixels inside the 16x16 grid to allow space.

# Left Leg (starts at x=5, spans y=2 to y=13) - Thickness 2
for y in range(2, 14):
    grid[y][5] = 0
    grid[y][6] = 0

# Right Leg (starts at x=10, spans y=5 to y=11) - Thickness 2
for y in range(5, 12):
    grid[y][10] = 0
    grid[y][11] = 0

# Diagonal Roof (connects top of left leg to top of right leg)
# It descends from (7, 2) down to (9, 5)
grid[2][5] = 0; grid[2][6] = 0; grid[2][7] = 0 
grid[3][7] = 0; grid[3][8] = 0; grid[3][9] = 0
grid[4][8] = 0; grid[4][9] = 0; grid[4][10] = 0; grid[4][11] = 0

def rot(m):
    return [list(elem) for elem in zip(*m[::-1])]

blocks = []
current = grid
for _ in range(4):
    lines = []
    for y in range(16):
        for x in range(16):
            val = current[y][x]
            lines.append(f"{val} {val} {val}")
    blocks.append("\n".join(lines) + "\n")
    current = rot(current)

with open('assets/markers/uruz.patt', 'w') as f:
    f.write("\n".join(blocks))

print("uruz.patt regenerated based on user PNG")
