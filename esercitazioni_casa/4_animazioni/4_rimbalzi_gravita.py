import g2d
x, y, dx, dy = 40, 80, 4, 4
ARENA_W, ARENA_H, BALL_W, BALL_H = 480, 360, 20, 20

# encapsulates behaviour, but exposes data
def move_ball(x: int, y: int, dx: int, dy: int) -> tuple[int, int, int, int]:
    dy += 0.5
    if not 0 <= x + dx <= ARENA_W - BALL_H:
        dx = -dx
    if not 0 <= y + dy<= ARENA_H - BALL_H:
        dy = -dy
    
    x += dx
    y += dy
    
    return (x, y, dx, dy)

def tick():
    global x, y, dx, dy
    g2d.clear_canvas()
    g2d.draw_image("ball.png", (x, y))
    x, y, dx, dy = move_ball(x, y, dx, dy)

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

main()
