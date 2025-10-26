from random import choice, randrange
from actor import Actor, Arena, Point

ARENA_W, ARENA_H = 800, 600
VIEW_W, VIEW_H = 480, 360
SCROLL_SPEED = 8

view_x, view_y = 0, 0

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
    def __init__(self, pos):
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._visible = True

    def move(self, arena: Arena):
        aw, ah = arena.size()
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


def update_view(center_actor):
    global view_x, view_y

    ax, ay = center_actor.pos()
    aw, ah = center_actor.size()

    view_x = ax + aw//2 - VIEW_W//2
    view_y = ay + ah//2 - VIEW_H//2

    view_x = max(0, min(view_x, ARENA_W - VIEW_W))
    view_y = max(0, min(view_y, ARENA_H - VIEW_H))


def tick():
    global view_x, view_y
    g2d.clear_canvas()
    keys = g2d.current_keys()

    if "ArrowLeft" in keys:
        view_x = max(view_x - SCROLL_SPEED, 0)
    if "ArrowRight" in keys:
        view_x = min(view_x + SCROLL_SPEED, ARENA_W - VIEW_W)
    if "ArrowUp" in keys:
        view_y = max(view_y - SCROLL_SPEED, 0)
    if "ArrowDown" in keys:
        view_y = min(view_y + SCROLL_SPEED, ARENA_H - VIEW_H)

    actors = arena.actors()
    if actors:
        update_view(actors[0])

    for a in actors:
        if a.sprite() is not None:
            ax, ay = a.pos()
            aw, ah = a.size()
            draw_pos = (ax - view_x, ay - view_y)
            if -aw < draw_pos[0] < VIEW_W and -ah < draw_pos[1] < VIEW_H:
                g2d.draw_image("sprites.png", draw_pos, a.sprite(), a.size())

    arena.tick(keys)

def main():
    global g2d, arena
    import g2d

    arena = Arena((ARENA_W, ARENA_H))
    arena.spawn(Ball((40, 80)))
    arena.spawn(Ball((80, 40)))
    arena.spawn(Ghost((120, 80)))
    arena.spawn(Turtle((230, 170)))

    g2d.init_canvas((VIEW_W, VIEW_H))
    g2d.main_loop(tick)


if __name__ == "__main__":
    main()