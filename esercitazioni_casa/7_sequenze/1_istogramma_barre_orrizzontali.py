import g2d

def main():
    lista = []
    n = int(input("Inserisci un numero positivo (0 per terminare): "))
    while n != 0:
        lista.append(n)
        n = int(input("Inserisci un numero positivo (0 per terminare): "))
         
    g2d.init_canvas((600,400))    
    
    for i, n in enumerate(lista):
        h = 400 / len(lista)
        x, y = 0, 0 + i * h
        g2d.set_color((0, 0, 255))
        g2d.draw_rect((x,y),(n * h , h))
    
    g2d.main_loop()
    
main()