import math, random, g2d

def randline(p1: g2d.Point) -> g2d.Point:
    x1, y1 = p1
    angle = math.radians(random.randint(0, 361)) 
    
    x2 = x1 + 100 * math.cos(angle)
    y2 = y1 + 100 * math.sin(angle)
    p2 = g2d.Point((x2, y2))
    
    g2d.draw_line(p1, p2)
    return p2

def main():
    g2d.init_canvas((400, 400))
    n = int(g2d.prompt("Numero di segmenti della spezzata:"))

    current = (200, 200)

    for _ in range(n):
        current = randline(current)

    g2d.main_loop()

if __name__ == "__main__":
    main()
