#!/usr/bin/env python3
import g2d

x, y, dx, dy = 200, 200, 4, 8
ARENA_W, ARENA_H, SIZE = 400, 400, 20

def move_ball(x: int, y: int, dx: int, dy: int) -> tuple[int, int, int, int]:
    if not 0 <= x + dx <= ARENA_W - SIZE:
        y += dy
        dx = -dx
    if not 0 <= y + dy <= ARENA_H - SIZE:
        dy = -dy
    x += dx
    return (x, y, dx, dy)

def on_click():
    global x, y, dx, dy
    dx = -dx
    x, y, dx, dy = move_ball(x, y, dx, dy)
    
def tick():
    global x, y, dx, dy
    g2d.clear_canvas()
    g2d.draw_image("sprites.png", (x, y), (20, 0), (SIZE, SIZE))
    x, y, dx, dy = move_ball(x, y, dx, dy)
    
    if (g2d.mouse_clicked()):
        on_click()

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

main()