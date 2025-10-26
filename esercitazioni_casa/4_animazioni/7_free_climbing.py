import g2d
from random import randint

ARENA_W, ARENA_H, SIZE = 200, 200, 20
x1, y1, dx1, dy1 = 50, ARENA_H - SIZE, 0, 0
x2, y2, dx2, dy2 = 150, ARENA_H - SIZE, 0, 0

def move_ball(x: int, y: int, dx: int, dy: int) -> tuple[int, int, int, int]:
    if not 0 <= x + dx <= ARENA_W - SIZE:
        dx = -dx
    if not 0 <= y + dy <= ARENA_H - SIZE:
        dy = -dy
    y += dy
    return (x, y, dx, dy)

def tick():
    global x1, y1, dx1, dy1
    global x2, y2, dx2, dy2

    g2d.clear_canvas()

    dy1 += randint(-1, 3)
    dy2 += randint(-1, 3)

    # muovi le due palle
    x1, y1, dx1, dy1 = move_ball(x1, y1, dx1, dy1)
    x2, y2, dx2, dy2 = move_ball(x2, y2, dx2, dy2)

    # disegna i due giocatori
    g2d.draw_image("sprites.png", (x1, y1), (SIZE, 0), (SIZE, SIZE))
    g2d.draw_image("sprites.png", (x2, y2), (0, SIZE), (SIZE, SIZE))

    # verifica chi arriva in alto (y <= 0)
    if y1 <= 0:
        g2d.alert("Ha vinto giocatore 1!")
        g2d.close_canvas()
    elif y2 <= 0:
        g2d.alert("Ha vinto giocatore 2!")
        g2d.close_canvas()

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

main()
