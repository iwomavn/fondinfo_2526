import g2d
from random import randrange

g2d.init_canvas((500, 500))
n = int(g2d.prompt("Numero quadrati da disegnare?"))
i, x, y = 0, 0, 0  

while i < n:
    r, g, b = randrange(256), randrange(256), randrange(256)
    g2d.set_color((r, g, b))
    g2d.draw_rect((x, y), (50, 50))
    x += 50
    y += 50
    i += 1

g2d.main_loop()