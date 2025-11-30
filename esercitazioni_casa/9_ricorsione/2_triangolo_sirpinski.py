import g2d

def draw_triangolo(x, y, w, h, max_depth, depth=0):
    g2d.set_color((0, 0, 0)) # caso base, rettangolo nero che prende tutta l'area
    g2d.draw_rect((x, y), (w, h))
    
    if depth == max_depth or w < 10: # se ho raggiunto massima ricorsione STOP
        return
    
    l = w // 2
    
    g2d.set_color((255, 255, 255))
    g2d.draw_rect((x, y), (l, l))
    
    draw_triangolo(x + l, y, l, l, max_depth, depth + 1)       
    draw_triangolo(x, y + l, l, l, max_depth, depth + 1)       
    draw_triangolo(x + l, y + l, l, l, max_depth, depth + 1)   

def main(): 
    width = height = 400
    g2d.init_canvas((width, height))
    
    n = int(g2d.prompt("Inserisci livello ricorsione: "))
    
    draw_triangolo(0, 0, width, height, n)
    
    g2d.main_loop()
    
if __name__ == "__main__":
    main()
