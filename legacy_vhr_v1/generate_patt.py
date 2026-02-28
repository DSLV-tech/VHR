# generate_patt.py
import math

# We will create a simple 16x16 matrix for the VHR logo.
# 0 = black (0,0,0), 255 = white (255,255,255)
# Actually, the background is white (255) and the text is black (0) for contrast inside the black border.

grid = [
    [255]*16 for _ in range(16)
]

# Draw 'V'
grid[4][2] = 0; grid[4][4] = 0
grid[5][2] = 0; grid[5][4] = 0
grid[6][2] = 0; grid[6][4] = 0
grid[7][3] = 0
grid[8][3] = 0

# Draw 'H'
grid[4][6] = 0; grid[4][8] = 0
grid[5][6] = 0; grid[5][8] = 0
grid[6][6] = 0; grid[6][7] = 0; grid[6][8] = 0
grid[7][6] = 0; grid[7][8] = 0
grid[8][6] = 0; grid[8][8] = 0

# Draw 'R'
grid[4][10] = 0; grid[4][11] = 0; grid[4][12] = 0
grid[5][10] = 0; grid[5][12] = 0
grid[6][10] = 0; grid[6][11] = 0
grid[7][10] = 0; grid[7][12] = 0
grid[8][10] = 0; grid[8][13] = 0

# We need to rotate a 16x16 square grid 90 degrees clockwise
def rotate_90(matrix):
    return [list(elem) for elem in zip(*matrix[::-1])]

def stringify_grid(matrix):
    lines = []
    for x in range(16):
        for y in range(16):
            val = matrix[x][y]
            # B G R
            lines.append(f"{val} {val} {val}")
    # AR.js training uses 256 lines per rotation block + a blank line
    return "\n".join(lines) + "\n"

blocks = []
current_grid = grid

for _ in range(4):
    blocks.append(stringify_grid(current_grid))
    current_grid = rotate_90(current_grid)

# Write to patt file
with open("/Users/cristiandisalvo/Desktop/VHR/assets/markers/vhr-logo.patt", "w") as f:
    f.write("\n".join(blocks))

print("Created vhr-logo.patt")
