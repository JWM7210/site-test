import ti_graphics as gfx
import random
import time

# Grid setup
WIDTH, HEIGHT = 10, 20
CELL = 10
screen = gfx.Screen()

# Define shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 1], [1, 1]],  # O
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]]   # J
]

def new_piece():
    shape = random.choice(SHAPES)
    return {"x": WIDTH // 2 - len(shape[0]) // 2, "y": 0, "shape": shape}

def collide(grid, piece):
    shape = piece["shape"]
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                gx, gy = piece["x"] + x, piece["y"] + y
                if gx < 0 or gx >= WIDTH or gy >= HEIGHT:
                    return True
                if gy >= 0 and grid[gy][gx]:
                    return True
    return False

def merge(grid, piece):
    for y, row in enumerate(piece["shape"]):
        for x, cell in enumerate(row):
            if cell and piece["y"] + y >= 0:
                grid[piece["y"] + y][piece["x"] + x] = 1

def clear_lines(grid):
    new = [r for r in grid if any(c == 0 for c in r)]
    while len(new) < HEIGHT:
        new.insert(0, [0] * WIDTH)
    return new

def rotate(piece):
    s = piece["shape"]
    piece["shape"] = [list(row) for row in zip(*s[::-1])]

grid = [[0]*WIDTH for _ in range(HEIGHT)]
piece = new_piece()
tick = 0.3
running = True

while running:
    # Input
    key = gfx.get_key()
    if key == "esc":
        running = False
    elif key == "left":
        piece["x"] -= 1
        if collide(grid, piece): piece["x"] += 1
    elif key == "right":
        piece["x"] += 1
        if collide(grid, piece): piece["x"] -= 1
    elif key == "down":
        piece["y"] += 1
    elif key == "up":
        rotate(piece)
        if collide(grid, piece):
            for _ in range(3): rotate(piece)  # undo

    # Gravity
    time.sleep(tick)
    piece["y"] += 1
    if collide(grid, piece):
        piece["y"] -= 1
        merge(grid, piece)
        grid = clear_lines(grid)
        piece = new_piece()
        if collide(grid, piece):
            running = False

    # Draw
    screen.clear()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if grid[y][x]:
                screen.fill_rect(x*CELL, y*CELL, CELL-1, CELL-1)
    for y, row in enumerate(piece["shape"]):
        for x, cell in enumerate(row):
            if cell:
                screen.fill_rect((piece["x"]+x)*CELL, (piece["y"]+y)*CELL, CELL-1, CELL-1)
    screen.update()
