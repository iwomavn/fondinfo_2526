from math import cos, sin, radians 
import g2d

def from_polar(plr):
    r, angle = plr
    return (r * cos(radians(angle)), r* sin(radians(angle)))

def move_around(start, lenght, angle):
    x0, y0= start
    dx, dy = from_polar((lenght, angle))
    return x0 + dx, y0 + dy

def draw_clock(center, radius):
    hours, minutes = 12, 60
    vertices_h, vertices_m = [], []
    step_h = 360 / hours
    step_m = 360 / minutes
    for i in range(hours):
        angle = i * step_h
        (x, y) = move_around(center, radius, angle)
        vertices_h.append((x, y))
    
    for i in range(minutes):
        angle = i * step_m
        (x, y) = move_around(center, radius, angle)
        vertices_m.append((x, y))
    
    g2d.set_color((255, 182, 193))
    g2d.draw_circle(center, radius + 10)
    for v in vertices_h:
        g2d.set_color((255, 255, 255))
        g2d.draw_circle(v, 5)

    for v in vertices_m:
        g2d.set_color((255, 255, 255))
        g2d.draw_circle(v, 2)

def main():
    g2d.init_canvas((400, 400))
    draw_clock((200, 200), 150)
    g2d.main_loop()
    
if __name__ == "__main__":
    main()
    