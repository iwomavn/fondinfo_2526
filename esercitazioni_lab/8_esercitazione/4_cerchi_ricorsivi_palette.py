import g2d
import g2d

def rec_circles(p, r, depth, colori, skip_dir=None):
    x, y = p
    
    if depth == 0: # finisco ricorsione
        return

    g2d.set_color(colori[depth])
    g2d.draw_circle(p, r)

    new_radius = int(r * 0.42)
    directions = [(-1, -1), (+1, -1), (-1, +1), (+1, +1)] # dove disegno nuovi cerchi

    for dx, dy in directions:
        if skip_dir == (dx, dy): # se la direzione è quella da saltare, esce dal for
            continue 

        nx = x + (dx * r)
        ny = y + (dy * r)

        next_skip = (-dx, -dy) # direzione opposta è quella da skippare
        rec_circles((nx, ny), new_radius, depth-1, colori, next_skip)

def main():
    g2d.init_canvas((400, 400))
    
    colori = []
    with open("sequenza_colori.txt", "r") as file:
        for line in file:
            r, g, b = map(int, line.split(","))
            colori.append((r, g, b))
            
    rec_circles((200, 200), 110, 4, colori)
    g2d.main_loop()

if __name__ == "__main__":
    main()