#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""
from random import randint

ARENA_W, ARENA_H, BALL_W, BALL_H = 480, 360, 20, 20

class Ball:
    def __init__(self, x0: int, y0: int):
        self._x = x0
        self._y = y0
        self._dx, self._dy = 4, 4
        self._color = (r, g, b) = (randint(0, 255), randint(0, 255), randint(0, 255))

    def move(self):
        if not 0 <= self._x + self._dx <= ARENA_W - BALL_W:
            self._dx = -self._dx
            self._color = (r, g, b) = (randint(0, 255), randint(0, 255), randint(0, 255))
        if not 0 <= self._y + self._dy <= ARENA_H - BALL_H:
            self._dy = -self._dy
            self._color = (r, g, b) = (randint(0, 255), randint(0, 255), randint(0, 255))
        self._x += self._dx
        self._y += self._dy

    def pos(self) -> tuple[int, int]:
        return self._x, self._y
    
    def color(self) -> tuple[int, int, int]:
        return self._color

def console_run():
    b1 = Ball(140, 180)
    b2 = Ball(180, 140)
    b3 = Ball(200, 100)

    b1.move()
    b2.move()
    b3.move()

    print("b1 @", b1.pos())
    print("b2 @", b2.pos())
    print("b3 @", b3.pos())

def tick():
    g2d.clear_canvas()  # BG
    g2d.set_color(b1.color())
    g2d.draw_rect(b1.pos(), (BALL_W, BALL_H))# FG
    g2d.set_color(b2.color())
    g2d.draw_rect(b2.pos(), (BALL_W, BALL_H))
    g2d.set_color(b3.color())
    g2d.draw_rect(b3.pos(), (BALL_W, BALL_H))
    b1.move()
    b2.move()
    b3.move()

def main():
    global b1, b2, b3, g2d
    import g2d  # Ball does not depend on g2d
    b1 = Ball(140, 180)
    b2 = Ball(180, 140)
    b3 = Ball(200, 100)

    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()