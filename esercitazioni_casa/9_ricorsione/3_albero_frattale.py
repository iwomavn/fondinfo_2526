import g2d
from math import radians, cos, sin 

def from_polar(plr):
    r, angle = plr
    a = radians(angle)
    return (r*cos(a), r*sin(a))

def move_around(start, lenght, angle):
    x0, y0 = start
    dx, dy = from_polar((lenght, angle))
    return(x0 + dx, y0 + dy)
    
def draw_tree(pos, lenght, angle):
    arrivo = move_around(pos, lenght, angle) # calcolo arrivo primo tronco
    
    if lenght < 5: # disegno foglia se lunghezza minore di 5
        g2d.set_color((0, 255, 0))
        g2d.draw_line(pos, (arrivo))
    else:
        g2d.set_color((150, 150, 50)) # tronco iniziale
        g2d.draw_line((pos), arrivo)

        draw_tree(arrivo, lenght * 4/5, angle - 30)
        draw_tree(arrivo, lenght * 4/5, angle + 30)
    
    
def main():
    g2d.init_canvas((400, 400))
    draw_tree((200, 350), 80, -90) # -90 perché si inizia dall'angolo superiore
    g2d.main_loop()
    
if __name__ == "__main__":
    main()