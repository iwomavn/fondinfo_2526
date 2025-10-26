import g2d
from random import randrange

def main():
    g2d.init_canvas((400, 400))
    n = int(g2d.prompt("Inserisci numero punti da visualizzare"))
    x1 = int(g2d.prompt("Inserisci la coordinata x del primo punto"))
    y1 = int(g2d.prompt("Inserisci la coordinata y del primo punto"))
    x2 = int(g2d.prompt("Inserisci la coordinata x dell'ultimo punto"))
    y2 = int(g2d.prompt("Inserisci la coordinata y dell'ultimo punto"))
    
    m_x = (x2 - x1) / n - 1
    m_y = (y2 - y1) / n - 1
    
    for i in range(n):
        x = m_x * i + x1
        y = m_y * i + y1
        r, g, b = randrange(256), randrange(256), randrange(256)
        g2d.set_color((r, g, b))
        g2d.draw_circle((x, y), 5)
    
    g2d.main_loop()
    
if __name__ == "__main__":
    main()