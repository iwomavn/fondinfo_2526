import g2d

def draw_circle(radius, n, colori, depht=0):
    radius_min = 200 / n
    max_depht = len(colori)

    if radius < radius_min:
        return

    if depht == max_depht:
        depht = 0
    color = colori[depht]
    g2d.set_color(color)

    g2d.draw_circle((200, 200), radius)

    m = (200 - radius_min) / n
    draw_circle(radius - m, n, colori, depht + 1)  
    
def main():
    colori = []
    with open("sequenza_colori.txt", "r") as file:
        for line in file:
            r, g, b = map(int, line.split(","))
            colori.append((r, g, b))
    
    g2d.init_canvas((400, 400))
    n = int(g2d.prompt("Inserisci n: "))
    draw_circle(200, n, colori)
    
    g2d.main_loop()
    

if __name__ == "__main__":
    main()
