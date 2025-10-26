import g2d
from random import randrange
def main():
    L = 500
    g2d.init_canvas((L, L))
    n = int(g2d.prompt("Inserisci un numero n: "))
    l = L / n * 2
    
    pos_1 = 0
    pos_last = L - (l/2)
    m = (pos_last - pos_1) / max(n - 1, 1)
    
    for i in range(n):
        g2d.set_color((randrange(256), randrange(256), randrange(256)))
        pos = m * i + pos_1
        g2d.draw_rect((pos - l/2, pos - l/2), (l, l))
    
    g2d.main_loop()
if __name__ == "__main__":
    main()