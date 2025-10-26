ARENA_W, ARENA_H, BALL_W, BALL_H = 480, 360, 20, 20

class Alien:
    def __init__(self, x0: int, y0: int):
        self._x = x0
        self._y = y0
        self._dx, self._dy = 4, 8

    def move(self):
        if not 0 <= self._x + self._dx <= ARENA_W - BALL_W:
            self._y += self._dy
            self._dx = -self._dx
        if not 0 <= self._y + self._dy <= ARENA_H - BALL_H:
            self._dy = -self._dy
        self._x += self._dx
        
    def change_direction(self):
        self._dx = -self._dx
        
    def pos(self):
        return self._x, self._y


def tick():
    g2d.clear_canvas()  # BG
    g2d.draw_rect(b1.pos(), (BALL_W, BALL_H))  # FG
    g2d.draw_rect(b2.pos(), (BALL_W, BALL_H))  # FG
    b1.move()
    b2.move()

def main():
    global b1, b2, g2d
    import g2d  # Ball does not depend on g2d
    b1 = Alien(140, 180)
    b2 = Alien(180, 140)
    b2.change_direction()

    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
