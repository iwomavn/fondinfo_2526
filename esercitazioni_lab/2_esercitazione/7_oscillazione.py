import g2d
import math

x1, y1, dx1, dy1= 200, 200, 2, 0 
ARENA_W, ARENA_H, BALL_W, BALL_H = 400, 400, 20, 20

def move_ball(x: int, y: int, dx: int, dy: int) -> tuple[int, int, int, int]:
    x += dx
    y = y + 10 * math.sin((x * 2 * 3.14)/ 80)
    if x > ARENA_W:
        x = -BALL_W
        y = 200
    return (x, y, dx, dy)

def tick(): # chiamata 30 volte al secondo
    global x1, y1, dx1, dy1
    g2d.clear_canvas()
    g2d.draw_image("ball.png", (x1, y1))
    x1, y1, dx1, dy1 = move_ball(x1, y1, dx1, dy1)

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()