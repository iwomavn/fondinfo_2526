import g2d
from random import choice

ARENA_W, ARENA_H = 400, 400
BALL_W, BALL_H = 20, 20

class RandomWalker:
    def __init__(self, x0: int, y0: int):
        self._x = x0 // 2 * 2
        self._y = y0 // 2 * 2 # arrotondo
        self._dx = 2 
        self._dy = 0

    def move(self):
        if self._x % 20 == 0 and self._y % 20 == 0:
            self._choose_new_direction()

        new_x = self._x + self._dx
        new_y = self._y + self._dy

        if 0 <= new_x <= ARENA_W - BALL_W and 0 <= new_y <= ARENA_H - BALL_H:
            self._x = new_x
            self._y = new_y

    def _choose_new_direction(self):
        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        opposite = (-self._dx, -self._dy)
        directions.remove(opposite)
        self._dx, self._dy = choice(directions)

    def pos(self) -> tuple[int, int]:
        return self._x, self._y

def tick():
    g2d.clear_canvas()
    walker.move()
    g2d.draw_image("ball.png", walker.pos())

def main():
    global walker, g2d
    walker = RandomWalker(200, 200)
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.load_image("ball.png") 
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
