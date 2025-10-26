import g2d

def draw_figure(center: g2d.Point, radius: int, n: int):
    for i in range(n):
        r = radius * (1 - i / n)
        black = int(255 * i / max((n - 1), 1))
        color = g2d.Color((black, black, black))
        g2d.set_color(color)
        g2d.draw_circle(center, r)

def main():
    g2d.init_canvas((500, 500))
    n = int(g2d.prompt("Inserisci il numero di figure da disegnare: "))
    
    radius = (500 / n)/2
    
    for i in range(n):
        x = radius + i * 2 * radius
        center = g2d.Point((x, 250))
        draw_figure(center, radius, n)

    g2d.main_loop()

if __name__ == "__main__":
    main()
