import g2d
x, y, dx, dy = 40, 80, 4, 4
ARENA_W, ARENA_H, BALL_W, BALL_H = 480, 360, 20, 20
frames = 0  # numero di frame ancora da muovere


# encapsulates behaviour, but exposes data
def move_ball(x: int, y: int, dx: int, dy: int) -> tuple[int, int, int, int]:
    dy += 0.5
    if not 0 <= x + dx <= ARENA_W - BALL_H:
        dx = -dx
    if not 0 <= y + dy<= ARENA_H - BALL_H:
        dy = -dy
    y += dy
    
    return (x, y, dx, dy)

def on_click():
    global x, y, dx, dy, frames
    frames = 5   # la palla si muove per 5 tick
    dy = -dy             # inverti direzione (facoltativo, se vuoi un rimbalzo)

def tick():
    global x, y, dx, dy, frames
    g2d.clear_canvas()
    g2d.draw_image("ball.png", (x, y))
    if (g2d.mouse_clicked()):
        on_click()
        
    if frames > 0:
        x, y, dx, dy = move_ball(x, y, dx, dy)
        frames -= 1

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

main()
