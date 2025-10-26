from random import choice, randrange, randint, uniform
from math import cos, sin, pi, radians
from actor import Actor, Arena, Point

class Ball(Actor):
    def __init__(self, pos):
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._dx, self._dy = 4, 4

    def move(self, arena: Arena):
        for other in arena.collisions():
            if not isinstance(other, Ghost):
                x, y = other.pos()
                if x < self._x:
                    self._dx = abs(self._dx)
                else:
                    self._dx = -abs(self._dx)
                if y < self._y:
                    self._dy = abs(self._dy)
                else:
                    self._dy = -abs(self._dy)

        arena_w, arena_h = arena.size()
        if self._x + self._dx < 0:
            self._dx = abs(self._dx)
        elif self._x + self._dx > arena_w - self._w:
            self._dx = -abs(self._dx)
        if self._y + self._dy < 0:
            self._dy = abs(self._dy)
        elif self._y + self._dy > arena_h - self._h:
            self._dy = -abs(self._dy)

        self._x += self._dx
        self._y += self._dy

    def pos(self) -> Point:
        return self._x, self._y

    def size(self) -> Point:
        return self._w, self._h

    def sprite(self) -> Point:
        return 0, 0

class Ghost(Actor):
    def __init__(self, arena_size: Point):
        aw, ah = arena_size
        cx, cy = aw / 2, ah / 2

        angle = radians(randint(0, 361))
        r = 100  

        # Posizione iniziale attorno al centro
        self._x = cx + r * cos(angle)
        self._y = cy + r * sin(angle)
        self._w, self._h = 20, 20
        self._visible = True

        self._init_x, self._init_y = self._x, self._y

    def move(self, arena: Arena):
        aw, ah = arena.size()
        keys = arena.current_keys()

        if "h" in keys:
            self._x, self._y = self._init_x, self._init_y
            return

        dx = choice([-4, 0, 4])
        dy = choice([-4, 0, 4])
        self._x = (self._x + dx) % aw
        self._y = (self._y + dy) % ah

        if randrange(100) == 0:
            self._visible = not self._visible
        if randrange(1000) == 0:
            arena.spawn(Ball(self.pos()))

    def pos(self) -> Point:
        return self._x, self._y

    def size(self) -> Point:
        return self._w, self._h

    def sprite(self) -> Point:
        if self._visible:
            return 20, 0
        return 20, 20

class Turtle(Actor):
    def __init__(self, pos):
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._speed = 2

    def move(self, arena: Arena):
        for other in arena.collisions():
            if isinstance(other, Ball):
                self.hit(arena)

        keys = arena.current_keys()
        if "ArrowUp" in keys:
            self._y -= self._speed
        elif "ArrowDown" in keys:
            self._y += self._speed
        if "ArrowLeft" in keys:
            self._x -= self._speed
        elif "ArrowRight" in keys:
            self._x += self._speed

        aw, ah = arena.size()
        self._x = min(max(self._x, 0), aw - self._w)
        self._y = min(max(self._y, 0), ah - self._h)

    def hit(self, arena: Arena):
        arena.kill(self)

    def pos(self) -> Point:
        return self._x, self._y

    def size(self) -> Point:
        return self._w, self._h

    def sprite(self) -> Point:
        return 0, 20

def tick():
    g2d.clear_canvas()
    for a in arena.actors():
        if a.sprite() is not None:
            g2d.draw_image("sprites.png", a.pos(), a.sprite(), a.size())
    arena.tick(g2d.current_keys())


def main():
    global g2d, arena
    import g2d

    arena = Arena((480, 360))
    arena.spawn(Ball((40, 80)))
    arena.spawn(Ball((80, 40)))
    arena.spawn(Ghost(arena.size())) 
    arena.spawn(Turtle((230, 170)))

    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)


if __name__ == "__main__":
    main()
