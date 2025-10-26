import g2d

def main ():
    L = 500
    n = int(g2d.prompt("Inserisci un numero n: "))
    r = (L / n)/2

    g2d.init_canvas((L, L))
    x_first = 0 + r
    x_last = L - r
    y = L / 2
    m = (x_last - x_first) / max(n - 1, 1)
    blue = 255 // n
    
    for i in range(n):
        x = m * i + x_first
        g2d.set_color((0, 0, blue * i))
        g2d.draw_circle((x, y), r)
        
    g2d.main_loop()

if __name__ == "__main__":
    main()