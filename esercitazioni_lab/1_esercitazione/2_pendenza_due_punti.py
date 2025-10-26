x1 = float(input("Inserisci la coordinata x del primo punto: "))
y1 = float(input("Inserisci la coordinata y del primo punto: "))
x2 = float(input("Inserisci la coordinata x del secondo punto: "))
y2 = float(input("Inserisci la coordinata y del secondo punto: "))

if x1 == x2:
    print("La retta è verticale, la pendenza è indefinita.")
else:
    m = (y2-y1)/(x2-x1)
    print(f"La pendenza della retta passante per i punti inseriti è {m}")