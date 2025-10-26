
import g2d
import math
import random

ARENA_W, ARENA_H = 400, 400
SPRITE_W, SPRITE_H = 20, 20

class OscillatingGhost:
    def __init__(self, x: int, y: int, dx: int):
        self._x = x
        self._y = y
        self._dx = dx
        self._visible = True
        self._base_y = y

    def move(self):
        self._x += self._dx
        self._y = self._base_y + 10 * math.sin((self._x * 2 * math.pi) / 80)

        if self._x > ARENA_W:
            self._x = -SPRITE_W
            self._y = self._base_y

        if self._x % 20 == 0:
            if random.randrange(3) == 0:
                self._visible = not self._visible

    def get_position(self) -> tuple[int, int]:
        return (int(self._x), int(self._y))

    def get_size(self) -> tuple[int, int]:
        return (SPRITE_W, SPRITE_H)

    def draw(self):
        if self._visible:
            g2d.draw_image("sprites.png", (20, 0, SPRITE_W, SPRITE_H), self.get_position())
        else:
            g2d.draw_image("sprites.png", (20, 20, SPRITE_W, SPRITE_H), self.get_position())

def tick():
    g2d.clear_canvas()
    ghost.move()
    ghost.draw()

def main():
    global ghost
    ghost = OscillatingGhost(100, 200, 2)
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
