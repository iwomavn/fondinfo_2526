import g2d
from random import randrange

g2d.init_canvas((500, 500))
n = int(g2d.prompt("Numero segmenti da disegnare?"))

for _ in range(n):
    x1, y1 = randrange(500), randrange(500)
    x2, y2 = randrange(500), randrange(500)
    g2d.set_color((0, 0, 0))
    g2d.draw_line((x1, y1), (x2, y2))
    
g2d.main_loop()
    