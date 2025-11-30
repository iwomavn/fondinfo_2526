import g2d

def main():
    larghezza_canvas, altezza_canvas = 500, 500
    g2d.init_canvas((larghezza_canvas, altezza_canvas))
    
    valori = []
    while True:
        val = float(g2d.prompt("Inserisci un valore positivo (negativo per terminare):"))
        if val < 0:
            break
        valori.append(val)
    
    if not valori:
        print("Nessun valore inserito.")
        return


    max_val = max(valori)
    n = len(valori)
    altezza_barra = altezza_canvas / n  

    for i, v in enumerate(valori):
        lunghezza = (v / max_val) * larghezza_canvas   
        y = i * altezza_barra                        
        
        g2d.set_color((255, 192, 203))
        g2d.draw_rect((0, int(y)), (int(lunghezza), int(altezza_barra - 2))) 
    
    g2d.main_loop()

if __name__ == "__main__":
    main()
