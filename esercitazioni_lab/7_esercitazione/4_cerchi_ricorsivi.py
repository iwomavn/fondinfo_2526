import g2d

def rec_circles(p, r):
    x, y = p
    if r <= 5:
        return
    
    g2d.set_color((0, 0, 0))
    g2d.draw_circle(p, r)
    new_radius = int(r * 0.42)
    
    rec_circles((x-r, y-r), new_radius)
    rec_circles((x+r, y-r), new_radius)
    rec_circles((x-r, y+r), new_radius)
    rec_circles((x+r, y+r), new_radius)
    
def main():
    g2d.init_canvas((400, 400))
    rec_circles((200, 200), 100)
    g2d.main_loop()

if __name__ == "__main__":
    main()
