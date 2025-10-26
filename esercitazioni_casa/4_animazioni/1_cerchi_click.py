import g2d
from random import randrange

ARENA_W, ARENA_H = 400, 400

x, y = 200, 200
dx, dy = 2, 0

def on_click ():
    global x, y
    curr_x, curr_y = g2d.mouse_pos()
    if abs(x-curr_x) <= 10 or abs(y-curr_y) <= 10:
        si = g2d.confirm("Chiudiamo il programma")
        if si:
            g2d.close_canvas()
    else:
        r, g, b = randrange(256), randrange(256), randrange(256)
        g2d.set_color((r, g, b))
        g2d.draw_circle((curr_x, curr_y), 20)
    
def tick():
    global x, y
    # g2d.clear_canvas()
    
    if (g2d.mouse_clicked()):
        on_click()

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()