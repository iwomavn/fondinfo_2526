import g2d

x1, y1, dx1, dy1 = 200, 200, 2, 0
ARENA_W, ARENA_H, BALL_W, BALL_H = 400, 400, 20, 20

def move_ball(x: int, y: int, dx: int, dy: int) -> tuple[int, int, int, int]:
    x += dx
    y += dy
    return (x, y, dx, dy)

def tick(): # chiamata 30 volte al secondo
    global x1, y1, dx1, dy1, countdown

    g2d.clear_canvas()
    g2d.draw_image("ball.png", (x1, y1))
    
    if x1 % 20 == 0 and y1 % 20 == 0:
        from random import choice
        dx1, dy1 = choice([(2,0),(-2,0),(0,2),(0,-2)])
    
    x1, y1, dx1, dy1 = move_ball(x1, y1, dx1, dy1)


def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()