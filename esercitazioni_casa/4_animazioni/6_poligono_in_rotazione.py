import g2d
from math import cos, sin, radians 
n, param = 0, 0
ARENA_W, ARENA_H = 400, 400

def from_polar(plr):
    r, angle = plr
    return (r * cos(radians(angle)), r* sin(radians(angle)))

def move_around(start, lenght, angle):
    x0, y0= start
    dx, dy = from_polar((lenght, angle))
    return x0 + dx, y0 + dy

def tick():
    global n, param
    g2d.clear_canvas()
    param += 0.5
    vertices = []
    step = 360 / n
    for i in range(n):
        angle = i * step + param 
        x, y = move_around((200, 200), 150, angle)
        vertices.append((x, y))

    g2d.set_color((255, 182, 193))
    g2d.draw_polygon(vertices)

def main():
    global n
    g2d.init_canvas((ARENA_W, ARENA_H))
    n = int(g2d.prompt("Numero lati? "))
    g2d.main_loop(tick)

main()
