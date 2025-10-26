import g2d
from random import randrange

def main():
    g2d.init_canvas((400, 400))
    n = int(g2d.prompt("Inserisci numero punti da visualizzare"))
    
    x1 = int(g2d.prompt("Inserisci la coordinata x del primo punto"))
    y1 = int(g2d.prompt("Inserisci la coordinata y del primo punto"))
    
    x2 = int(g2d.prompt("Inserisci la coordinata x dell'ultimo punto"))
    y2 = int(g2d.prompt("Inserisci la coordinata y dell'ultimo punto"))
    
    r1 = int(g2d.prompt("Inserisci il valore di rosso (0-255) del primo cerchio"))
    g1 = int(g2d.prompt("Inserisci il valore di verde (0-255) del primo cerchio"))
    b1 = int(g2d.prompt("Inserisci il valore di blu (0-255) del primo cerchio"))
    
    r2 = int(g2d.prompt("Inserisci il valore di rosso (0-255) dell'ultimo cerchio"))
    g2 = int(g2d.prompt("Inserisci il valore di verde (0-255) dell'ultimo cerchio"))
    b2 = int(g2d.prompt("Inserisci il valore di blu (0-255) dell'ultimo cerchio"))
    
    m_x = (x2 - x1) / n - 1
    m_y = (y2 - y1) / n - 1
    
    for i in range(n):
        x = m_x * i + x1
        y = m_y * i + y1
        r = r1 + (r2 - r1) * i // (n - 1)
        g = g1 + (g2 - g1) * i // (n - 1)
        b = b1 + (b2 - b1) * i // (n - 1)
        g2d.set_color((r, g, b))
        g2d.draw_circle((x, y), 5)
    
    g2d.main_loop()
    
if __name__ == "__main__":
    main()