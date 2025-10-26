import g2d
from random import randrange

g2d.init_canvas((500, 500))
raggio = 50

n = int(g2d.prompt("Numero quadrato da disegnare?"))

for i in range(n):
    x, y = randrange(500), randrange(500)  
    r, g, b = randrange(256), randrange(256), randrange(256)
    g2d.set_color((r, g, b))
    g2d.draw_circle((x, y), (raggio))

g2d.main_loop()