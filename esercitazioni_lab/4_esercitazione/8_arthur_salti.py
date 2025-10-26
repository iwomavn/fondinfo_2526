from actor import Actor, Arena, Point

# ( (sprite_coord), (sprite_size) )
DEFAULT = ((6, 43), (20, 31))
LEFT_DEFAULT = ((486, 43), (20, 31))
JUMP_RIGHT = ((144, 29), (32, 27))
JUMP_LEFT = ((336, 29), (32, 27))

class Arthur(Actor):
    def __init__(self, pos):
        self._x, self._y = pos
        self._dx, self._dy = 5, 15

        # Settings
        self._sprite, self._size = DEFAULT

        # Animation
        self._animation = False
        self._animation_tick = 0
        self._animation_cooldown = 0

    def move(self, arena: Arena):
        aw, _ = arena.size()

        if self._animation_tick > 0:
            self._animation_tick -= 1
            if self._animation_tick == 0:
                self._animation = False
                self._sprite, self._size = DEFAULT
                self._y += self._dy
                self._animation_cooldown = 30

        if self._animation_cooldown > 0:
            self._animation_cooldown -= 1

        keys = arena.current_keys()
        if "d" in keys:
            self._x = min((self._x + self._dx), aw)
            if not self._animation:
                self._sprite, self._size = DEFAULT
            else:
                self._sprite, self._size = JUMP_RIGHT
        elif "a" in keys:
            self._x = max(0, (self._x - self._dx))
            if not self._animation:
                self._sprite, self._size = LEFT_DEFAULT
            else:
                self._sprite, self._size = JUMP_LEFT


        if "w" in keys:
            if not self._animation and not self._animation_cooldown > 0:
                self._y -= self._dy
                self._animation = True
                self._animation_tick = 10
                self._sprite, self._size = JUMP_RIGHT


    def pos(self) -> Point:
        return (self._x, self._y)

    def size(self) -> Point:
        return self._size

    def sprite(self) -> Point | None:
        return self._sprite