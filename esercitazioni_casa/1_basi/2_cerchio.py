import g2d
import math

g2d.init_canvas((500, 500))
center = (250, 250)

r = int(g2d.prompt("Inserisci il valore del raggio (tra 0 e 200): "))
if (r < 0 or r > 200):
    r = int(input("Raggio non valido. Inserisci il valore del raggio (tra 0 e 200):"))
else:
    area = r * r * math.pi
    circonferenza = 2 * r * math.pi
    g2d.set_color((255, 192, 203))
    g2d.draw_circle(center, r)
    g2d.draw_text(f"Area: {area}", (250, 250 - r - 20), 20)
    g2d.draw_text(f"Circonferenza: {circonferenza}", (250, 250 + r + 20), 20)
    g2d.main_loop()