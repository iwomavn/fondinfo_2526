import g2d

def main ():
    L = 500
    n = int(g2d.prompt("Inserisci un numero n: "))
    
    g2d.init_canvas((L, L))
    red = 255 / n
    r_last = (L/n)/2
    r_first = L/2
    m = (r_first - r_last) / max(n - 1, 1)
    for i in reversed(range(n)):
        g2d.set_color((red * i, 0, 0))
        r = m * i + r_last
        g2d.draw_circle(((L / 2), (L / 2)), r)
        
    g2d.main_loop()
    
if __name__ == "__main__":
    main()