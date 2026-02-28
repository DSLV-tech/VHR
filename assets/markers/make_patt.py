import sys
from PIL import Image

def generate_patt(img_path, out_path):
    img = Image.open(img_path).convert('L')
    # AR.js looks at the inner image for patterns, the black border is the 25% padding.
    # The image is already just the inner symbol (black U on white background) with some border.
    # Let's crop the thick black border off first to get just the pattern area.
    
    # We resize the inner pattern to 16x16
    img = img.resize((16, 16))
    pixels = img.load()
    
    matrix = [[pixels[x,y] for x in range(16)] for y in range(16)]
    
    def rot(m):
        return [list(elem) for elem in zip(*m[::-1])]
    
    blocks = []
    current = matrix
    for _ in range(4):
        lines = []
        for y in range(16):
            for x in range(16):
                val = current[y][x]
                lines.append(f"{val} {val} {val}")
        blocks.append("\n".join(lines) + "\n")
        current = rot(current)
        
    with open(out_path, "w") as f:
        f.write("\n".join(blocks))

if __name__ == '__main__':
    generate_patt(sys.argv[1], sys.argv[2])
