grid = [[255]*16 for _ in range(16)]

# Left leg (tall)
for y in range(2, 14):
    grid[y][4] = 0
    grid[y][5] = 0

# Right leg (short)
for y in range(5, 12):
    grid[y][10] = 0
    grid[y][11] = 0

# Angled roof from top-left to mid-right
grid[2][4] = 0; grid[2][5] = 0; grid[2][6] = 0
grid[3][6] = 0; grid[3][7] = 0; grid[3][8] = 0
grid[4][8] = 0; grid[4][9] = 0; grid[4][10] = 0

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

print("uruz.patt created successfully")
