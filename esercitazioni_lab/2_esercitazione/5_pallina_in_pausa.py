import g2d

x1, y1, dx1, dy1, countdown = 200, 200, 2, 0, 0  
ARENA_W, ARENA_H, BALL_W, BALL_H = 400, 400, 20, 20

def move_ball(x: int, y: int, dx: int, dy: int) -> tuple[int, int, int, int]:
    global countdown
    if countdown > 0: # in pausa
        return (x, y, 0, 0)
    x += dx
    y += dy
    return (x, y, dx, dy)

def tick(): # chiamata 30 volte al secondo
    global x1, y1, dx1, dy1, countdown
    
    if g2d.mouse_clicked() and countdown == 0:
        countdown = 30
    
    g2d.clear_canvas()
    g2d.draw_image("ball.png", (x1, y1))
    
    x1, y1, dx1, dy1 = move_ball(x1, y1, dx1, dy1)
   
    if countdown > 0:
        countdown -= 1
        if countdown == 0:
            dx1 = 2

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()