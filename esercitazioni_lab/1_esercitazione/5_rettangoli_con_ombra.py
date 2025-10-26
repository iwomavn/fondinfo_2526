import g2d
from random import randrange

g2d.init_canvas((500, 500))
numero = int(g2d.prompt("Numero rettangoli da disegnare?"))

for i in range(numero):
    x = randrange(0, 390) 
    y = randrange(0, 390)   
    larghezza = randrange(100, 199) 
    altezza = randrange(100, 199)
    r, g, b = randrange(256), randrange(256), randrange(256)
    
    g2d.set_color((80, 80, 80))
    g2d.draw_rect((x + 5, y + 5), (larghezza, altezza))
    
    g2d.set_color((r, g, b))
    g2d.draw_rect((x, y), (larghezza, altezza))

g2d.main_loop()