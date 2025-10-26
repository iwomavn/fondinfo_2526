import g2d
from random import randrange

g2d.init_canvas((500, 500))
n = int(g2d.prompt("Numero quadrato da disegnare?"))

for i in range(n):
    x, y = randrange(401), randrange(401)  
    r, g, b = randrange(256), randrange(256), randrange(256)
    g2d.set_color((r, g, b))
    g2d.draw_rect((x, y), (100, 100))

g2d.main_loop()