from math import cos, sin, radians 
import g2d

def from_polar(plr):
    r, angle = plr
    return (r * cos(radians(angle)), r* sin(radians(angle)))

def move_around(start, lenght, angle):
    x0, y0= start
    dx, dy = from_polar((lenght, angle))
    return x0 + dx, y0 + dy

def draw_polygon(n, center, radius):
    vertices = []
    step = 360 / n 
    for i in range(n):
        angle = i*step
        (x, y) = move_around(center, radius, angle)
        vertices.append((x, y))
    
    g2d.set_color((255, 182, 193))
    g2d.draw_polygon(vertices)

def main():
    g2d.init_canvas((400, 400))
    n = int(g2d.prompt("Numero lati? "))
    draw_polygon(n, (200, 200), 150)
    g2d.main_loop()
    
if __name__ == "__main__":
    main()
    